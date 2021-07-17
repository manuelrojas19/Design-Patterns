from abc import ABC, abstractmethod
from ingredient_factory import IngredientFactory


class Pizza(ABC):
    @abstractmethod
    def prepare(self) -> None:
        pass

    def __str__(self) -> str:
        """ TODO: format string and add validations for the properties """
        string = 'Pizza {\n\t Dough: ' + str(self.dough) + '\n' + \
            '\t Sacue: ' + str(self.sauce) + '\n' '\t cheese: ' + \
            str(self.cheese) + '\n' + '\t pepperonie: ' + \
            str(self.pepperoni) + '\n}'
        return string


class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory: IngredientFactory) -> None:
        self.ingredientFactory = ingredientFactory

    def prepare(self) -> None:
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
        self.pepperoni = self.ingredientFactory.createPepperoni()


""" TODO: add more pizzas classes"""
