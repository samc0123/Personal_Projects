import random
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

n=4

try:
    make_pie(n)
except IndexError:
    make_pie(random.randint(0,len(fruits)-1))