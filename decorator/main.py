""" The Decorator Pattern attaches additional responsibilites to an object dinamically. Decorators
    provide a flexible alternative to subclassing for extending functionallity.
"""

from condiment import Mocha
from beverage import Espresso


def main():
    beverage = Espresso()
    print(f'{beverage.getDescription()} ${beverage.cost()}')

    beverage = Mocha(beverage)
    print(f'{beverage.getDescription()} ${beverage.cost()}')

    beverage = Mocha(beverage)
    print(f'{beverage.getDescription()} ${beverage.cost()}')


if __name__ == '__main__':
    main()
