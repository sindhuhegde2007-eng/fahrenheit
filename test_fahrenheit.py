from fahrenheit import classify_temperature


def test_temperature_case1():
    expected_output = (
        "Temperature:10\n"
        "Status:Cold"
    )
    assert classify_temperature(10) == expected_output


def test_temperature_case2():
    expected_output = (
        "Temperature:25\n"
        "Status:Normal"
    )
    assert classify_temperature(25) == expected_output


def test_temperature_case3():
    expected_output = (
        "Temperature:35\n"
        "Status:Hot"
    )
    assert classify_temperature(35) == expected_output
