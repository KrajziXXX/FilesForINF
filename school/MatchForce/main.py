class Player:
    def __init__(self, pid, rank, ping, skill, reports, score=0):
        self.pid = pid
        self.rank = rank
        self.ping = ping
        self.skill = skill
        self.reports = reports
        self.score = score
def loadPlayers(filename):
    with open(filename) as f:
        return [Player(pid, rank, int(ping), int(skill), int(reports))
                for line in f if (s := line.strip())
                for pid, rank, ping, skill, reports in [s.split(';')]]
def displayPlayers(players):
    print("ID        RANK       PING   SKILL   REPORTS SCORE")
    print("-------------------------------------------------")
    for player in players:
        print(f'{player.pid} {player.rank} {player.ping} {player.skill} {player.reports} {player.score}')
def filter(players):
    while True:
        print("\nFilter Options:")
        print("1. By ping < 1000ms")
        print("2. By Rank Gold +")
        print("3. By Reports > 20")
        print("4. Exit")
        choice = input("Select filter (1-4): ")
        if choice == '1':
           displayPlayers([p for p in players if p.ping < 1000])
        elif choice == '2':
            ranks = ["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grandmaster"]
            gold_index = ranks.index("Gold")
            displayPlayers([p for p in players if ranks.index(p.rank) >= gold_index])
        elif choice == '3':
            displayPlayers([p for p in players if p.reports > 20])
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            continue
def scoring(players):
    for player in players:
        player.score += player.skill - (player.ping / 100) - (player.reports * 2)
        player.score = int(player.score)
    print("\nPlayer Scorings:")
    return players
def classification(players):
    classifications = []
    for player in players:
        if player.score >70:
            rank = "PRO"
        elif player.score <= 70 and player.score > 40:
            rank = "AVG"
        elif player.score <= 40:
            rank = "RISK"
        classifications.append((player.pid, rank))
    print("\nPlayers Classification:")
    print("ID        RANK")
    print("---------------------")
    for pid, rank in classifications:
        print(f'{pid} {rank}')
    return classifications
def ranking(classifications):
    print("\nPlayers Ranking: ")
    print("ID        RANK")
    print("---------------------")
    for pid,rank in classifications:
        if rank == "PRO" or rank == "AVG":
            print(f'{pid} {rank}')

def matchMaking(players):
    match = []
    first_player_rank = None
    first_player_score = 0
    if len(players) <10:
        print("Not enough players for matchmaking.")
        return
    for player in players:
        if len(match) == 0:
            match.append(player)
            first_player_rank = player.rank
            first_player_score = player.score
        else:
            if player.rank == first_player_rank and abs(player.score - first_player_score) < 15:
                match.append(player)
            if len(match) == 10:
                break
    if len(match) == 10:
        groupA = match[:5]
        avgpingGroupA = sum(p.ping for p in groupA) / 5
        groupB = match[5:]
        avgpingGroupB = sum(p.ping for p in groupB) / 5
        print("\nMatchmaking Results:")
        if avgpingGroupA < avgpingGroupB:
            print("Group A has better average ping.")
        else:
            print("Group B has better average ping.")
        print("Group A:")
        for player in groupA:
            print(f"  {player.pid} - {player.rank} - {player.score}")
        print("Group B:")
        for player in groupB:
            print(f"  {player.pid} - {player.rank} - {player.score}")
def toxicity(players):
    print("\nToxicity Report:")
    for player in players:
        if player.reports >30 and player.score <30:
            print(f'{player.pid}-> TOXIC')
def AntiSmurf(players):
    print("\nAnti-Smurf Report:")
    for player in players:
        if player.skill > 80 and player.rank in ["Bronze", "Silver"]:
            print(f'{player.pid}-> POTENTIAL SMURF')
            print(f"Message sent about promotion to higher rank for {player.pid}")
def AdminPanel(players):
    print("\nAdmin Panel")
    while True:
        print("\nOptions:")
        print("1. Block Player")
        print("2. Change Rank")
        print("3. simulate a match")
        print("4. Exit")
        choice = input("Select option (1-4): ")
        if choice == '1':
            pid = input("Enter Player ID to block: ")
            if any(p.pid == pid for p in players):
                print(f"Player {pid} has been blocked.")
            else:
                print("Player ID not found.")
        elif choice == '2':
            pid = input("Enter Player ID to change rank: ")
            new_rank = input("Enter new rank: ")
            if any(p.pid == pid for p in players):
                for p in players:
                    if p.pid == pid:
                        p.rank = new_rank
                print(f"Player {pid} rank changed to {new_rank}.")
            else:
                print("Player ID not found.")
                
        elif choice == '3':
            matchMaking(players)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
            continue
def main():
    players = loadPlayers("players.txt")
    displayPlayers(players)
    print("\n==========================")
    filter(players)
    print("\n==========================")
    uppdate = scoring(players)
    displayPlayers(uppdate)
    print("\n==========================")
    classifications = classification(uppdate)
    print("\n==========================")
    ranking(classifications)
    print("\n==========================")
    toxicity(uppdate)
    print("\n==========================")
    AntiSmurf(uppdate)
    print("\n==========================")
    AdminPanel(uppdate)

main()