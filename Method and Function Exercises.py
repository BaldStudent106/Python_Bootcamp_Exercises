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

count={"lowercount":0,"uppercount":0}

def is_up(string,count):
    for character in string:
        if (character.islower()):
            count["lowercount"]+=1
        else:
            count["uppercount"]+=1
    return(count)

string="Hi, This is my Python Exercise"

count=is_up(string,count)

print(f'There is {count["lowercount"]} lowercase letters')
print(f'There is {count["uppercount"]} uppercase letters')
        

'''
Question 4: Write a Python function that takes a list and returns a list with uniques element of the first list
'''
list_example=[2,3,4,5,1,5,51,23,5,1,1,3]

def unique(list1):
    x=[]
    for i in list1:
        if i not in x:
            x.append(i)
    return x

print(unique(list_example))

'''
Question 5: Write a Python Function to multiple all the numbers in a list
'''

list_example2=[3,2,5,1,-4]

def multiplyfunc(list_input):
    num=list_input[0]
    for i in list_input[1::1]:
        num*=i
    return num

print(multiplyfunc(list_example2))
        
'''
Question 6: Write a Python function to check whether a word or phrase is palindrome or not
'''    


def palindrome(string):
    string.replace(" ","")
    return(string == string[::-1])

print(palindrome("racecar"))

'''
Question 7: Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
'''

import string

string_example2="aaaaaabcdefghijklmnopqrstuvwxyz   "
def ispangram(string,alphabet=string.ascii_lowercase):
   string.replace(" ","")
   string=string.lower() 
   set1=set(string)
   set2=set(alphabet)
   return set1==set2
result=ispangram(string_example2)
if(result):
    print(f"String {string_example2} is a pangram")
else:
    print(f"String {string_example2} is a pangram")