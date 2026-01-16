def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


if __name__ == "__main__":
    c = float(input("enter the number"))
    f = celsius_to_fahrenheit(c)

    print("Temperature in Celsius:", c)
    print("Temperature in Fahrenheit:", f)
