from abc import ABC, abstractmethod
from subject import Subject

""" This is the Observer interface wich has to be implement by all of the Observers """


class Observer(ABC):

    """ This method contains the state values the Observers get from the subject"""
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float) -> None:
        raise NotImplementedError


class DisplayElement(ABC):
    @abstractmethod
    def display(self) -> None:
        raise NotImplementedError


class CurrentConditionDisplay(Observer, DisplayElement):
    def __init__(self, wheaterData: Subject) -> None:
        self.__temperature = None
        self.__humidity = None
        self.__wheaterData = wheaterData
        self.__wheaterData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float) -> None:
        self.__temperature = temp
        self.__humidity = humidity
        self.display()

    def display(self) -> None:
        print(
            f'Current conditions: {self.__temperature} F degrees and {self.__humidity}% humidity')
