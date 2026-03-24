"""
Question 7: Temperature Converter
"""
width = 30

# calculating in a loop
while True:

    # printing menu
    print("\n" + "═" * width)
    print(f"{'TEMPERATURE CONVERTER MENU':^{width}}")
    print("═" * width)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    print("═" * width)

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Exiting...")
        break

    inp = eval(input("Enter temperature value: "))
    result = 0
    unit_a = ""          # temp from
    unit_b = ""          # temp to

    # converting temp
    if choice == '1':
        result = (inp * 9/5) + 32
        unit_a = "Celcius"  
        unit_b = "Fahrenheit"
    elif choice == '2':
        result = (inp - 32) * 5/9
        unit_a = "Fahrenheit" 
        unit_b = "Celsius"
    elif choice == '3':
        result = inp + 273.15
        unit_a = "Celcius"
        unit_b = "Kelvin"
    elif choice == '4':
        result = inp - 273.15
        unit_a = "Kelvin" 
        unit_b = "Celsius"
    elif choice == '5':
        result = (inp - 32) * 5/9 + 273.15
        unit_a = "Fahrenheit"
        unit_b = "Kelvin"
    elif choice == '6':
        result = (inp - 273.15) * 9/5 + 32
        unit_a = "Kelvin" 
        unit_b = "Fahrenheit"
    else:                                                           # incorrect choice
        print("Invalid choice! Please try again.")
        continue

    # print result of conversion
    res_str = f"{inp} {unit_a} = {round(result, 2)} {unit_b}"
    print("\n" + "═" * width)
    print(f"Result: \n{res_str}")
    print("═" * width)



"""
OUTPUT:

══════════════════════════════
  TEMPERATURE CONVERTER MENU
══════════════════════════════
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
4. Kelvin to Celsius
5. Fahrenheit to Kelvin
6. Kelvin to Fahrenheit
7. Exit
══════════════════════════════
Enter your choice (1-7): 1
Enter temperature value: 37

══════════════════════════════
Result:
37 Celcius = 98.6 Fahrenheit
══════════════════════════════

MENU

Enter your choice (1-7): 2
Enter temperature value: 98.6

══════════════════════════════
Result: 
98.6 Fahrenheit = 37.0 Celsius
══════════════════════════════

MENU

Enter your choice (1-7): 9
Enter temperature value: 25
Invalid choice! Please try again.

MENU

Enter your choice (1-7): 7
Exiting...

"""