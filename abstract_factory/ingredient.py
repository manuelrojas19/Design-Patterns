from abc import ABC, abstractmethod


class Dough(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class ThickCrustDough(Dough):
    def __str__(self) -> str:
        return 'Thick Crust Dough'


class ThinCrustDough(Dough):
    def __str__(self) -> str:
        return 'Thin Crust Dough'


class Cheese(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class MozzarellaCheese(Cheese):
    def __str__(self) -> str:
        return 'Mozzarella Cheese'


class ReggianoCheese(Cheese):
    def __str__(self) -> str:
        return 'Regiano Cheese'


class Clams(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class FrozenClams(Clams):
    def __str__(self) -> str:
        return 'Frozen Clams'


class FreshClams(Clams):
    def __str__(self) -> str:
        return 'Fresh Clams'


class Sauce(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class PlumTomatoSauce(Sauce):
    def __str__(self) -> str:
        return 'Plum Tomato Sauce'


class MarianaSauce(Sauce):
    def __str__(self) -> str:
        return 'Mariana Sauce'


class Pepperoni(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class SlicedPepperoni(Pepperoni):
    def __str__(self) -> str:
        return 'SlicedPepperoni'


class Veggies(ABC):
    @abstractmethod
    def __str__(self) -> str:
        pass


class Garlic(Veggies):
    def __str__(self) -> str:
        return 'Garlic'


class Onion(Veggies):
    def __str__(self) -> str:
        return 'Onion'


class Mushroom(Veggies):
    def __str__(self) -> str:
        return 'Mushroom'


class RedPapper(Veggies):
    def __str__(self) -> str:
        return 'RedPapper'
