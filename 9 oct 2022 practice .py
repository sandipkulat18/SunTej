#!/usr/bin/env python
# coding: utf-8

# In[3]:


for  i in range (5):
    print(i)


# In[4]:


def func():
    global j
    for j in range(5):
        print(j)


# In[5]:


func()


# In[9]:


i=list(range(0,100))


# In[10]:


i


# In[11]:


def tare(a):
    if a%2== 0:
        return a


# In[12]:


tare(7)


# In[13]:


list(filter(tare,i))


# In[14]:


import numpy as np


# In[15]:


np.random.rand(3,2)


# In[18]:


np.mean(np.random.rand(3,2))


# In[19]:


for h in i:
    print(i)


# In[20]:


24%2


# In[21]:


2==2


# In[25]:


def fun(a):
    print( a*a)
    print('this is Numpy')


# In[26]:


fun (3)


# In[27]:


def give(a='string'):
    print( a)
    return a


# In[28]:


give()


# In[33]:


x=int(input('enter x'))
y=int(input('enter y'))


# In[36]:


try:
    a=x/y
    print(a)
except ZeroDivisionError:
    print(0)
finally:
    print('finally it is working')

try:
  a=x/y
  print(a)
 


# In[37]:


p= ['1','2','3']


# In[38]:


for i in p:
    print(type(i))


# In[41]:


g=map(int,p)


# In[43]:


type(g)


# In[44]:


list(g)


# In[46]:


k=list(map(int,p))


# In[47]:


k


# In[49]:


h=list(range(0,1000))


# In[50]:


h


# leh(h)

# In[51]:


len(h)


# In[52]:


map(func, h)


# In[53]:


type(h)


# In[55]:


list(map(fun,h))


# In[59]:


def function(a):
    return a*a


# In[60]:


function(2)


# In[61]:


f=list(map(function,h))


# In[62]:


f


# In[65]:


def tare(a):
    if a%2==0:
        return a
    


# In[66]:


tare(7)


# In[67]:


list(filter (tare,h))


# In[68]:


set(filter (tare,h))


# In[ ]:




