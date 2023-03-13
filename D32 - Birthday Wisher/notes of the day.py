import smtplib
import datetime as dt
import random

with open("quotes.txt", "r") as file:
    data = file.read()
    list_of_quotes = data.split("\n")

my_email = "ingmiguelgaona@gmail.com"
password = "xudtmgnipbqrbvqc"

now = dt.datetime.now()
# year = now.year
# month = now.month
day_of_week = now.weekday()
# print(day_of_week)

# date_of_birth = dt.datetime(year=1999, month=10, day=14)
# print(date_of_birth)

if day_of_week == 0:
    random_message = random.choice(list_of_quotes)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="miguelgaona714@gmail.com",
            msg=f"Subject:Mensaje de miercoles <3\n\n{random_message}"
        )
else:
    print("Have a nice day")