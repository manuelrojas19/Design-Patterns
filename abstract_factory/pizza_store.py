
from abc import ABC, abstractmethod
from ingredient_factory import ChicagoIngredientFactory, NYIngredientFactory
from pizza import PepperoniPizza, Pizza


class PizzaStore(ABC):
    @abstractmethod
    def createPizza(self, item: str) -> Pizza:
        pass

    def orderPizza(self, type: str) -> Pizza:
        pizza = self.createPizza(type)
        pizza.prepare()
        return pizza


class NYPizzaStore(PizzaStore):
    def __init__(self) -> None:
        self.ingredientFactory = NYIngredientFactory()

    def createPizza(self, item: str) -> Pizza:
        if (item == 'pepperoni'):
            pizza = PepperoniPizza(self.ingredientFactory)

        """ TODO: add more pizzas """

        return pizza


class ChicagoPizzaStore(PizzaStore):
    def __init__(self) -> None:
        self.ingredientFactory = ChicagoIngredientFactory()

    def createPizza(self, item: str) -> Pizza:
        if (item == 'pepperoni'):
            pizza = PepperoniPizza(self.ingredientFactory)

        """ TODO: add more pizzas """

        return pizza
