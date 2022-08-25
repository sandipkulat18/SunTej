#!/usr/bin/env python
# coding: utf-8

# In[6]:


lacation = ['mumbai', 'pune', 'nagpur',"nashik",]


# In[7]:


lacation


# In[8]:


for city in lacation:
    print(city)


# In[12]:


salary =[1000,2000,4000,5000,6000,5500,8000,7500]
for val in salary:
    if val > 3500:
        print(val)


# In[15]:


students_score= [34,45,33,56,77,67,98,85,54,31,89]
for marks in students_score:
    if marks >60:
        if marks > 70:
            print (marks, '-distiction')
        else:
            print(marks, '-first calss')
    elif marks >50 and marks <= 60:
        print(marks, '-second class')
    elif marks > 35:
        print (marks, "-pass")
    else:
        print(marks, '-failed, Better luck next time')
        


# In[16]:


print(salary)


# In[20]:


sal = [val for val in salary if val > 5500]


# In[21]:


sal


# In[27]:


for num in range (2,7):
    print("multiplicaion table for", num)
    for i in range (1,11):
        print(num * i)
        if i == 10:
            print('\n')
else:
    print("*"* 30)
    print('end of multiplication table')
    print("*"* 30)


# In[33]:


i =0
while i <10:
    i += 1
    print( i, "data trained")
    


# In[34]:


import time


# In[40]:


result= time.localtime()
print(result)


# In[41]:


print(result)


# In[43]:


while True:
    result = time.localtime()
    if result.tm_hour== 18 and result.tm_min == 0:
        print('good evening buddy')
        break


# In[44]:


students= ['sandip','sachin','ganesh','rahul','om']
for name in enumerate(students):
    print(name)


# In[53]:


for name in enumerate(students,101):
    print(name)


# In[54]:


student_name= ['sandip','sachin']
student_marks=[12,23,23]


# In[55]:


details= list(zip(student_name,student_marks))


# In[56]:


details


# In[57]:


name,marks=zip(* details)


# In[58]:


name


# In[68]:


marks


# In[75]:


city= ['hydrabad','mumbai','goa','pune','india','kerala']
for val in city:
    if val== "goa":
        break
    print(val)


# In[76]:


city= ['hydrabad','mumbai','goa','pune','india','kerala']
for val in city:
    if val== "goa":
        continue
    print(val)


# In[77]:


salary=[2000,3000,4800,4000,4990,5000,4400,4600]
for i in salary:
    if i >4600:
        break
    print(i)


# In[78]:


salary=[2000,3000,4800,4000,4990,5000,4400,4600]
for i in salary:
    if i >4600:
        continue
    print(i)


# In[84]:


s= 'i Love you'


# In[85]:


s


# In[86]:


s[0:]


# In[87]:


s[2:7]


# In[88]:


s [0]


# In[90]:


s[5].upper()


# In[95]:


s[::-2]


# In[108]:


def sandip(name):
    print('Hello',name)
sandip('Good morning')


# In[107]:


def num(num1,num2):
    return num1*num2
num(2,3)

    


# In[ ]:




