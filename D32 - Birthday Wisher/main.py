##################### Extra Hard Starting Project ######################
# Import libraries
import pandas as pd
import random
import smtplib
import datetime as dt

my_email = "mymail@gmail.com"
password = "mypassword"

todays_date = dt.datetime.now()
today = (todays_date.month,todays_date.day)
data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
        text = file.read()
        new_text = text.replace("[NAME]", birthday_dict[today]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_dict[today]["email"],
            msg=f"Subject:Happy Birthday! <3\n\n{new_text}"
        )
