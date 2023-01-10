#!/usr/bin/env python
# coding: utf-8

# In[2]:


def main():

 x,y =2,4

 if(x < y):

  st= "x is less than y"

 else:

  st= "x is greater than y"

 print (st)

if __name__ == "__main__":

 main()


# In[5]:




def main():

 x,y =12,8

 if(x < y):

  st= "x is less than y"

 else:

  st= "x is greater than y"

 print(st)

if __name__ == "__main__":

 main()


# In[6]:


def main():

 x,y =8,8

 if(x < y):

  st= "x is less than y"

 elif (x == y):

  st= "x is same as y"

 else:

  st="x is greater than y"

 print(st)

if __name__ == "__main__":

 main()


# In[7]:


class myClass():

  def method1(self):

      print("DT")

  def method2(self,someString):

      print("Software Testing:" + someString)

def main():

  # exercise the class methods

  c = myClass ()

  c.method1()

  c.method2(" Testing is fun")

if __name__== "__main__":

  main()


# In[ ]:





# In[9]:


#5.Print characters from a string that are present at an even index number

#For example, str = "DATATRAINED" so you should display â€˜Dâ€™, â€˜Tâ€™, â€˜Tâ€™, â€˜Aâ€™,'N','D' .

#HINT:

#Use Python input() function to accept a string from a user.

#Calculate the length of string using the len() function

#Next, iterate each character of a string using for loop and range() function.
#Use start = 0, stop = len(s)-1, and step =2. the step is 2 because we want only even index numbers

#in each iteration of a loop, use s[i] to print character present at current even index number

#Solution:

# accept input string from a user

word = input('Enter word ')

print("Original String:", word)

# get the length of a string

size = len(word)

# iterate a each character of a string

# start: 0 to start with first character

# stop: size-1 because index starts with 0

# step: 2 to get the characters present at even index like 0, 2, 4

print("Printing only even index chars")

for i in range(0, size - 1, 2):

    print("index[", i, "]", word[i])


# In[10]:


#Concatenate two lists index-wise

#Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

#Solution:

#Use the zip() function. This function takes two or more iterables (like list, dict, string), aggregates them in a tuple, and returns it.

list1 = ["M", "na", "i", "Ke"]

list2 = ["y", "me", "s", "lly"]

list3 = [i + j for i, j in zip(list1, list2)]

print(list3)


# In[11]:


#Turn every item of a list into its square.Given a list of numbers, write a program to turn every item of a list into its square.

#Solution:

numbers = [1, 2, 3, 4, 5, 6, 7]

# result list

res = []

for i in numbers:

    # calculate square and add to the result list

    res.append(i * i)

print(res)


# In[12]:


#Replace listâ€™s item with new value if found

#You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

#Solution:

list1 = [5, 10, 15, 20, 25, 50, 20]

# get the first occurrence index

index = list1.index(20)

# update item present at location

list1[index] = 200

print(list1)


# In[13]:


#Write a Program to extract each digit from an integer in the reverse order.

#For example, If the given int is 7536, the output shall be â€œ6 3 5 7â€œ, with a space separating the digits.

number = 7536

print("Given number", number)

while number > 0:

    # get the last digit

    digit = number % 10

    # remove the last digit and repeat the loop

    number = number // 10

    print(digit, end=" ")


# In[15]:


#Count the total number of digits in a number

#Solution:

num = 758695

count = 0

while num != 0:

    # floor division

    # to reduce the last digit from number

    num = num // 10

    # increment counter by 1

    count = count + 1

print("Total digits are:", count)


# In[16]:


import sqlite3


# In[61]:


conn = sqlite3.connect('exedatabase.db')

print ("Opened database successfully");

conn.execute('create table Student(ID INT Primary Key,NAME Test,AGE INT,ADDRESS,SALARY float)')

conn.execute("INSERT INTO Student (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Ajeet', 27, 'Delhi', 20000.00 )");

conn.execute("INSERT INTO Student(ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 22, 'London', 25000.00 )");

conn.execute("INSERT INTO Student(ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Mark', 29, 'CA', 200000.00 )");

conn.execute("INSERT INTO Student (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Kanchan', 22, 'Ghaziabad ', 65000.00 )");

conn.commit()

# now start writing SQL query for select/update/delete


# In[47]:


result= conn.execute("select * from Student")
for row in result:
    print(row)


# In[54]:


sql= "update Student set ADDRESS= 'Mumbai' where ID= 1"
conn.execute(sql)
conn.commit()


# In[55]:


result= conn.execute("select * from Student")
for row in result:
    print(row)


# In[57]:


sql= "Delete from  Student   where ID= 1"
conn.execute(sql)
conn.commit()


# In[60]:


result= conn.execute("select * from Student")
for row in result:
    print(row)


# In[ ]:




