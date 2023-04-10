import requests

class OpenWeatherMap:
  def __init__(self, api_key, query):
    self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    self.API_KEY = api_key
    self.QUERY = query
    self.URL = self.BASE_URL + "q=" + self.QUERY + "&APPID=" + self.API_KEY

  def get_data(self):
    response = requests.get(self.URL)
    return response.json()
