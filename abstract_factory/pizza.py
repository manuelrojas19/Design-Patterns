from abc import ABC, abstractmethod
from ingredient import Cheese, Dough, Pepperoni, Sauce
from ingredient_factory import IngredientFactory


class Pizza(ABC):
    @property
    def name(self):
        return f'{self.name}'

    @name.setter
    def name(self, name):
        self.name = name

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
        return pizzaStr


class PepperoniPizza(Pizza):
    name = None
    dough = None
    sauce = None
    cheese = None
    veggies = None
    pepperoni = None

    def __init__(self, ingredientFactory: IngredientFactory) -> None:
        self.ingredientFactory = ingredientFactory

    def prepare(self) -> None:
        print(f'Preparing a {self.name}')
        self.dough = self.ingredientFactory.createDough()
        self.sauce = self.ingredientFactory.createSauce()
        self.cheese = self.ingredientFactory.createCheese()
        self.veggies = self.ingredientFactory.createVeggies()
        self.pepperoni = self.ingredientFactory.createPepperoni()
