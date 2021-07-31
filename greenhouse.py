from helpers import is_day, read_config
from logger import Logger
from sonoff_api_driver import SonoffConnection
from temp_analog import AnalogThermometer
from temp_hum_diigital import DigitalMultimeter
from time import sleep

logger = Logger()
dev1 = SonoffConnection("ID_SERIAL1", "IP1")
dev2 = SonoffConnection("ID_SERIAL2", "IP@")
atherm1 = AnalogThermometer()
mmeter = DigitalMultimeter(17)

def main_loop():
    while True:
        conf = read_config()
        digital_temp, digital_humidity = mmeter.get_temp_and_huidity()
        analog_temp = atherm1.get_temp()
        digital_temp = digital_temp if digital_temp else analog_temp
        is_now_day = is_day()

        if is_now_day:
            dev1.turn_on()
        else:
            dev1.turn_off()

        avg_temp = (float(digital_temp) + float(analog_temp)) / 2

        if avg_temp > conf["fanTurningTreshold"]:
            dev2.turn_on()
        elif avg_temp <= conf["fanTurnOffTreshold"]:
            dev2.turn_off()
        logger.measurements(f"{analog_temp}--{digital_temp}--{digital_humidity}--{is_now_day}--{dev2.is_on()}")
        sleep(conf["redingStepTime"])

if __name__ == ("__main__"):
    main_loop()

