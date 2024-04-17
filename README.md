# IOT-TempAlert

## Description
IOT-TempAlert is a Python-based project designed to monitor temperature levels and send alerts to users via SMS, email, and Telegram Bot when the temperature exceeds a predefined threshold value. It utilizes hardware components such as a temperature sensor and a Wi-Fi module (ESP8266) integrated into a module called BOLT for sensing and transmitting temperature data to the cloud. The cloud, hosted by the BOLT module, stores temperature readings at regular intervals and provides graphical representations for easy monitoring.

## Features
- **Temperature Monitoring**: The project continuously monitors temperature levels using a temperature sensor connected to the ESP8266 module.
- **Threshold Alerting**: When the temperature exceeds the predefined threshold value, the system triggers an alert mechanism.
- **Alert Mechanisms**:
  - SMS Alert: Uses Twilio API to send SMS alerts to users' mobile phones.
  - Email Alert: Utilizes Twilio API to send email alerts to users' email addresses.
  - Telegram Bot Alert: Sends alerts to users who are members of a specified Telegram channel using Telegram Bot API.
- **Cloud Storage**: Temperature data is stored in the cloud hosted by the BOLT module, allowing users to access historical temperature readings and graphical representations.

## Hardware Components
- Temperature Sensor: Used to measure temperature levels.
- ESP8266 Wi-Fi Module (BOLT): Integrated with the temperature sensor for transmitting data to the cloud.

## Software Components
- Python 3: Programming language used for developing the project.
- Twilio API: Utilized for sending SMS and email alerts.
- Request Library: Used for making API calls to the Telegram Bot for sending alerts to Telegram channels.
- BOLT Cloud: Hosts the cloud infrastructure for storing temperature data and providing graphical representations.

## Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Gittecho/IOT-TempAlert.git

## Requirements 
1. Install the required Python dependencies using pip:
   ```bash
   pip install -r requirements.txt
2. Set up Twilio and Telegram Bot APIs with the necessary credentials.
3. Configure the ESP8266 module to connect to the Wi-Fi network and transmit temperature data to the BOLT cloud.

## Usage 
1. Start the Python script on a device connected to the BOLT module and temperature sensor.
2. Monitor the temperature readings on the BOLT cloud platform or through the provided graphical representations.
3. Receive alerts via SMS, email, or Telegram Bot when the temperature exceeds the threshold value.

## Contributing
Contributions to the IOT-TempAlert project are welcome! Whether you're a developer, hardware enthusiast, or have suggestions for improvements, feel free to contribute by opening issues or submitting pull requests.

## License
This project is licensed under the MIT License, allowing for free use, modification, and distribution of the codebase.
