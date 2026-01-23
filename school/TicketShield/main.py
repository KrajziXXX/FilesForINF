def load(filename):
    with open(filename) as f:
        return [line.strip().split(';') for line in f if line.strip()] 
def display(date):
    print("=======================")
    print("USER   TYPE    QTY   TIME")
    print("------------------------")
    for d in date:
        if d[2] == "VIP":
            print(d[1]," ",d[2],"    ",d[3]," ",d[4])
        else:
            print(d[1]," ",d[2]," ",d[3]," ",d[4])
def system(date):
    #Cennik biletów
    vip_price = 250
    normal_price = 120
    
    #Raport użytkownika
    user_report = {}
    transactions = []
    
    for ticket in date:
        tid, user, ticket_type, qty, time = ticket
        qty = int(qty)
        
        if ticket_type == "VIP":
            transaction_value = qty * vip_price
        else:
            transaction_value = qty * normal_price
        
        transactions.append({
            'tid': tid,
            'user': user,
            'type': ticket_type,
            'qty': qty,
            'time': time,
            'value': transaction_value
        })
        
        if user not in user_report:
            user_report[user] = {
                'purchases': 0,
                'total_tickets': 0,
                'total_amount': 0,
                'transactions': []
            }
        
        user_report[user]['purchases'] += 1
        user_report[user]['total_tickets'] += qty
        user_report[user]['total_amount'] += transaction_value
        user_report[user]['transactions'].append({
            'type': ticket_type,
            'qty': qty,
            'time': time
        })
    
    #Limit zakupu
    print("=======================")
    exceeded = []
    for user, data in user_report.items():
        if data['total_tickets'] > 4:
            exceeded.append(user)
            print(f"{user} → PRZEKROCZENIE ({data['total_tickets']} biletów)")
    
    #Wykrywanie scalperów
    suspicious_users = set()
    
    for user, data in user_report.items():
        if data['total_tickets'] > 4:
            types = [t['type'] for t in data['transactions']]
            if len(set(types)) == 1:
                suspicious_users.add(user)
                print(f"{user} → PODEJRZANY (Scalper)")
            else:
                print(f"{user} → PODEJRZANY (Różne typy biletów)")
    
    print("=======================")
    #kwoty transakcji
    print(f"NORMAL: {normal_price} zł | VIP: {vip_price} zł")
    print("\nTransakcje:")
    for trans in transactions:
        print(f"{trans['tid']} | {trans['user']} | {trans['type']:6} | {trans['qty']} szt | {trans['value']} zł | {trans['time']}")
    
    #Raport użytkownika
    print("USER   | ZAKUPY | BILETY | RAZEM ZŁ")
    print("-------|--------|--------|----------")
    for user in sorted(user_report.keys()):
        data = user_report[user]
        print(f"{user:6} | {data['purchases']:6} | {data['total_tickets']:6} | {data['total_amount']:8}")
    print("=======================")
    #Ranking sprzedaży
    #TOP użytkownicy
    top_users = sorted(user_report.items(), key=lambda x: x[1]['total_amount'], reverse=True)
    print("\nTOP UŻYTKOWNICY:")
    for i, (user, data) in enumerate(top_users[:3], 1):
        print(f"  {i}. {user}: {data['total_amount']} zł ({data['total_tickets']} biletów)")
    
    #TOP godziny sprzedaży
    hours = {}
    for trans in transactions:
        hour = trans['time'].split(':')[0]
        if hour not in hours:
            hours[hour] = 0
        hours[hour] += trans['value']
    
    top_hours = sorted(hours.items(), key=lambda x: x[1], reverse=True)
    print("\nTOP GODZINY SPRZEDAŻY:")
    for i, (hour, amount) in enumerate(top_hours[:3], 1):
        print(f"  {i}. {hour}:00 - {amount} zł")
    
    #Najczęściej kupowany typ biletu
    ticket_types = {}
    for trans in transactions:
        if trans['type'] not in ticket_types:
            ticket_types[trans['type']] = {'qty': 0, 'amount': 0}
        ticket_types[trans['type']]['qty'] += trans['qty']
        ticket_types[trans['type']]['amount'] += trans['value']
    
    print("POPULARNOŚĆ TYPÓW BILETÓW:")
    for ticket_type in sorted(ticket_types.keys()):
        data = ticket_types[ticket_type]
        print(f"  {ticket_type}: {data['qty']} szt | {data['amount']} zł")


def admin_mode(date):
    #Tryb Admina
    blacklist = set()
    blocked_transactions = set()
    
    print("\n" + "="*50)
    print("TRYB ADMINA")
    print("="*50)
    
    while True:
        print("\nMENU:")
        print("1. Zablokuj użytkownika")
        print("2. Anuluj transakcję")
        print("3. Zmień ceny biletów")
        print("4. Wyświetl czarną listę")
        print("5. Wyjdź")
        print("-" * 50)
        
        choice = input("Wybierz opcję: ").strip()
        
        if choice == "1":
            user_id = input("Podaj ID użytkownika: ").strip()
            exists = any(ticket[1] == user_id for ticket in date)
            if exists:
                blacklist.add(user_id)
                print(f"Użytkownik {user_id} dodany do czarnej listy!")
            else:
                print(f"Użytkownik {user_id} nie istnieje!")
                
        elif choice == "2":
            trans_id = input("Podaj ID transakcji: ").strip()
            exists = any(ticket[0] == trans_id for ticket in date)
            if exists:
                blocked_transactions.add(trans_id)
                print(f"Transakcja {trans_id} została zablokowana!")
            else:
                print(f"Transakcja {trans_id} nie istnieje!")
                
        elif choice == "3":
            print("ZMIANA CEN BILETÓW")
            while True:
                print("1. VIP")
                print("2. NORMAL")
                print("3. EXIT")
                price_choice = input("Wybierz: ").strip()
                
                if price_choice == "1":
                    try:
                        new_price = int(input("Nowa cena VIP: "))
                        print(f"Cena VIP ustawiona na {new_price} zł")
                    except ValueError:
                        print("Błąd: Podaj liczbę!")
                        
                elif price_choice == "2":
                    try:
                        new_price = int(input("Nowa cena NORMAL: "))
                        print(f"Cena NORMAL ustawiona na {new_price} zł")
                    except ValueError:
                        print("Błąd: Podaj liczbę!")
                        
                elif price_choice == "3":
                    break
                else:
                    print("Nieznana opcja!")
                    
        elif choice == "4":
            print("\nCZARNA LISTA:")
            if blacklist:
                for user in sorted(blacklist):
                    print(f"  - {user}")
            else:
                print("  (pusta)")
                
        elif choice == "5":
            print("Wychodzisz z trybu admina...")
            break
        else:
            print("Nieznana opcja!")


def main():
    date = load("tickets.txt")
    display(date)
    system(date)
    admin_mode(date)

main()