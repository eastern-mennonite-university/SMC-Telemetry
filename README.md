# SMC-Telemetry
Software for getting data from the Super Mileage Car
## Cellular Communication
In order for us to get data from the car to the rest of the team that's trackside, we teather our phones to the Pi using USB and send data to a DNS server at EMU. This works with either Android or iOS, but on Android it is able to explicitly be enabled or disabled. iOS automaticly enables or disables it, inherently making it more finicky than Android as we have no control.
## GPS Hardware
Onboard Pi utitilizes an Arduino with the Adafruit Ultimate GPS Logger Shield attached to it. See https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield for details. For arduino libaries and data parsing see adafruit library https://github.com/adafruit/Adafruit_GPS
## CAN Hardware
The Megasquirt ECU mainly uses USB/Serial to burn changes to the firmware, it is easier to configure the ECU's CAN Bus to broadcast the data we want. We use an Adafruit CAN Feather to capture the data. See https://learn.adafruit.com/adafruit-rp2040-can-bus-feather/overview for details. This link also provides details on how to set it up with the Arduino IDE. 
## Trackside Monitor
The Trackside Monitor allows the team to visualize live data that is sent from the car to the crew. This will aid in the process of tuning, choosing driving strategies, and understanding what is happening with the car during driving sessions.

There are two parts to this monitor: the websocket and the Django server.

The websocket runs on the Pi in the car and will stream data to the Django server. The server runs in Replit and allows us to give anyone the development URL and let them view the data. 

#### Note that as of Jan 1st, 2024 we cannot make custom dev URLs, so the URL will need to be changed in the WSsend.py file on the Pi everytime we have a new one.

When in the Replit dashboard for the repo, all you need to do is press the green 'Run' button and it will launch Django for you.

### Build
The Trackside Monitor build will need to run on the RaspberryPi that is connected to the router with the crew. It is on the receiving end of LoRa transmissions from the car.
#### Dependencies
* Django
* django_eventstream
* channels (version 3.0.5)

Each of these dependencies will need to be installed for the Trackside Monitor to run. They can be installed as such:
```
pip install Django django_eventstream channels==3.0.5
```
#### Build Django
1. In ```trackside_monitor_project/settings.py``` set ```SECRET_KEY = config('SECRET_KEY')``` to the secret key for this application. For EMU Super Mileage Car team members, get the key from a team member. For other cases, use Django's documentation to determine how to generate a new secret key, and instead use that key for this application. Otherwise, it should be fine to set this to an arbitrary string, as signing, encryption, and other security measures will likely not be needed for this application as data is unlikely to be sensitive.
2. In ```trackside_monitor_project/settings.py``` add the IP address of the trackside Raspberry Pi to the ALLOWED_HOSTS list. Change ```ALLOWED_HOSTS = []``` to ```ALLOWED_HOSTS = ['<ip_address>',]``` where ```<ip_address>``` using the appropriate ip address.
3. Move static files to Django's root. Run ```python trackside_monitor_project/manage.py collectstatic```.
4. Create Django model migrations. Run ```python trackside_monitor_project/manage.py makemigrations```.
5. Apply migrations. Run ```python trackside_monitor_project/manage.py migrate```.
### Running the Application
After installing all of the dependencies and completing the build steps above, it should be possible to run the application. To start the server run ```trackside_monitor_project/manage.py runserver <ip_address>:8000```. When the server is running the page can be accessed at ```http://<ip_address>:8000``` e.g. [http://localhost:8000](http://localhost:8000) on the device the server is running on.
