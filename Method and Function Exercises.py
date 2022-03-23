'''
My Exercises for testing my knowledge about methods and functions of python
'''

'''
Question  1: Create a function that will calculate the volume of a sphere given its radius.
The volume of the sphere is 3/4 x pi x r**3
'''
import math
pi=math.pi
vol= lambda x:3/4*pi*x**3
print(vol(3))

'''
Question 2: Write a function that checks whether a number is in a given range
'''

def check(num, low, high):
    if(num>low and num<high):
        print(f"{num} is within the range")
    else:
        print(f"{num} is not within the range")

check(11, 0, 10)

'''
Question 3: Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
'''

lowercount=0
uppercount=0


def is_up(string,lowercount,uppercount):
    for character in string:
        if (character.islower()):
            lowercount+=1
        else:
            uppercount+=1
    return(lowercount,uppercount)

string="Hi, This is my Python Exercise"

lowercount, uppercount=is_up(string,lowercount, uppercount)

print(f"There is {lowercount} lowercase letters")
print(f"There is {uppercount} uppercase letters")
        

'''
Question 4: Write a Python function that takes a list and returns a list with uniques element of the first list
'''
list_example=[2,3,4,5,1,5,51,23,5,1,1,3]

def unique(list1):
    uniquelist=set()
    for i in list1:
       uniquelist.add(i)
    return uniquelist

print(list(unique(list_example)))

'''
Question 5:
'''