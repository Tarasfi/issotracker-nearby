import requests
from datetime import datetime
import smtplib
import time

my_email = "tarasfikroy@gmail.com"
password = "aabxmrbquxpkyckg"

MY_LAT = 51.909586 # Your latitude
MY_LONG = 8.381067 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longtitude"])

#Your position is within +5 or -5 degrees of the ISS position.


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

time_now = datetime.now()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



def check_nearby():
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5) and (MY_LONG - 5 <= iss_longitude <= MY_LONG + 5) and time_now.hour < sunrise:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="banebhop@gmail.com",
                msg=f"Subject: ISS is close to your location \n\n Go outside and look above you!!! \n\n This code was written 15.10.24 00:35 \n\n Path: pyth/isso-task-day33"
            )
        print("Succes")
    else:
        print("Fail")




while True:
    check_nearby()
    time.sleep(60)