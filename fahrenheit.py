import sys

# Check if argument is provided
if len(sys.argv) != 2:
    print("Usage: python celsius_to_fahrenheit.py <celsius_value>")
    sys.exit(1)

# Read Celsius value from command line
celsius = float(sys.argv[1])

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Display result
print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
