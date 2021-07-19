from abc import ABC, abstractmethod
from typing import List
from ingredient import Cheese, Dough, Pepperoni, Sauce, Veggies
from ingredient_factory import IngredientFactory

"""This class represents an abstract client wich is the product to implement"""


class Pizza(ABC):
    name: str
    dough: Dough
    sauce: Sauce
    cheese: Cheese
    pepperoni: Pepperoni
    veggies: List[Veggies]

    @abstractmethod
    def prepare(self) -> None:
        raise NotImplementedError

    def bake(self) -> None:
        print('Bake for 25 minutes at 350')

    def cut(self) -> None:
        print('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        print('Place the pizza in official PizzaStore box')

    def __str__(self) -> str:
        pizzaStr = f'{self.name}: \n'
        if(self.dough):
            pizzaStr += f'  Dough: {self.dough} \n'
        if(self.sauce):
            pizzaStr += f'  Sauce: {self.sauce} \n'
        if(self.cheese):
            pizzaStr += f'  Cheese: {self.cheese} \n'
        if(self.pepperoni):
            pizzaStr += f'  Pepperoni: {self.pepperoni} \n'
        if(self.veggies):
            pizzaStr += f'  Veggies: {self.veggies} \n'
        return pizzaStr

""" This classes represents a concrete client wich uses a factory to produce a certain family of objects,
    since the behavior of create objects its encapsulated the client does not know wich family of objects
    was created.
"""

class PepperoniPizza(Pizza):
    def __init__(self, ingredientFactory: IngredientFactory) -> None:
        self.ingredientFactory = ingredientFactory

    def prepare(self) -> None:
        print(f'Preparing a {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
        self.pepperoni = self.ingredientFactory.createPepperoni()
        self.veggies = self.ingredientFactory.createVeggies()
