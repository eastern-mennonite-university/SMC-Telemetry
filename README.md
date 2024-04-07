# SMC-Telemetry
Software for getting data from the Super Mileage Car
## Cellular Communication
In order for us to get data from the car to the rest of the team that's trackside, we are using a LTE hat to connect the Pi to cellular networks
https://www.jeffgeerling.com/blog/2022/using-4g-lte-wireless-modems-on-raspberry-pi
## GPS Hardware
Onboard Pi utitilizes an Arduino with the Adafruit Ultimate GPS Logger Shield attached to it. See https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield for details. For arduino libaries and data parsing see adafruit library https://github.com/adafruit/Adafruit_GPS
## CAN Hardware
The Megasquirt ECU mainly uses USB/Serial to burn changes to the firmware, it is easier to configure the ECU's CAN Bus to broadcast the data we want. We use an Adafruit CAN Feather to capture the data. See https://learn.adafruit.com/adafruit-rp2040-can-bus-feather/overview for details. 
## Trackside Monitor
The Trackside Monitor allows the team to visualize live data that is sent from the car to the crew. This will aid in the process of tuning, choosing driving strategies, and understanding what is happening with the car during driving sessions.

There are two parts to this monitor: the websocket and the Django server.

The websocket runs on the Pi in the car and will stream data to the Django server. The server runs in Replit and allows us to give anyone the development URL and let them view the data. 

#### Note that as of Jan 1st, 2024 we cannot make custom dev URLs, so the URL will need to be changed in the WSsend.py file on the Pi everytime we have a new one.

When in the Replit dashboard for the repo, all you need to do is press the green 'Run' button and it will launch Django for you.
