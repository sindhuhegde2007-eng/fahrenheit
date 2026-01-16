from fahrenheit import classify_temperature

def test_zero_celsius():
    assert classify_temperature(0) == "Temperature:0\nStatus:Cold"

def test_boiling_point():
    assert classify_temperature(100) == "temperature:212\nstatus:hot"

def test_negative_temperature():
    assert classify_temperature(-40) == "temperature:-40\nstatus:normal"

