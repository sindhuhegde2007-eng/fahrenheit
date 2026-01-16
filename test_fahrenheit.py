from fahrenheit import classify_temperature

def test_zero_celsius():
    assert classify_temperature(0) == expected_output

def test_boiling_point():
    assert classify_temperature(100) == expected_output

def test_negative_temperature():
    assert classify_temperature(-40) == expected_output

