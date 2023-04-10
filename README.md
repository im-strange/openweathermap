# OpenWeatherMap API
Python simple wrapper for OpenWeatherMap API
<br><br> 

Clone this repo and move `pyowmp.py` into your working directory, or,
just copy and paste `pyowmp.py` from this repo.
<br>

### Example usage
```py
import requests
from pyowmp import OpenWeatherMap

API_KEY = "your_api_key"
query = "London"
openweather = OpenWeatherMap(API_KEY, query)

data = openweather.get_data()
```
<br>

> Replace with your own API key. `query` can be city name or `lat&long` object.
<br> 

If the request is good, you will receive dictionary/json
object. See below:
```json
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 803,
      "main": "Clouds",
      "description": "broken clouds",
      "icon": "04d"
    }
  ],
  "base": "stations",
  "main": {
    "temp": 287.69,
    "feels_like": 286.84,
    "temp_min": 284.18,
    "temp_max": 288.96,
    "pressure": 1006,
    "humidity": 63
  },
  "visibility": 10000,
  "wind": {
    "speed": 7.2,
    "deg": 240
  },
  "clouds": {
    "all": 75
  },
  "dt": 1681139615,
  "sys": {
    "type": 2,
    "id": 2075535,
    "country": "GB",
    "sunrise": 1681103782,
    "sunset": 1681152422
  },
  "timezone": 3600,
  "id": 2643743,
  "name": "London",
  "cod": 200
}
```
<br>

If something is wrong, error
message will be sent.
```json
{
  "cod": "404",
  "message": "city not found"
}
```
<br>

Note:
> Use the repository's content only for
legal and ethical purposes.
