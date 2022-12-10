import math
# data

userName = 'rocking_head' #string
live = False #Boolean
address = 'California' #String
age = 10 #number int
life = 80.80 #number float

users = ['rocking_head', 'jumping_monkey', 'crying_soul', 'dead_pirate']
#list

# Dictionary / object / json
neha = {
        "phone": 89892566,
        "address": 'Siliguri',
        "married": True
        }

sutapa = {
        #key : value
        "phone": 45659878,
        "address": 'NCB',
        "skills": ['Html', 'CSS', 'JS', 'Linux']
        }

sutapa["phone"]=56569888
sutapa["married"]=False

# print(sutapa)

cars = ['maruti', 'tata', 'BMW', 'Bugati', 'Posche']

# print(cars)

# for i in cars:
#     print(i.upper())

name = input("Enter name please : ")

print("Hello " + name)

x = int(input("Enter length : "))
y = int(input("Enter breadth : "))

p = 2*(x+y)
area = x*y

print("Perimeter :", p,  "Area :", area)


n = int(input("Enter a number : "))

print(math.pow(n, 0.5))


