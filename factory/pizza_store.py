from abc import ABC, abstractmethod
from pizza import ChicagoStyleCheesePizza, NYStyleCheesePizza, Pizza

""" This class has the function of creator, a creator is a class wich contains the implementation
    for all of the methods to manipulate the objects, except for the factory mehtod
"""


class PizzaStore(ABC):
    def orderPizza(self, type: str) -> Pizza:
        pizza = self.createPiza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    """ This is the abstract factory method which has to be implemented by the creator subclasses
        Since this method is abstract the creator never really knows wich concrete object was created
     """
    @abstractmethod
    def createPiza(self, type: str) -> Pizza:
        raise NotImplementedError


""" This classes are the Concrete Creator Classes which implements the factory method"""


class NYPizzaStore(PizzaStore):
    def createPiza(self, type: str) -> Pizza:
        """ Concrete creators are responsible for creating one or more concrete objects.
            They are the only classes wich knows how to create a certain product because 
            this classes encapsulate that functionality with the factory abstract method
        """
        if (type == 'cheese'):
            return NYStyleCheesePizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):
    def createPiza(self, type: str) -> Pizza:
        if (type == 'cheese'):
            return ChicagoStyleCheesePizza()
        else:
            return None
