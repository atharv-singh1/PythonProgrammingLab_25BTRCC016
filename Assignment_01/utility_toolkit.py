import math

while True:
    print("\n========== PERSONAL UTILITY TOOL ==========")
    print("1. Celsius to Fahrenheit Conversion")
    print("2. Fahrenheit to Celsius Conversion")
    print("3. Calculate Area of Circle")
    print("4. Calculate Simple Interest")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit}")

    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"Temperature in Celsius: {celsius}")

    elif choice == 3:
        radius = float(input("Enter radius of circle: "))
        area = math.pi * radius * radius
        print(f"Area of Circle: {area}")

    elif choice == 4:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest: "))
        time = float(input("Enter time in years: "))
        simple_interest = (principal * rate * time) / 100
        print(f"Simple Interest: {simple_interest}")

    elif choice == 5:
        print("Thank you for using the Personal Utility Tool.")
        break

    else:
        print("Invalid choice. Please try again.")
