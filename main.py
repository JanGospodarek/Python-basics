#*args (tuple) =================

# def add(*data):
#     sum=0
#     data=list(data)
#     data[0]=0
#     for i in data:
#         sum+=i
#     return sum
#
# print(add(1,2,3,4))

#**kwargs (dictionary) =================

# def hello(**data):
#     print('hello',end=" ")
#     for key,value in data.items():
#         print(value,end=" ")
# hello(title='mr',first='jan',middle='marcin',last='mlody g')

#string.format() =================
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

#exception =================
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

