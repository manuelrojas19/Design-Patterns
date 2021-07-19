""" The Abstract Factory Pattern provides an interface for creating families of related or depende 
    objects without specifying their concrete classes. By writting code that uses this interface,
    we decoupled our code from the actual factory that creates the products. That allow us to
    implement a variety of factories that produce products meant for different contexts such as differents
    regions, operating systems, or different look and fell.

    Since our code is decoupled from the actual objects, we can substitute different factories to get different
    behaviors.
"""

from pizza import Pizza
from pizza_store import ChicagoPizzaStore, NYPizzaStore, PizzaStore

def main():
    store: PizzaStore
    pizza: Pizza

    store = NYPizzaStore()
    pizza = store.orderPizza('pepperoni')
    print(pizza)

    store = ChicagoPizzaStore()
    pizza = store.orderPizza('pepperoni')
    print(pizza)


if __name__ == "__main__":
    main()
