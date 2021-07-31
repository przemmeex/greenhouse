from abc import ABC, abstractmethod
 
class Thermometer(ABC):
    @abstractmethod
    def get_temp(self):
        pass
