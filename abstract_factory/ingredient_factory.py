from abc import ABC, abstractmethod
from typing import List
from ingredient import *


class IngredientFactory(ABC):
    @abstractmethod
    def createDough(self) -> Dough:
        pass

    @abstractmethod
    def createCheese(self) -> Cheese:
        pass

    @abstractmethod
    def createClams(self) -> Clams:
        pass

    @abstractmethod
    def createSauce(self) -> Sauce:
        pass

    @abstractmethod
    def createPepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def createVeggies(self) -> List[Veggies]:
        pass


class NYIngredientFactory(IngredientFactory):
    def createDough(self) -> Dough:
        return ThinCrustDough()

    def createCheese(self) -> Cheese:
        return ReggianoCheese()

    def createClams(self) -> Clams:
        return FreshClams()

    def createSauce(self) -> Sauce:
        return MarianaSauce()

    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def createVeggies(self) -> Veggies:
        return [Garlic(), Onion(), Mushroom(), RedPapper()]


class ChicagoIngredientFactory(IngredientFactory):
    def createDough(self) -> Dough:
        return ThickCrustDough()

    def createCheese(self) -> Cheese:
        return MozzarellaCheese()

    def createClams(self) -> Clams:
        return FrozenClams()

    def createSauce(self) -> Sauce:
        return PlumTomatoSauce()

    def createPepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def createVeggies(self) -> List[Veggies]:
        return [Garlic(), Onion(), Mushroom(), RedPapper()]
