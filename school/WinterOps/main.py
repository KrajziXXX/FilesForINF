zonefile = "data/zones.txt"
vehiclesfile = "data/vehicles.txt"
def read_zones(filename):
    zones = []
    with open(filename, "r",encoding="utf-8") as file:
        zones = [line.strip() for line in file]
    return zones

def display_zones(zone_list):
    print()
    print("-----------Zones-----------")
    print("---------------------------")
    print("     Zone        | Status")
    print("-----------------|---------")
    for zone in zone_list:
        zone_name, status = zone.split(";")
        print(f"{zone_name:<16} | {status:<6} |")

def read_vehicles(filename):
    vehicles = []
    with open(filename, "r", encoding="utf-8") as file:
        vehicles = [line.strip() for line in file]
    return vehicles

def display_vehicles(veh_list):
    print()
    print("-----------Vehicles---------")
    print("----------------------------")
    print("     Vehicle   | Status")
    print("---------------|------------")
    for vehicle in veh_list:
        vehicle_name, status = vehicle.split(";")
        print(f"{vehicle_name:<14} | {status:<9} |")

def snowrem(veh_list, zone_list):
    print()
    while True:
        print("\nOptions:")
        print("1. Assign vehicle to zone")
        print("2. Change vehicle status")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            print("\nAssign Vehicle to Zone")
            print("\nAvailable Vehicles:")
            for i, vehicle in enumerate(veh_list):
                print(f"{i + 1}. {vehicle}")
            vehicle_choice = int(input("Select a vehicle by number: ")) - 1
            vehicle_name, vehicle_status = veh_list[vehicle_choice].split(";")
            if vehicle_status == "w_trakcie":
                print(f"\nVehicle '{vehicle_name}' cannot be assigned because its status is 'w_trakcie'.")
                continue
            print("\nAvailable Zones:")
            for i, zone in enumerate(zone_list):
                print(f"{i + 1}. {zone}")
            zone_choice = int(input("Select a zone by number: ")) - 1
            zone_name, _ = zone_list[zone_choice].split(";")
            print(f"\nNazwa_Sprzetu: {vehicle_name}  | Strefa: {zone_name}")

        elif choice == "2":
            print("\nChange Vehicle Status")
            print("Available Vehicles:")
            for i, vehicle in enumerate(veh_list):
                print(f"{i + 1}. {vehicle}")
            vehicle_choice = int(input("Select a vehicle by number: ")) - 1

            new_status = input("Enter new status: ")
            vehicle_name, _ = veh_list[vehicle_choice].split(";")
            veh_list[vehicle_choice] = f"{vehicle_name};{new_status}"
            print(f"\nUpdated status of {vehicle_name} to {new_status}")

        elif choice == "3":
            print("\nExiting Snow Removal Management.")
            break

        else:
            print("\nInvalid choice. Please try again.")



zones = read_zones(zonefile)
display_zones(zones)
vehicles = read_vehicles(vehiclesfile)
display_vehicles(vehicles)
print()
snowrem(vehicles,zones)
