number_of_consumers = int(input("Enter number of consumers: "))

for number in range(1, number_of_consumers + 1):
    name = input(f"Consumer {number}: ")
    units = int(input("Units: "))

    if units < 0:
        print(f"Invalid units for {name} - Skipped")
        continue

    if units == 0:
        print("0 units entered. Processing stopped.")
        break

    if units <= 100:
        rate = 2
    elif units <= 200:
        rate = 3
    elif units <= 300:
        rate = 5
    else:
        rate = 7

    bill = units * rate
    print(f"{name} - {units} units - Bill: Rs. {bill}")
