from myProject.weather import check_weather
import pytest

'''def test_check_weather1():
    assert check_weather(21.00) == "hot", "temperature greater than 20° must be considered as hot temp"

def test_check_weather2():
    assert check_weather(5.00) == "average", "temperature between 10 and 20 must be considered as average temp"

def test_check_weather3():
    assert check_weather(5.00) == "cold", "temperature lower than 10 degrees must considered as cold"

def test_check_weather4():
    assert check_weather(13.00) == "average", "temperature between 10 and 20 must be considered as average temp"

def test_check_weather5():
    assert check_weather(30.00) == "hot", "temperature greater than 20° must be considered as hot temp"
    assert check_weather(11.00) == "cold", "temperature lower than 10 degrees must considered as cold"
'''
@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")

])
def test_check_weather(temperature, expected):
    ae:str=""
    if temperature>20:
        ae ="temperatures greater thena 20 degeree must be considered as hot"
    elif 10 <temperature <20:
        ae ="temperatures greater thena 20 degeree must be considered as average temp"
    else:
        ae ="temperatures greater thena 20 degeree must be considered as cold"

    assert check_weather(temperature) == expected, ae
'''def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected'''
