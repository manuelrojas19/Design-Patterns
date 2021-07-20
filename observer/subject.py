from abc import ABC, abstractmethod

""" This is the Subject interface wich has to be implemented by any object who needs has got subcribers"""


class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def removeObserver(self, observer) -> None:
        raise NotImplementedError

    @abstractmethod
    def notifyObserver(self) -> None:
        raise NotImplementedError


""" This class implements the subject interface """


class WheaterData(Subject):
    def __init__(self) -> None:
        """ This list hols all of the references to the subscribers """
        self.__observers = []
        self.__temperature = None
        self.__humidity = None
        self.__pressure = None

    def registerObserver(self, observer) -> None:
        self.__observers.append(observer)

    def removeObserver(self, observer) -> None:
        self.__observers.remove(observer)

    """ This method is invoqued when the measurements change, since we know that all of the
        observers implements a method calls observer we can use it in order to notify and update
        his data.
    """
    def notifyObserver(self) -> None:
        for observer in self.__observers:
            observer.update(self.__temperature,
                            self.__humidity, self.__pressure)

    def mesurementsChanged(self) -> None:
        self.notifyObserver()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.__temperature = temperature
        self.__humidity = humidity
        self.__pressure = pressure
        self.mesurementsChanged()
