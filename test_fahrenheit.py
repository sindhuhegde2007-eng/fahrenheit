from temperature import celsius_to_fahrenheit

def test_zero_celsius():
    result = celsius_to_fahrenheit(0)
    print("0C ->", result)
    assert result == 32

def test_boiling_point():
    result = celsius_to_fahrenheit(100)
    print("100C ->", result)
    assert result == 212

def test_negative_temperature():
    result = celsius_to_fahrenheit(-40)
    print("-40C ->", result)
    assert result == -40

