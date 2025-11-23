# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    # Converts Fahrenheit to Celsius using global factor
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Converts Celsius to Fahrenheit using global factor
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = input("Enter the temperature to convert: ")

    # Validate numeric input
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    elif unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    else:
        raise ValueError("Invalid temperature unit. Please enter C or F.")

if __name__ == "__main__":
    main()
