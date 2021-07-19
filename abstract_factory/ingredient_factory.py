from abc import ABC, abstractmethod
from typing import List
from ingredient import *

""" This class represents an Abstract Factory wich provides an interface wich consists of a set of 
    methods for producing a family of concrete objects this interfaces must be implemented
    by all the concrete class, the concrete factories. 
"""


class IngredientFactory(ABC):
    @abstractmethod
    def createDough(self) -> Dough:
        raise NotImplementedError

    @abstractmethod
    def createCheese(self) -> Cheese:
        raise NotImplementedError

    @abstractmethod
    def createClams(self) -> Clams:
        raise NotImplementedError

    @abstractmethod
    def createSauce(self) -> Sauce:
        raise NotImplementedError

    @abstractmethod
    def createPepperoni(self) -> Pepperoni:
        raise NotImplementedError

    @abstractmethod
    def createVeggies(self) -> List[Veggies]:
        raise NotImplementedError


""" This classes are the concrete factories wich implement the different product families. To create
    a product a client uses one of these factories so it never has to instantiate a concrete object.
    The job of the concrete factories is to create the right family of objects.
"""


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
