from abc import ABC, abstractmethod
from ingredient_factory import ChicagoIngredientFactory, IngredientFactory, NYIngredientFactory
from pizza import PepperoniPizza, Pizza

""" This class Represent a factory method because we want to be able to create a product that
    varies by region, this class provides an abstract interface for creating one product. """


class PizzaStore(ABC):
    ingredientFactory: IngredientFactory

    def orderPizza(self, type: str) -> Pizza:
        pizza = self.createPizza(type)
        print(f'Making a {pizza.name}')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def createPizza(self, item: str) -> Pizza:
        raise NotImplementedError


""" The subclases decides wich concrete factory use to produce objects """


class NYPizzaStore(PizzaStore):
    def __init__(self) -> None:
        self.ingredientFactory = NYIngredientFactory()

    def createPizza(self, item: str) -> Pizza:
        if (item == 'pepperoni'):
            pizza = PepperoniPizza(self.ingredientFactory)
            pizza.name = 'New York Style Cheese Pizza'

        """ TODO: add more pizzas types """

        return pizza


class ChicagoPizzaStore(PizzaStore):
    def __init__(self) -> None:
        self.ingredientFactory = ChicagoIngredientFactory()

    def createPizza(self, item: str) -> Pizza:
        if (item == 'pepperoni'):
            pizza = PepperoniPizza(self.ingredientFactory)
            pizza.name = 'Chicago Style Cheese Pizza'

        """ TODO: add more pizzas types """

        return pizza
