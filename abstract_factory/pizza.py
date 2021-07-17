from abc import ABC, abstractmethod
from ingredient import Cheese, Dough, Pepperoni, Sauce
from ingredient_factory import IngredientFactory


class Pizza(ABC):
    @property
    def dough(self) -> Dough:
        pass

    @property
    def sauce(self) -> Sauce:
        pass

    @property
    def cheese(self) -> Cheese:
        pass

    @property
    def pepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def prepare(self) -> None:
        pass

    def __str__(self) -> str:
        pizzaStr = 'Pizza { \n'
        if(self.dough):
            pizzaStr += '\t Dough { \n \t\t' + str(self.dough) + '\n\t} \n'
        if(self.sauce):
            pizzaStr += '\t Sauce { \n \t\t' + str(self.sauce) + '\n\t} \n'
        if(self.cheese):
            pizzaStr += '\t Cheese { \n \t\t' + str(self.cheese) + '\n\t} \n'
        if(self.pepperoni):
            pizzaStr += '\t Pepperoni { \n \t\t' + \
                str(self.pepperoni) + '\n\t} \n'
        pizzaStr += '}'
        return pizzaStr


class PepperoniPizza(Pizza):
    dough = None
    sauce = None
    cheese = None
    veggies = None
    pepperoni = None

    def __init__(self, ingredientFactory: IngredientFactory) -> None:
        self.ingredientFactory = ingredientFactory

    def prepare(self) -> None:
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
        self.pepperoni = self.ingredientFactory.createPepperoni()
