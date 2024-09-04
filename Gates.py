from abc import ABC, abstractmethod

class Gates(ABC):

    @abstractmethod
    def readFile(self):
        pass