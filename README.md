# OpenWeatherMap API
Python simple wrapper for OpenWeatherMap API
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
