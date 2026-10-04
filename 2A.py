slots = {
    1: ["Car", True],
    2: ["Bike", True],
    3: ["Car", True],
    4: ["EV", False],
    5: ["Car", False],
    6: ["Bike", True]
}

while True:
    print("\nWelcome to Parking System!")
    print("1. Park Vehicle")
    print("2. Remove Vehicle")
    print("3. Show Parking Status")
    print("4. Exit")

    ch = int(input("Enter your choice (1,2,3,4): "))

    # Park a vehicle
    if ch == 1:
        v = input("Enter vehicle type (Car/Bike/EV): ")
        found = False

        for s in slots:
            # Check vehicle type and whether slot is empty
            if slots[s][0] == v and slots[s][1]:
                slots[s][1] = False
                print("Vehicle parked successfully in slot", s)
                found = True
                break

        if not found:
            print("No parking available")

    # Remove a vehicle
    elif ch == 2:
        s = int(input("Enter the slot number to remove the vehicle: "))

        if s in slots and not slots[s][1]:
            slots[s][1] = True
            print("Vehicle removed successfully")
        else:
            print("Parking already empty or invalid slot")

    # Show parking status
    elif ch == 3:
        for s in slots:
            status = "Empty" if slots[s][1] else "Occupied"
            print("Slot", s, "->", slots[s][0], "Status ->", status)

    # Exit
    elif ch == 4:
        break

    else:
        print("Invalid choice!")
