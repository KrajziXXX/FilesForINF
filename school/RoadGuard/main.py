zonestxt = "./data/zones.txt"
userstxt = './data/users.txt'
reportstxt = './data/reports.txt'
def main():
    print("RoadGuard")
    #Loaders
    zones = loadzones(zonestxt)
    users = loadusers(userstxt)
    reports = loadreports(reportstxt)

    while True:
        print("|--------Menu--------|")
        print("| 1. Display Zones   |")
        print("| 2. Display Reports |")
        print("| 3. Report          |")
        print("| 4. Exit            |")
        print("|--------------------|")

        choice = int(input("Choice: "))
        if choice == 1:
            display_zones(zones)
            print()
        elif choice == 2:
            display_reports(reports)
            print()
        elif choice == 3:
            zgloszenie(reports)
            print()
        elif choice == 4:
            print("....")
            break
        else:
            print("Error")
            print()
    #...

def loadzones(filename):
    zones = []
    with open(filename, "r",encoding="utf-8") as file:
        zones = [line.strip() for line in file]
    return zones

def loadusers(filename):
    users = []
    with open(filename, "r",encoding="utf-8") as file:
        users = [line.strip() for line in file]
    return users

def loadreports(filename):
    reports = []
    with open(filename, "r",encoding="utf-8") as file:
        reports = [line.strip() for line in file]
    return reports

def display_zones(zone_list):
    print()
    print("----display_zones---")
    print("|-----------------|")
    print("|       Zone      |")
    print("|-----------------|")
    for zone in zone_list:
        print(f"| {zone:<16}|")
    print("|-----------------|")

def display_reports(reports_list):
    print()
    print("----------display_reports---------")
    print("|-------------------------------|")
    print("|    Zone     | Status  |  ID   |")
    print("|-------------|---------|-------|")
    for report in reports_list:
        zone_name, status, id = report.split(";")
        print(f"| {zone_name:<12}| {status:<8}| {id} |")
    print("|-------------------------------|")

def zgloszenie(reports):
    #wybór strefy -> wybór typu zgłoszenia -> przypisanie do użytkownika 
    strefa = input("Podaj Strefe: ")
    print()
    status = input("Podaj typ / status zgłoszenia: ")
    print()
    id = int(input("Podaj swoje id: "))
    reports.append(f"{strefa};{status};{id}")






main()
