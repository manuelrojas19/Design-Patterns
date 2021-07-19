""" The Strategy Pattern defines a family of algorithms, encapsulates each one, and makes then interchangable.
    Strategy lets the algorithm vary independently from clients that use it.
"""

from behavior import FlyWithRockets
from duck import Duck, MallardDuck, ModelDuck


def main():
    mallardDuck: Duck
    mallardDuck = MallardDuck()
    mallardDuck.display()
    mallardDuck.performFly()
    mallardDuck.performQuack()

    modelDuck: Duck
    modelDuck = ModelDuck()
    modelDuck.display()
    modelDuck.performFly()
    """This behaviors or algorithms can be change it dinamically"""
    modelDuck.flyBehavior = FlyWithRockets()
    modelDuck.performFly()
    modelDuck.performQuack()


if __name__ == '__main__':
    main()
