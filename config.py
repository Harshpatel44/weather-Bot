__author__ = 'Harsh'

intents=["weather",'time']



weather_api="https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22"
time_api="http://api.timezonedb.com/v2/get-time-zone?key=07H8X0FZBUWV&format=json&by=zone&zone="