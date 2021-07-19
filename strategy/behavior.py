from abc import ABC, abstractmethod

""" This class is an abstract supertype wich could be an abstract class or a interface 
    wich the subclasses has to implement in order to create a family of algorithms a client
    can use this interface to refer to an specific type of algorithm.
"""


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self) -> None:
        raise NotImplementedError


""" This classes represents the concrete implementations of the super class with this approach
    we are allow to assing the concrete implementation of the objects at runtime.

    We can add new algorithms without modifying any of the existing algorithms families or touching
    the classes with use this algorithm.s
"""


class Quack(QuackBehavior):
    def quack(self) -> None:
        print('Quack')


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print('Squeak')


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print('<< Mute >>')


""" Classes wich represents another family of algorithms"""


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self) -> None:
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print('I am flying!')


class DoesNotFly(FlyBehavior):
    def fly(self) -> None:
        print('I cannot fly :(')

class FlyWithRockets(FlyBehavior):
    def fly(self) -> None:
        print('I am flying with rockets!')
