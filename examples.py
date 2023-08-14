"""
https://github.com/Python-oop/Api_practice
http://open-notify.org/Open-Notify-API/ISS-Location-Now/
https://www.webfx.com/web-development/glossary/http-status-codes/
https://docs.python-requests.org/en/latest/
https://kanye.rest/
https://sunrise-sunset.org/api
"""

import  requests
from datetime import datetime
MY_LAT = 28.237988
MY_LON = 83.995590

# response = requests.get(url='http://api.open-notify.org/iss-now.json')

# data = response.json()

# latitude = data['iss_position']['latitude']
# longitude = data['iss_position']['longitude']
# print(latitude)

parameters = {
    'lat':MY_LAT,
    'lon':MY_LON,
    'formatted': 0,
}

response  = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']
sunrise_time = sunrise.split('T')[1].split(':')[0]
sunset_time = sunset.split('T')[1].split(':')[0]

print(sunrise_time)

time_now = datetime.now()
print(time_now.hour)




# def get_quote():
#     response = requests.get(url='https://api.kanye.rest')
#     data = response.json()
#     quote = data['quote']
#     canvas.itemconfig(quote_text, text=quote, font=("Arriel", 14, "bold"))
#     #Write your code here.