import RPi.GPIO as GPIO
import dht11
from abstracts import Thermometer, Higrometer
from logger import Logger
from time import sleep

logger = Logger()

class DigitalMultimeter(Thermometer, Higrometer):
    """Manage digital multimeter

    :param Thermometer: device to measure temperature
    :type Thermometer
    :param Higrometer: device to measure humidity
    :type Higrometer
    """
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    def __init__(self, used_pin):
        """initilaizator

        :param used_pin: Pin on RPi used for gatering data from meter
        :type used_pin: int
        """
        self.instance = dht11.DHT11(pin=used_pin)

    def get_temp(self):
        """Get reading

        :return: temperature reading
        :rtype: string
        """
        for _ in range(15):
            result = self.instance.read()
            if result.is_valid():
                return "%-3.1f" % result.temperature
            sleep(1)
        return

    def get_huidity(self):
        """Get humidity in %

        :return: humidity reading
        :rtype: string
        """
        for _ in range(15):
            result = self.instance.read()
            if result.is_valid():
                return "%-3.0f" % result.humidity
            sleep(1)
        return

    def get_temp_and_huidity(self):
        """Get temperature and humidity

        :return: temperature and humidity
        :rtype: tuple
        """
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


