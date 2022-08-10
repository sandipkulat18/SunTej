#!/usr/bin/env python
# coding: utf-8

# In[1]:


def sandip():
    while True:
        try:
            val = int(input("please enter yor interger :"))
        except:
            print("you did not enter interger :")
            continue
        else:
            print("yor enter r interger :")
            break
        finally:
            print("Finnaly i excuted")
        print(val)


# In[2]:


sandip()


# In[12]:


def my_list():
    while True:
        try:
            num = int(input("please enter yor interger :"))
        except:
            print("you did not enter interger :")
            continue
        else:
            print("yor enter r interger :")
            break
        finally:
            print("Finnaly i excuted")
        print(num)
        


# In[13]:


my_list()


# In[17]:


def sachin():
        try:
            num = int(input("please enter yor interger :"))
        except:
            print("you did not enter interger :")
            num = int(input("please renter enter yor interger :"))
        finally:
            print("enter r interger")
        print()


# In[18]:


sachin()


# In[ ]:




