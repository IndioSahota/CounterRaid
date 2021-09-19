from constants import *
from twilio.rest import Client
import camera
import geolocator

# The Twilio client
client = Client(account_sid, auth_token)
data = geolocator.get_location()
sms = "ALERT: THREAT DETECTED!" \
          + "\n\nIP: " + data['query'] \
          + "\nISP: " + data['isp'] \
          + "\nLocation: " + data['city'] + ", " + data['region'] + ", " + data['country'] \
          + "\nCoordinates (Latitude, Longitude): " + str(data['lat']) + ", " + str(data['lon'])


# Method for reporting keylogged data to the user via SMS (twilio)
def report():
    # takes pictures
    camera.use_camera()
    # Creates message
    message = client.messages.create(
        to=USER_NUMBER,
        from_=TWILIO_NUMBER,
        body="\n\n" + sms,
        media_url=['https://c1.staticflickr.com/3/2899/14341091933_1e92e62d12_b.jpg'])
