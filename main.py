# *args (tuple) =================
import organism
import animals

# def add(*data):
#     sum=0
#     data=list(data)
#     data[0]=0
#     for i in data:
#         sum+=i
#     return sum
#
# print(add(1,2,3,4))

# **kwargs (dictionary) =================

# def hello(**data):
#     print('hello',end=" ")
#     for key,value in data.items():
#         print(value,end=" ")
# hello(title='mr',first='jan',middle='marcin',last='mlody g')

# string.format() =================
#
# animal='cow'
# item='moon'
# print("the {} jumped over {}".format(animal,item))
# print("the {1} jumped over {0}".format(animal,item))
# print("the {item1} jumped over {item2}".format(item1='cow',item2='moon'))
#
# text="the {} jumped over {}"
# print(text.format(animal,item))
#
# name='jan'
# print('hello, my name is {}.wow'.format(name))
# print('hello, my name is {:10}.wow'.format(name)) #padding right
# print('hello, my name is {:>10}.wow'.format(name)) #padding left
# print('hello, my name is {:^10}.wow'.format(name)) #center
#
# number=3.14159
# bigNumber=1000
# print('the number pi is {:.2f}'.format(number))
# print('the number pi is {:.3f}'.format(number)) #also rounding
# print('the number pi is {:,}'.format(bigNumber))
# print('the number pi is {:b}'.format(bigNumber))


# random =================
#
# import random
# x=random.randint(1,6)
# y=random.random()
# myList=['rock','paper','scissors']
# z=random.choice(myList)
# cards=[1,2,3,4,5,6,7,8,9,'j','q']
# random.shuffle(cards)
# print(x,y,z,cards)

# exception =================
#
# try:
#     numerator=int(input('enter a number to divide: '))
#     denominator=int(input('enter a number to devide by: '))
#     result=numerator/denominator
# except ZeroDivisionError as e:
#     print('you cant divide by zero')
# except ValueError as e:
#     print('enter only numbers')
# else:
#     print(result)
# finally:
#     print('this will always execute')

# file detection =================

# import os
#
# path='/Users/janek/PycharmProjects/cw1/test.txt' #z backslashami uzywamy zamiast "\", "\\"
# if os.path.exists(path):
#     print('location exists')
#     if os.path.isfile(path):
#         print('this is a file')
#     elif os.path.isdir(path):
#         print('this is a directory')
# else:
#     print('doesnt exist')

# reading file =================

# try:
#     with open('test.txt') as file:
#       print(file.read())
#     print(file.closed)
# except FileNotFoundError:
#     print('file not found')

# write file =================

# text='hejjjjj\n essa \n'
# with open('test2.txt','w') as file:
#     file.write(text)
#
# text='\n no hej'
# with open('test2.txt','a') as file:
#     file.write(text)

# copying files =================

# .copyfile(), .copy(), .copy2()
# import shutil
#
# shutil.copyfile('test.txt','copy.txt')

# move files =================

# import os
#
# source='test.txt'
# destination="/Users/janek/test.txt"
#
# try:
#     if os.path.exists(destination):
#         print('there is already a file!')
#     else:
#         os.replace(source,destination)
#         print(source+' was moved')
# except FileNotFoundError as e:
#     print(e)

# delete files =================

# import os
# try:
#     os.remove('test.txt')
# except FileNotFoundError:
#     print('that file wa snot found')

# modules =================

# import msgs
# msgs.hello()

# OOP =================

# from Car import Car
# car1=Car('bmw','i3','2021','black')
# car2=Car('ford','mustang',2022,'red')
# car2.drive()
# car1.stop()

# OOP-inheritence =================

# from animals import *
# rabbit=animals.Rabbit()
# bird=animals.Bird()
# fish=animals.Fish()
# print(rabbit.alive)
# fish.eat()
# fish.swim()

# OOP-multilevel inharitance  funkcja super w konstruktorze:   super().__init__(params) =================

# from organism import *
#
# dog=organism.Dog()
# dog.eat()
# dog.bark()

# OOP- abstract classes =================
#
# from abc import ABC,abstractmethod
# class Vehicle(ABC):
#     @abstractmethod
#     def go(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
# class Car(Vehicle):
#     def go(self):
#         print('drive car')
#     def stop(self):
#         print('stopped')
# class Motorcycle(Vehicle):
#     def go(self):
#         print('drive motorcycle')
#     def stop(self):
#         print('stopped')
# # vehicle=Vehicle()
# car=Car()
# motorcycle=Motorcycle()
# motorcycle.go()

