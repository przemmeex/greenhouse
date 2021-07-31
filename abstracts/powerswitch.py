from abc import ABC, abstractmethod
 
class PowerSwitch(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
    @abstractmethod
    def is_on(self):
        pass
