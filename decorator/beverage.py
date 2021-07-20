from abc import ABC, abstractmethod


class Beverage(ABC):
    description: str

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError

    def getDescription(self) -> str:
        return self.description


class Espresso(Beverage):
    def __init__(self) -> None:
        self.description = 'Espresso'

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self) -> None:
        self.description = 'House Blend Coffe'

    def cost(self) -> float:
        return .89
