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