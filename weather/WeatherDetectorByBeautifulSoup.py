#Weather detector of required city
import re
import urllib.request
from bs4 import BeautifulSoup
#http://www.weather-forecast.com/locations/<Required City>/forecasts/latest
city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
soup=BeautifulSoup(data1)
result=soup.find_all('span')
print(result[30].contents)