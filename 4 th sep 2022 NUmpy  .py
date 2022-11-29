#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


print(dir(np))


# In[3]:


np.sqrt(10)


# In[5]:


print('minium ', np.amin([10,23,24,12]))
print('maxium ', np.amax([10,23,24,12]))


# In[6]:


np.ceil(29.1)


# In[16]:


np.ceil(np.sqrt(10))


# In[12]:


np.ceil(np.sum(np.sqrt([5,10,15,20])))


# In[17]:


np.array([5,9,13])


# In[18]:


type([5,9,13])


# In[19]:


a= np.array([[1,2],[3,4],[5,6]])
print("Yype-", a.dtype)
print('\n','*'*20)
print('\n', a)
      


# In[20]:


a.ndim


# In[22]:


np.array([1,2,3],dtype= float)


# In[24]:


a=[1,2]
c=np.array(a)
print(c)


# In[25]:


B=np.asarray(c)
print(B)


# In[26]:


my_mat=[[1,2,3],[4,5,6],[6,7,8]]
mat=np.array(my_mat)


# In[28]:


print(type(mat))
print(mat)
print(mat.ndim)
print(mat.size)
print(mat.shape)
print(mat.dtype)


# In[29]:


list(range(2,10.5,.4))


# In[31]:


a=np.arange(2,10.5,.4)
a


# In[32]:


a[::-1]


# In[33]:


print(np.arange(50,-1,-5))


# In[36]:


print(np.linspace(10,40,5))


# In[39]:


print(np.linspace(2.0,3.0,num=4,endpoint=False,retstep= True))


# In[40]:


np.linspace(2.0,3.0,num=4,endpoint=False,retstep= True)


# In[ ]:




