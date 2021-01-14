from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, par):
        self.par = par

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Пальто с расходом ткани: {round(self.par / 6.5 + 0.5, 2)} метра'


class Suit(Clothes):
    @property
    def consumption(self):
        return f'Костюм с расходом ткани: {round(2 * self.par + 0.3, 2)} метра'


suit_one = Suit(2)
coat_one = Coat(10)
print(suit_one.consumption)
print(coat_one.consumption)
