import requests
import datetime
import smtplib

a = False

def comp_location():
    global a
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if iss_latitude in range(MY_LAT-5, MY_LAT+5) and iss_latitude in range(MY_LNG-5, MY_LNG+5):
        a = True
        mail_sender()
    else:
        a = False
        

def mail_sender():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="to_mail",
            msg="Subject:Look Up!\n\nHeads up, the ISS is right above your head!"
        )

def sun_func():
    sunset_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()
    sunset_data = sunset_response.json()
    sunrise = (int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])+18)%24
    sunset = (int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0])+18)%24
    now = datetime.datetime.now()
    actual_hour = now.hour
    if actual_hour > sunset or actual_hour < sunrise:
        comp_location()
    else:
        print("There's nothing in the sky keep waiting")

MY_EMAIL = "mymail@gmail.com"
PASSWORD = "YOUR PASSWORD"
MY_LAT = "YOUR_LAT"
MY_LNG = "YOUR_LNG"


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

sun_func()
