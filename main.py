import requests  # for making HTTP requests
import json  # library for handling JSON data
import time  # module for sleep operation

from boltiot import Bolt  # importing Bolt from boltiot module
from conf import confy as co  # config file


class Boltiot:
    print('**********************BOLT-IOT***********************')

    msg = "hello There Mate"

    def send_telegram_message(message):
        """Sends message via Telegram"""
        url = "https://api.telegram.org/" + co.telegram_bot_id + "/sendMessage"
        data = {
            "chat_id": co.telegram_chat_id,
            "text": message
        }
        try:
            response = requests.request(
                "POST",
                url,
                params=data
            )

            print("This is the Telegram URL")
            print(url)
            print("This is the Telegram response")
            print(response.text)
            telegram_data = json.loads(response.text)
            return telegram_data["ok"]
        except Exception as e:
            print("An error occurred in sending the alert message via Telegram")
            print(e)
            return False

    mybolt = Bolt(co.bolt_api_key, co.device_id)

    def get_sensor_value_from_pin(pin):
        """Returns the sensor value. Returns -999 if request fails"""
        try:
            response = Boltiot.mybolt.analogRead(pin)
            data = json.loads(response)
            if data["success"] != 1:
                print("Request not successfull")
                print("This is the response->", data)
                return -999
            sensor_value = int(data["value"])
            return sensor_value
        except Exception as e:
            print("Something went wrong when returning the sensor value")
            print(e)
            return -999

    def start(self):
        while True:
            # Step 1
            sensor_value = Boltiot.get_sensor_value_from_pin("A0")
            print("The current sensor value is:", sensor_value)

            # Step 2
            if sensor_value == -999:
                print("Request was unsuccessfull. Skipping.")
                time.sleep(10)
                continue

            # Step 3
            if sensor_value >= co.threshold:
                print("Sensor value has exceeded threshold")
                message = "Alert! Sensor value has exceeded " + str(co.threshold) + \
                          ". The current value is " + str(sensor_value)
                telegram_status = Boltiot.send_telegram_message(message)
                print("This is the Telegram status:", telegram_status)

            # Step 4
            time.sleep(10)

    if __name__ == "__main__":
        print('Start the process')
        start()
