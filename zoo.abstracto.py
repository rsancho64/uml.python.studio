# code from https://blog.teclado.com/python-abc-abstract-base-classes/

from abc import ABC, abstractmethod  # a builtin module


class Animal(ABC):  # ABC: Abstract base class

    @property
    def food_eaten(self):
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"You can't feed this animal with {food}.")

    # @property
    @abstractmethod
    def diet(self):
        """ok food list"""
        pass

    @abstractmethod
    def feed(self):
        pass  # print("ñam")

    @abstractmethod
    def do(self, action):
        pass


class Lion(Animal):

    @property
    def diet(self):
        return ["antelope", "cheetah", "buffaloe"]

    def do(self, action, time):  # It's still mandatory to implement action. "time" is our other parameter
        print(f"{action} a lion! At {time}")

    def feed(self, time):
        print(f"Feeding a lion with {self._food} meat! At {time}")

    # def give_food(self):
    #     print("Feeding a lion with raw meat!")


class Panda(Animal):

    def do(self, action, time):
        print(f"{action} a panda! At {time}")

    def feed(self, time):
        print(f"Feeding a snake with {self._food} meat! At {time}")

    # def wrong_name(self):
    #     print("Feeding a panda with some tasty bamboo!")


class Snake(Animal):

    @property
    def diet(self):
        return ["frog", "rabbit"]

    def do(self, action, time):
        print(f"{action} a snake! At {time}")

    def feed(self, time):
        print(f"Feeding a snake with {self._food} meat! At {time}")

    # def feed_snake(self):
    #     print("Feeding a snake with mice!")


if __name__ == "__main__":

    # ZOO1
    # leo = Lion()
    # po = Panda()
    # sam = Snake()

    # leo.give_food()
    # po.wrong_name()
    # sam.feed_snake()

    # Put all the animals in a list:
    # zoo = [leo, po, sam]  # Could be many more animals there!

    # Loop through the animals and feed them
    # for animal in zoo:
    #     # But what do we put here now?
    #     # Is it animal.give_food() or animal.feed_animal(), hmm?
    #     animal.feed()  # This will throw an AttributeError!

    # zoo2 = [Lion(), Panda(), Snake()]

    # for animal in zoo2:
    #     animal.do(action="feeding", time="10:10 PM")

    # ZOO3

    leo = Lion()
    leo.food_eaten = "antelope"
    leo.feed("10:10 AM")
    leo.do("pee", "10:10 AM")

    adam = Snake()
    adam.food_eaten = "frog"
    adam.feed("10:10 AM")

    # leo2 = Lion()
    # # leo2.food_eaten = "cauliflower"
    # leo2.feed("10:10 AM")

    # leo3 = Lion()
    # leo3.food_eaten = "carrot"
    # leo3.feed("10:10 AM")
