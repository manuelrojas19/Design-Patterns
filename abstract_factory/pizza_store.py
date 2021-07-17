from abc import ABC, abstractmethod
from ingredient_factory import ChicagoIngredientFactory, NYIngredientFactory
from pizza import PepperoniPizza, Pizza


class PizzaStore(ABC):
    @abstractmethod
    def createPizza(self, item: str) -> Pizza:
        pass

    def orderPizza(self, type: str) -> Pizza:
        pizza = self.createPizza(type)

        print('------------------------------------------')
        print(f'Making a {pizza.name}')
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


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
