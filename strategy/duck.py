from abc import ABC, abstractmethod
from behavior import DoesNotFly, FlyBehavior, FlyWithWings, Quack, QuackBehavior


""" This class represents the abstract client wich makes use of an encapsulated family of algorithms,
    since this class is an abstract class it does not know wich concrete algorithm was use.
"""


class Duck(ABC):
    """ Each type of this object has a reference to something that implements a certain interface. 
        This approach favor composition over inheritance
    """
    quackBehavior: QuackBehavior
    flyBehavior: FlyBehavior

    def performQuack(self) -> None:
        """ Rather than handling the behavior or algorithm itselft, the object delegates this to the objects
            wich is referenced.
        """
        self.quackBehavior.quack()

    def performFly(self) -> None:
        self.flyBehavior.fly()

    @abstractmethod
    def display(self) -> None:
        raise NotImplemented


"""
    This classes represents the concrete clients wich has the knowledge about wich concrete algorithm is use.
"""


class MallardDuck(Duck):
    def __init__(self) -> None:
        self.quackBehavior = Quack()
        self.flyBehavior = FlyWithWings()

    def display(self) -> None:
        print('I am a real Mallard Duck')


class ModelDuck(Duck):
    def __init__(self) -> None:
        self.quackBehavior = Quack()
        self.flyBehavior = DoesNotFly()

    def display(self) -> None:
        print('I am a model duck')