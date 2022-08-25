#!/usr/bin/env python
# coding: utf-8

# In[16]:


i = 10
if i >10:
    print('it is less than 10')
elif i<6:
    print('it is less than 5')
else:
    print('it is something else ')


# In[19]:


print('it is less than 10 ') if i>10 else print('it is something else') 


# In[23]:


item_1=100
item_2=300
if (item_1 +item_2) >= 500:
    print('you are elgible for free shiping')
else:
    extra=500-(item_1 + item_2)
    print('please add ',extra, 'Rs worth of an item for free shiping')


# In[25]:


a =200
b =100
c=300
if a>b and c >a:
    print('Both condition is true')
else:
    print('both are not true')


# In[28]:


a =200
b =100
c=300
if a>b or c <a:
    print('Atleast one condion is true.')
else:
    print('both are not true')


# In[49]:


marks =34
if marks >= 60:
    if marks >75:
        print(marks, '-Distinction')
    else:
        print(marks, '- first class')
elif marks > 50 and marks <= 60:
    print(marks,'- second class')
elif marks >= 35:
    print(marks, '-pass')
else:
    print(marks, 'failed , Better luck next time')


# In[51]:


num1 = 20
num2 = 30
if num1 == "20":
    print('it is 20')
elif num2 > 25:
    print('it is grether than 25')


# In[52]:


range(10)


# In[53]:


list(range(10))


# In[60]:


list(range (0,11,2))


# In[ ]:




