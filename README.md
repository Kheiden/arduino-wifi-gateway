# Arduino WiFi webserver

This python code is used to generate Arduino code which can be deployed on an Arduino Uno R4 Wifi.


## Prerequisites

Run `pip3 install -r requirements.txt` in your python environment of choice.

Copy `.env.template` to `.env` and update the environment variable to match your Wifi
SSID and password.

Make HTML updates to `create_source/input_html/index.html`

## Usage

Run `python3 main.py`

Upload the directory `ArduinoCode` to the Arduino.