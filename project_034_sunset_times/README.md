# project_034_sunset_times

```python3
import requests
from datetime import datetime
import smtplib
import time
```
<p>
The code begins by importing necessary modules:<br/><br/>
* <b>requests</b> : Used for making HTTP requests to web services and APIs.<br/>
* <b>datetime</b> : Used for handling date and time information.<br/>
* <b>smtplib</b> : Used for sending email messages.<br/>
* <b>time</b> : Used for handling time-related functions.<br/>
</p>

```python3
# Email ID & Password
MY_EMAIL = "pythontest0811@gmail.com"
PASSWORD = "faryltfdgtqrickd"
RECEIVER_EMAIL = "pythontest0811@gmail.com"
```
<p>
The code sets up email credentials for sending notifications. Replace these values with your own email and password.
</p>

```python3
# Send the email
def sending_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg="Subject:Look Up!👆\n\nThe ISS is above you in the sky."
        )

```
<p>
The <b>sending_mail</b> function is defined, which is responsible for sending an email notification. It uses the Gmail SMTP server to send an email with a specific subject and message.
</p>

```python3
# Address
MY_LAT = 49.282730  # Vancouver latitude
MY_LONG = -123.120735  # Vancouver longitude

```
<p>
The latitude and longitude coordinates for a specific location (in this case, Vancouver) are defined. This location will be used to check if the International Space Station (ISS) is overhead.
</p>

```python3
def is_iss_overhead():
    # ISS Positions API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    # Current position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

```
<p>
The <b>is_iss_overhead</b> function is defined to check if the ISS is overhead. It makes an HTTP request to an ISS position API, extracts the ISS's current latitude and longitude, and checks if the ISS is within +5 or -5 degrees of the specified location (Vancouver). If it is, the function returns <b>True</b>.
</p>

```python3
def is_night():
    # Sunrise and Sunset API
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

```
<p>
The <b>is_night</b> function checks if it's nighttime at the specified location. It uses a Sunrise and Sunset API to retrieve sunrise and sunset times for the location (Vancouver). It then compares the current hour with these times to determine if it's nighttime. If it is, the function returns <b>True</b>.
</p>

```python3
while True:
    # Run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():
        sending_mail()

```
<p>
The code enters an infinite loop that runs continuously. It sleeps for 60 seconds between each iteration. During each iteration, it checks if both <b>is_iss_overhead</b> and <b>is_night</b> functions return <b>True</b>. If both conditions are met (the ISS is overhead, and it's nighttime), it sends an email using the <b>sending_mail</b> function.
</p>

<p>
In summary, this Python code continuously checks if the International Space Station (ISS) is overhead and if it's nighttime at a specified location (Vancouver). 
If both conditions are met, it sends an email notification to the provided email address. 
The code runs indefinitely, checking these conditions every 60 seconds.
</p>
