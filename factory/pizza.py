from abc import ABC
from typing import List

""" This class represent the interfaces that all concrete objects must implement in this way, the classes
    which use the concrete objects can refer to this interface instead the concrete class.
"""


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    toppings: List[str]

    def prepare(self) -> None:
        print(f'Preparing: {self.name}')
        print('Tossing dough')
        print('Adding sauce')
        print('Adding toppings: ')
        for topping in self.toppings:
            print(f'  {topping}')

    def bake(self) -> None:
        print('Bake for 25 min at 350')

    def cut(self) -> None:
        print('Cutting the pizza into diagonal slices')

    def box(self) -> None:
        print('Place pizza in official PizzaStore box')

    def __str__(self) -> str:
        pizzaStr = f'{self.name}: \n'
        if(self.dough):
            pizzaStr += f'  Dough: {self.dough} \n'
        if(self.sauce):
            pizzaStr += f'  Sauce: {self.sauce} \n'
        if(self.toppings):
            pizzaStr += f'  Toppings: {self.toppings} \n'
        return pizzaStr


""" This are the differents concrete class wich implements the same interface """


class NYStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self.name = 'NY Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Mariana Sauce'
        self.toppings = ['Greated Regiano Cheese']


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self) -> None:
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Thick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings = ['Shredded Mozzarella Cheese']

    """ Overrided method """

    def cut(self) -> None:
        print('Cutting the pizza into square slices')
