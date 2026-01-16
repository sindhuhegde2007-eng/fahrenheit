def classify_temperature(temp):
    if temp < 20:
        status = "Cold"
    elif temp <= 30:
        status = "Normal"
    else:
        status = "Hot"

    result = (
        f"Temperature:{temp}\n"
        f"Status:{status}"
    )
    return result


if __name__ == "__main__":
    temp = 32
    print(classify_temperature(temp))
