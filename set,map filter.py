#!/usr/bin/env python
# coding: utf-8

# In[2]:


x=set()


# In[3]:


type(x)


# In[4]:


x.add(1)


# In[5]:


x


# In[6]:


x.add(2)
x


# In[7]:


x.add(1)
x

x


# In[13]:


xyz= ("sandip","sachin","sandip","ganesh","sachin","rahul","rahul")
set(xyz)


# In[14]:


xyz= ("sandip","sachin","sandip","ganesh","sachin","rahul","rahul")
set(xyz)


# In[48]:


def sandip (T):
    return(float(9)/5*T + 32)
def celcius (T):
    return(float(9)/5*T - 32)
temp=[0,22.5,40,100]

F_temp=list(map(sandip,temp))

F_temp


# In[40]:


list(map(celcius,F_temp))


# In[52]:


list(map(lambda x:(5.0/9)*(x+32),F_temp))


# In[ ]:





# In[63]:


def even_check(num):
    if num%2 == 0:
        return True


# In[65]:


lst =range(30)
list(filter(even_check,lst))


# In[69]:


list(filter(lambda x :x%2 == 0,lst ))


# In[70]:



abc = ( )

type(abc)


# In[72]:


abc = set( )

abc


# In[ ]:




