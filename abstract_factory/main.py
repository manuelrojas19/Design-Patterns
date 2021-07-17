from pizza import Pizza
from pizza_store import ChicagoPizzaStore, NYPizzaStore, PizzaStore


if __name__ == "__main__":
    store: PizzaStore
    pizza: Pizza

    store = NYPizzaStore()
    pizza = store.orderPizza('pepperoni')
    print(pizza)

    store = ChicagoPizzaStore()
    pizza = store.orderPizza('pepperoni')
    print(pizza)
