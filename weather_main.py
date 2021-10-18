import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}


api_key = "api_key must be written here"
account_sid = 'AC747614aefb2a77f9501c3efbb57457ef'
auth_token = 'auth_token must be written here'

weather_params = {
    "lat": 14.582260,
    "lon": 120.974800,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
data = response.json()

weather_forecast = [data["hourly"][i]["weather"][0]["id"] for i in range(12)]

print(weather_forecast)
flag=False
for i in weather_forecast:
    if i <= 900:
        flag=True
        break

if flag:
    client = Client(account_sid, auth_token,  http_client=proxy_client)

    message = client.messages.create(
        to="user's tel number",
        from_="+14123856885",
        body="You don't need to take an umbrella today!")

else:
    client = Client(account_sid, auth_token,  http_client=proxy_client)

    message = client.messages.create(
        to="user's tel number",
        from_="+14123856885",
        body="Take your umbrella, Today is rainy!")


print(message.status)




































