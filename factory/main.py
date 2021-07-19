""" The Factory Pattern defines an interface for creating an object, but lets subclasses decide 
    wich class to instantiate. Factory Method lets a class defer instantiation to subclasses

    The Factory Pattern is usefull if we have got one concrete creator because we are decoupling
    the implementation of the product from its use. If we add additional products or change a pro
    ducts implementation, it wont affect our creator because this is not tighly coupled to any
    concrete product
"""

from pizza import Pizza
from pizza_store import ChicagoPizzaStore, NYPizzaStore, PizzaStore


def main():
    pizzaStore: PizzaStore
    pizza: Pizza

    pizzaStore = NYPizzaStore()
    pizza = pizzaStore.orderPizza('cheese')
    print(pizza)

    pizzaStore = ChicagoPizzaStore()
    pizza = pizzaStore.orderPizza('cheese')
    print(pizza)


if __name__ == '__main__':
    main()
