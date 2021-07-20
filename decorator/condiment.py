from abc import ABC, abstractmethod
from beverage import Beverage

class CondimentDecorator(Beverage, ABC):
    @abstractmethod
    def getDescription(self) -> str:
        raise NotImplementedError

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ', mocha'

    def cost(self) -> float:
        return .20 + self.beverage.cost()
