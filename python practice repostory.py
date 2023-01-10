#!/usr/bin/env python
# coding: utf-8

# In[1]:


8+4


# In[2]:


16*5


# In[3]:


first='This is my first program.'
print(first)


# In[5]:


loaction= 'World'
print('Hello',loaction)


# In[6]:


squares = [1, 4, 9, 16, 25]


# In[7]:


squares


# In[8]:


squares[0]


# In[9]:


squares[-1]


# In[10]:


squares[-3:]


# In[11]:


squares[:]


# In[12]:


squares + [36, 49, 64, 81, 100]


# In[13]:


cubes = [1, 8, 27, 65, 125]


# In[17]:


cubes[2] 


# In[15]:


cubes


# In[18]:


cubes.append(216)


# In[19]:


cubes


# In[20]:


name = "Tesla"


# In[21]:


name


# In[23]:


name.lower()


# In[24]:


name.upper()


# In[25]:


len(name)


# In[26]:


name.capitalize()


# In[27]:


name.isalpha()


# In[28]:


starship = "Enterprise"


# In[29]:


starship.startswith("en")


# In[30]:


starship.endswith("rise")


# In[31]:


str.replace(old, new)


# In[32]:


string = "Welcome Sir "


# In[34]:


#Loops /if

x=0

#define a while loop

while(x <4):

  print(x)

  x = x+1


# In[35]:


i = 1

while i <= 10:

    print(i)

    i=i+1


# In[36]:


for x in range(2,7):

  print(x)


# In[37]:


Months = ["Jan","Feb","Mar","April","May","June"]

for m in Months:

  print(m)


# In[38]:


words = ['cat', 'window', 'defenestrate']

for w in words:

 print(w)

for w in words:

 print(w, len(w))


# In[43]:




a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):

 print(i)


# In[40]:


range(5, 10)


# In[41]:



range(0, 10, 3)


# In[42]:


list(range(9))


# In[50]:


x=2

y=4

if (x < y):
    st= "x is less than y"

          

else:

  st= "x is greater than y"

print (st)


# In[65]:


x = int(input("Please enter an integer: "))

#Please enter an integer: 42

if x < 0:

    x = 0
    print('Negative changed to zero')

elif x == 0:

    print('Zero')

elif x == 1:

    print('Single')

else:
    print('More')


# In[70]:


#Task :write a program using if-elif with different country value and total values.

total = 49

#country = "US"

country = "AU"

if country == "US":

    if total <= 50:

        print("Shipping Cost is $50")

elif total <= 100:

        print("Shipping Cost is $25")

elif total <= 150:

     print("Shipping Costs $5")

else:

        print("FREE")

if country == "AU":

    if total <= 50:

        print("Shipping Cost is $100")

else:

     print("FREE")


# In[77]:


#ask : write a program to find even or odd using for loop /range function.



for num in range(2, 10):
     if num % 2 == 0:
        print("Found an even number", num)

        continue

print("Found a number", num)


# In[80]:


#ask :write two different loops for break if x is even number and continue when the number is divide by 5.



# use the break and continue statements

for x in range (10,20):

    if (x == 15): 
        break

   #if (x % 2 == 0) : continue

        print(x)

# use the break and continue statements

for x in range (10,20):

   #if (x == 15): break

   if (x % 5 == 0): 
        continue

print(x)


# In[82]:


#Display numbers divisible by 5 from a list.Iterate the given list of numbers and print only those numbers which are divisible by 5.

#Solution:

num_list = [10, 20, 33, 45, 55]

print("Given list:", num_list)

print('Divisible by 5:')

for num in num_list:

    if num % 5 == 0:

        print(num)


# In[86]:


#Calculate the sum of all numbers from 1 to a given number

#Solution:

# s: store sum of all numbers

s = 0

n = int(input("Enter number "))

# run loop n times

# stop: n+1 (because range never include stop number in result)

for i in range(1, 1):
    s =s+i

print("\n")


# In[91]:


#Write a program to print multiplication table of a given number

#Solution:

n = 2

# stop: 11 (because range never include stop number in result)

# run loop 10 times

for i in range(1, 11, 1):

    # 2 *i (current number)

    product = n * i

    print(product)


# In[92]:


#Practice below codes for list comprehension

vec = [-4, -2, 0, 2, 4]

 # create a new list with the values doubled

[x*2 for x in vec]

# filter the list to exclude negative numbers

[x for x in vec if x >= 0]


# In[93]:


[x for x in vec if x >= 0]


# In[94]:


[x*2 for x in vec]


# In[95]:


freshfruit = [' banana', ' loganberry ', 'passion fruit ']

[weapon.strip() for weapon in freshfruit]


# In[96]:


# create a list of 2-tuples like (number, square)

[(x, x**2) for x in range(6)]


# In[98]:


basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
     print(f)


# In[99]:


for i in reversed(range(1, 10, 2)):

     print(i)


# In[102]:


#If -Elif practice

 

 

today = 'Sunday'

 

if today == 'Sunday':

    print("Today is the day of the sun.")

elif today == 'Monday':

    print("Today is the day of the moon.")

