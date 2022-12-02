#!/usr/bin/env python
# coding: utf-8

# In[2]:


from numpy.random import randint as ri
import pandas as pd


# In[3]:


marks= ri(30,101,1000)
student_mark=pd.Series(marks)
student_mark.head()


# In[7]:


marks_mean=student_mark.mean()
print("Mark Mean : ",marks_mean)
marks_std=student_mark.std()
print("Mark Std : ",marks_std)


# In[6]:


student_mark.shape


# In[20]:


x=50


# In[21]:


import scipy.stats as  st


# In[22]:


prob=st.norm.cdf(x,loc=marks_mean,scale=marks_std)
prob


# In[23]:


score=(x-marks_mean)/marks_std
score


# In[ ]:





# In[14]:


(50-marks_mean)/marks_std


# In[15]:


(60-marks_mean)/marks_std


# In[24]:


x=[23,34,56]


# In[25]:


import statistics as st


# In[26]:


avg= st.mean(x)
avg


# In[27]:


import numpy as np


# In[28]:


avg=np.sum((np.square(23-avg)+np.square(34-avg)+np.square(56-avg))/3)


# In[29]:


avg


# In[31]:


np.var(x)


# In[32]:


np.std(x)


# In[34]:


mean=25


# In[40]:


sample_mean=24.2
std=1.5
n=30


# In[42]:


z=(sample_mean-mean)/(std/np.sqrt(30))


# In[43]:


z


# In[ ]:




