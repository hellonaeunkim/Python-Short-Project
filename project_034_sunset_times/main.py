import requests
from datetime import datetime
import smtplib
import time

#Email ID & Password
MY_EMAIL = "pythontest0811@gmail.com"
PASSWORD = "faryltfdgtqrickd"
RECIEVER_EMAIL = "pythontest0811@gmail.com"

#Send the e-mail
def sending_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIEVER_EMAIL,
            msg="Subject:Look Up!👆\n\nThe ISS is above you in the sky."
        )
    
#Address
MY_LAT = 49.282730 # Vancouver latitude
MY_LONG = -123.120735 # Vancouver longitude

def is_iss_overhead():
    #ISS Positions API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    #Current position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    #Sunrise and Sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    # It's dark
    if time_now <= sunrise or time_now >= sunset:
        return True

while True:
    # Run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():
        sending_mail()


