import requests
import smtplib

MY_EMAIL = "mymail"
PASSWORD = "mypassword"

API_KEY = "apikey"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": "yourlat",
    "lon": "yourlon",
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True
        
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="to_mail",
            msg="Subject:Its going to rain!\n\nRemember to bring an umbrella<3"
        )
