import w1thermsensor
from abstracts import Thermometer
from logger import Logger

logger = Logger()

class AnalogThermometer(Thermometer):

    def get_temp(self): 
        try:
            sensor = w1thermsensor.W1ThermSensor()
            return f"{sensor.get_temperature():.1f}"
        except Exception as e1:
            logger.error(f"Analog temp reading went badly, fixed value 25 returned message :{e1}")
            return 25
        
