from abc import ABC, abstractmethod
 
class Higrometer(ABC):
    @abstractmethod
    def get_huidity(self):
        pass
