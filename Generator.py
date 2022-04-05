'''
A few exercises for python generators
'''

#Question 1: Create a generator that generates the squares of numbers up to some number N

def gensquares(n):
    
    for num in range(n):
        yield num**2

for x in gensquares(10):
    print(x)

#Question 2: Create a generator that yields "n" random numbers between a low and high number (that are inputs). 

import random
num=random.randint(0,10)
def rand_num(low,high,n):
    for x in range(n):
        yield random.randint(low,high)

for x in rand_num(0,9,num):
        print (x)

#Question 3: Use the iter() function to convert the string below into an iterator:
s='hello'
word=iter(s)
print(next(word))