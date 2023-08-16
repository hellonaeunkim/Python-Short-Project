import random
import pandas
from datetime import datetime
import smtplib

#Datetime
today = datetime.now()
today_tuple = (today.month, today.day)

#Read csv file
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row.day): data_row for (index, data_row) in data.iterrows()}

#Email ID & Password
MY_EMAIL = "pythontest0811@gmail.com"
PASSWORD = "faryltfdgtqrickd"

#Check if today matches a birthday in the birthdays.csv
if today_tuple in birthdays_dict:
    #Get the birthday person's name
    birthday_person = birthdays_dict[today_tuple]
    #Pick a random letter from letter templates
    random_num = random.randint(1,4)
    file_path = f"letter_templates/letter_{random_num}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
    #Replace the [NAME] with the person's actual name from birthdays.csv
        contents.replace("[NAME]", birthday_person.name)

    #Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person.email,
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