elif today == 'Tuesday':

    print("Today is the day of Tyr, the god of war.")

elif today == 'Wednesday':

    print("Today is the day of Odin, the supreme diety.")

elif today == 'Thursday':

    print("Today is the day of Thor, the god of thunder.")

elif today == 'Friday':

    print("Today is the day of Frigga, the goddess of beauty.")

elif today == 'Saturday':

    print("Today is the day of Saturn, the god of fun and feasting.")

 

 

 

 

 


# In[109]:


a_number = 55

 

if a_number % 2 == 0:

    print('{} is divisible by 2'.format(a_number))

elif a_number % 3 == 0:

    print('{} is divisible by 3'.format(a_number))

elif a_number % 5 == 0:

    print('{} is divisible by 5'.format(a_number))

else:

    print('All checks failed!')

    print('{} is not divisible by 2, 3 or 5'.format(a_number))

 


# In[110]:


#Ranges are used for iterating over lists when you need to track the index of elements while iterating.

 

a_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

 

for i in range(len(a_list)):

    print('The value at position {} is {}.'.format(i, a_list[i]))


# In[112]:


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

 

for day in weekdays:

    print('Today is {}'.format(day))

    if (day == 'Wednesday'):

        print("I don't work beyond Wednesday!")

        break

 


 

 


# In[113]:


for day in weekdays:

    if (day == 'Wednesday'):

        print("I don't work on Wednesday!")

        continue

    print('Today is {}'.format(day))


# In[114]:


def square(x):
    return x*x
print(square(4))


# In[120]:


def add_numbers(x,y):
    sum = x + y
    return sum
num1 = 9
num2 = 6
print("The sum is", add_numbers(num1, num2))


# In[124]:


def greet(name, msg):
     print("Hello", name + ', ' + msg)
greet("Sandip", "Good morning!")


# In[126]:


#Task : Write a function absolute_value to find absolute of a given number.
#Soln.
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num
print(absolute_value(0))
print(absolute_value(-4))


# In[132]:


def multiply(x,y):
    print"value of x=",x
    print"value of y=",y
    return x*y
print multiply(2,4)


# In[133]:


#Task : Write the above code to find cube of x.
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences)
print(list(filtered_result))


# In[134]:


#Task : write the above code for the expression x**3
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences)
print(list(filtered_result))


# In[138]:


#Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
#HINT:
#Create a function that will take two numbers as parameters
#Next, Inside a function, multiply two numbers and save their product in a product variable
#Next, use the if condition to check if the product >1000. If yes, return the product
#Otherwise, use the else block to calculate the sum of two numbers and return it.
#Solution:
def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2
# first condition
result = multiplication_or_sum(20, 70)
print("The result is", result)
# Second condition
result = multiplication_or_sum(40, 70)
print("The result is", result)



# # #Task: Check if the first and last number of a list is the same.
# #Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
# #Solution:
# def first_last_same(numberList):
#     print("Given list:", numberList)
#     first_num = numberList[0]
#     last_num = numberList[-1]
#     if first_num == last_num:
#         return True
#     else:
#         return False
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))
# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))
# 

# # Class

# In[144]:




class Complex:

    def __init__(self, realpart, imagpart):

        self.r = realpart

        self.i = imagpart

x = Complex(3.0, -4.5)

x.r




# In[145]:


x.i


# In[161]:


# In class Methods may call other methods by using method attributes of the self argument:

class Bag:

    def __init__(self):

        self.data = []

    def add(self, x):

        self.data.append(x)

    def addtwice(self, x):

        self.add(x)

        self.add(x)

bg=Bag()

bg.addtwice('Cricket')


# In[162]:


bg=Bag()


# In[163]:


bg.addtwice('Cricket')


# In[165]:


import statistics 


# In[168]:


data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

statistics.mean(data)


# In[167]:



statistics.median(data)


# In[170]:


import math

math.cos(math.pi / 4)


# In[171]:


math.log(1024, 2)


# In[1]:


while True:

    try:

        x = int(input("Please enter a number: "))

        break

    except ValueError:

         print("Oops! That was no valid number. Try again...")


# In[2]:


import math

math.cos(math.pi / 4)


# In[3]:


math.log(1024, 2)


# In[4]:




#write a function to append the numbers 1 to 8 in a list using for loop inside it.

#Soln:

def f1():

    s=[]

    for i in range(1,8):

        s.append(i)

    print(s)

f1()


# In[ ]:


def f2():

    p=int(input("Enter any number to generate the table "))

    for i in range(1,11):

        print(p,"*",i,"=",p*i)

    print("Table completed")

f2()


# In[2]:


#Write a parametric function to pass user input values and find simple interest.

def si(p,r,t):

    sip=p*r*t

    return sip

p=int(input("enter value"))

r=int(input("enter value"))

t=int(input("enter value"))

si(p,r,t)


# In[4]:


#Write a function to take user input and append the data in a list.
def s2():

    s=[]

    for i in range(1,5):

        p=input("enter val")

        s.append(p)

    print(s)

s2()


# ## 
