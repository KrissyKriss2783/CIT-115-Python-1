# Welcome message with name and hungarian notations

print(f"Crystal Lamb's Temp Converter:\n ")

# Prompt the user for temperature
f_temperature = input("Please enter a temperature:")

try:
    f_temperature = float(f_temperature)
except ValueError:#is raised when a function receives an argument of the correct type but an inappropriate value. TypeError didn't work!
        print("Please enter a valid number for the temperature.")
else:
    # Prompt user for unit
    s_unit = input("Is the temperature in (F)ahrenheit or (C)elsius? ")

    if s_unit not in ('F', 'C', 'f', 'c'):
        print("Enter a F or C")
    else:
        # Convert it from Fahrenheit to Celsius
        if s_unit in ('F','f'):
            if f_temperature > 212:
                print("Temp can not be > 212")
            else:
                f_celsius = (5.0 / 9) * (f_temperature - 32)
                print(f"The Celsius equivalent is: {f_celsius:.1f}")

        # Convert it from Celsius to Fahrenheit
        elif s_unit in ('C','c'):
            if f_temperature > 100:
                print("Temp can not be > 100")
            else:
                f_fahrenheit = ((9.0 / 5.0) * f_temperature) + 32
                print(f"The Fahrenheit equivalent is: {f_fahrenheit:.1f}")

