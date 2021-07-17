import abc


class QuackStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractclassmethod
    def quack(self):
        """Required Method"""


class LoudQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("QUACK! QUACK!")


class GentleQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("quack")


class LightStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractclassmethod
    def lights_on(self):
        """Required method"""

class OnForTenSecondsStrategy(LightStrategyAbstract):
    def lights_on(self):
        print("Luces en 10 segundos")