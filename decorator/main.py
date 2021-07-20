""" The Decorator Pattern attaches additional responsibilites to an object dinamically. Decorators
    provide a flexible alternative to subclassing for extending functionallity.
"""

from condiment import Mocha
from beverage import Espresso


def main():
    beverage = Espresso()
    print(f'{beverage.getDescription()} ${beverage.cost()}')

    beverage2 = Mocha(beverage)
    print(f'{beverage2.getDescription()} ${beverage2.cost()}')

    beverage3 = Mocha(beverage2)
    print(f'{beverage3.getDescription()} ${beverage3.cost()}')


if __name__ == '__main__':
    main()
