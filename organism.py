class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print('eatiing')

    def sleep(self):
        print('sleeping')

class Dog(Animal):
    def bark(self):
        print('barking')