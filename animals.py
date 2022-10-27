class Animal:
    alive=True
    def eat(self):
        print('eatiing')
    def sleep(self):
        print('sleeping')

class Rabbit(Animal):
    def jump(self):
        print('jumping')
class Fish(Animal):
    def swim(self):
        print('swimming')
class Bird(Animal):
    def fly(self):
        print('flying')