import smtplib
import datetime as dt
import random

#Email ID & Password
MY_EMAIL = "pythontest0811@gmail.com"
PASSWORD = "faryltfdgtqrickd"

#Send emails on selected days
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    # Open the file to email
    with open("quotes.txt", "r") as quotes_data:
        all_quote = quotes_data.readlines()
        quote = random.choice(all_quote)
        
    #Sending email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="pythontest0811@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
