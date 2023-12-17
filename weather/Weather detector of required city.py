#Weather detector of required city
import re
import urllib.request
#http://www.weather-forecast.com/locations/Paris/forecasts/latest
city = input("Enter your city: ")
url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
m=re.search('<div class="read-more-content">',data1)
end= m.start()+401
newstr=(data1[m.start():end])
print(newstr)
start=m.end()
final=newstr[start:end]
print(final)