# SMC-Telemetry
Software for getting data from the Super Mileage Car
## LoRa Radios
Each Raspberry Pi device is equipped with a LoRa radio device to allow the car to send data over long distances. This allows for communication necessary for the Trackside Monitor and other uses for the SMC-Telemetry project. Each Raspberry Pi needs to be configured and have permissions set so that the LoRa radios can be used with Python scripts. To enable read and write access to all users and groups, create a udev rule for Raspbian in both Raspberry Pis. In ```/etc/udev/rules.d/``` create a file named ```50-serial-ecu.rules```. In this file, paste the following:
```
KERNEL=="hidraw*", SUBSYSTEM=="hidraw", MODE="0666"
```
## GPS Hardware
Onboard Pi utitilizes Adafruit Ultimate GPS Logger Shield. See https://learn.adafruit.com/adafruit-ultimate-gps-logger-shield for details. For arduino libaries and data parsing see adafruit library https://github.com/adafruit/Adafruit_GPS
## Trackside Monitor
The Trackside Monitor allows the team to visualize live data that is sent from the car to the crew. This will aid in the process of tuning, choosing driving strategies, and understanding what is happening with the car during driving sessions.
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
