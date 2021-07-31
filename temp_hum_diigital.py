import RPi.GPIO as GPIO
import dht11
from abstracts import Thermometer, Higrometer
from logger import Logger
from time import sleep

logger = Logger()

class DigitalMultimeter(Thermometer, Higrometer):
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    def __init__(self, used_pin):
        self.instance = dht11.DHT11(pin=used_pin)

    def get_temp(self):
        for _ in range(15):
            result = self.instance.read()
            if result.is_valid():
                return "%-3.1f" % result.temperature
            sleep(1)
        return

    def get_huidity(self):
        for _ in range(15):
            result = self.instance.read()
            if result.is_valid():
                return "%-3.0f" % result.humidity
            sleep(1)
        return

    def get_temp_and_huidity(self):
        for _ in range(35):
            result = self.instance.read()
            if result.is_valid():
                return "%-3.1f" % result.temperature, "%-3.1f" % result.humidity
            sleep(0.2)
        logger.error("reading digital temp and/or humidity failed")
        return None, None
        
    @staticmethod
    def cleanup():
        GPIO.cleanup()


