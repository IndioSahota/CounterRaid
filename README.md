# CounterRaid

### Anti-Theft Application

Cybersecurity is paramount in fostering sound computer networks and systems; it encapsulates many things from protecting our data from cyber attackers who would wish to steal this information and cause harm. Sensitive data, personal information, governmental and industry information, intellectual property, and many other media of delicate information are always at risk, and CounterRaid is designed to address such fears. 

CounterRaid can be activated by sending a text message to the Twilio number. Once activated CounterRaid will take the current IP address and locational details of your device, in addition to taking a picture through the webcam. From there, it will actively send SMS messages every two minutes containing logged data of what has been typed on the laptop. The purpose of this is to check if any passwords or other various forms of private information have been accessed. 

In order to run CounterRaid, the following commands should be run through the terminal to install dependencies:

`pip install opencv-contrib-python`
`pip install geocoder`
`pip install twilio`
`pip install pyimgur`