# walrus operator Python 3.8> =================

# print(happy:=True)
# foods=[]
#
# #without :=
# while True:
#     food=input('food: ')
#     if food=='quit':break
#     foods.append(food)
# #with :=
# while food:=input('food: ')!='quit':
#     foods.append(food)

# lambda fn =================

# double=lambda x,y:x*y
# print(double(3,4))

# sorting =================

# students = ['wow', 'abc', 'bde', 'rgrbv']
# students_tuple = ('wow', 'abc', 'bde', 'rgrbv')
#
# students.sort()
# for i in students:
#     print(i)
#
# sorted_students = sorted(students_tuple, reverse=True)
#
# for i in sorted_students:
#     print(i)

# students_II = [('xyz', "F", 50), ('abc', "A", 20), ('dfr', "D", 73), ('wow', "B", 21)]
# # students_II.sort() #sortowanie po nazwisku
# students_II.sort(key=lambda grades:grades[1])#sortowanie w indexie 1 (ocena)    ,reverse=True
# print(students_II)
# sorted_s=sorted(students_II,key=lambda ages:ages[2])
# print(sorted_s)


# map() =================

# store = [('shirt', 12), ('jacket', 43), ('dress', 30), ('pants', 20), ('bucket hat', 93)]
# to_euro=lambda data:(data[0],round(data[1]*0.82,2))
# store_in_euros=list(map(to_euro,store))
# print(store_in_euros)

# filter() =================

# store = [('shirt', 12), ('jacket', 12), ('dress', 30), ('shirt', 20), ('bucket hat', 93)]
# price=lambda data:data[1]>=20
#
# store_prices=list(filter(price,store))
# print(store_prices)

# reduce() =================

# import functools
#
# letters=['h','e','l','l','o']
# word=functools.reduce(lambda x,y:x+y,letters)
# print(word)

# list cmprehension =================

# # squares=[]
# # for i in range(1,11): squares.append(i*i)
# # print(squares)
#
#
# squares=[i*i for i in range(1,11)]
# print(squares)
#
# # students=[100,90,80,70,60,50,40,30,0]
# # passed_st=list(filter(lambda x:x>=60,students))
# # print(passed_st)
#
# students=[100,90,80,70,60,50,40,30,0]
# passed_st=[i for i in students if i>=60]
# print(passed_st)

# dictionary comprehension =================

# # dictionary={key:expression for (key,val) in iterable}
# cities = {'new york': 100, 'boston': 50, 'london': 23}
# cities_in_C = {key: ((val - 32) * (5 / 9)) for (key, val) in cities.items()}
# desc_cities = {key: ('warm' if val >= 40 else 'cold') for (key, val) in cities.items()}
# print(cities_in_C, desc_cities)
#
# cities_weather = {'new york': 'sunny', 'boston': 'cloudy', 'london': 'sunny'}
# sunny_weather = {key: val for (key, val) in cities_weather.items() if val == 'sunny'}
# print(sunny_weather)

# zip(*iterables) =================

# usernames=['dude','bro','mister']
# passwords=('p@ssword','abc123','guest')
#
# users=dict(zip(usernames,passwords))
#
# for key,val in users.items():print(key,val)

# multithreading =================
#
# import threading
# import time
#
# print(threading.active_count())
# def eat():
#     time.sleep(3)
#     print('you eat breakfast')
#
# def drink():
#     time.sleep(5)
#     print('you drink beer')
#
# x=threading.Thread(target=eat,args=())
# x.start()
# y=threading.Thread(target=drink,args=())
# y.start()
#
# x.join()
# y.join()
# print(time.perf_counter())
## eat()
## drink()

#multiprocessing =================

# from multiprocessing import Process,cpu_count
# import time
# def counter(num):
#     count=0
#     while count<num:count+=1
#
# def main():
#     a = Process(target=counter, args=(500000000,))
#     b=Process(target=counter,args=(500000000,))
#
#     a.start()
#     b.start()
#     a.join()
#     b.join()
#     print('finished in: ',time.perf_counter()," seconds")
#
# if __name__=='__main__':
#     main()