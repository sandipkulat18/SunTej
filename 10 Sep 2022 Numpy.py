#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[3]:


print('ventor of zeros \n ------')
print(np.zeros(5))


# In[7]:


print('Matrix of zeros \n ------')
print(np.zeros((5,6)))


# In[9]:


print('Matrix of zeros \n ------')
print(np.ones((5,6)))


# In[11]:


print('Matrix of 5 s\n ------')
print(5*np.ones((3,4)))


# In[14]:


x= np.arange(30).reshape(5,6)
print(x)


# In[15]:


np.arange(10)


# In[16]:


# Reshaping
import numpy as np
from numpy.random import randint as ri

a = ri(1,99,30)
a


# In[17]:


c= a.reshape(6,5)
c


# In[20]:


print("min of a",a.min())
print("max of a", a.max())


# In[22]:


np.mean(c)


# In[29]:


print(np.random.seed(6))
print("Rondom number generation (from Uniform distubution)")


# In[44]:


print(np.random.rand(10,6))


# In[45]:


print('number  of normal distubutor with zero mean  and statand deviation  1' )
print(np.random.randn(10,3))


# In[50]:


print('Rondam  integer  vector ', np.random.randint(5,20,10))


# In[48]:


print("\n rondam interger Matrix")
print(np.random.randint(1,3000,(5,6)))


# In[41]:


## Enter Real time example otp example

while True:
    otp1=np.random.randint(1000,10000,1)
    print("you are Otp - ", otp1)
    user_otp=int(input('enter opt'))
    if otp1== user_otp:
        print('login successfully')
        break
    else:
        print('invalide otp,generate new otp')
        continue
        


# In[42]:


import numpy as np
from numpy.random import randint as ri

a = ri(1,99,30)
a


# In[58]:


#sorting
m= ri (1,100,25).reshape(5,5)
print("\n5x5 Matrix of Rodam integer\n",'-'*20,"\n",m )
print("\nhere is sorted  matrix along each row\n",'-'*20,"\n",np.sort(m) )
print("\nhere is sorted  matrix along each column\n",'-'*20,"\n",np.sort(m,axis=0))


# In[59]:


# Numpy condtition
emp_sal= np.random.randint(8,70,10)
emp_sal


# In[60]:


print(np.where(emp_sal<25))


# In[66]:


emp_sal[np.where(emp_sal<25)]


# In[65]:


np.clip(emp_sal,a_min=20, a_max=50)


# In[ ]:


# indecing and slicing


# In[69]:


arr= np.arange(10,30)
print("Array", arr)


# In[71]:


print("Element at 7th indesx :- ", arr[7])


# In[72]:


print("Element at 2ng,4th, and 9th  indesx :- ", arr[[2,4,9]])


# In[73]:


my_mat= [[1,2,3],[3,4,5],[7,8,9]]
mat= np.array(my_mat)
mat


# In[78]:


print("\n double bracket indesing \n --------")
print('\n elemnt in  row index 1 and column 2 : -', mat[1][2])


# In[76]:


mat


# In[80]:


print ('Entire row  at index 2 :- ', mat[2])
print("\nentire column at index 3: \n", mat[:,1:])


# In[84]:


print(mat[1:2,1:2])


# In[83]:


mat


# In[85]:


print('',mat[0:2,[1,2]])


# In[89]:


# Update Matrix
print('Original Matrix =\n\n',mat)


# In[90]:


mat[0,1]=35
mat


# mat[1,0]=100
# mat

# In[91]:


mat[1,0]=100
mat


# In[95]:


mat=np.array(ri(10,100,15)).reshape(3,5)
print('matrix og random digit number \n-------------\n',mat)


# In[96]:


mat>50


# In[97]:


print('element is getter than 50 \n ', mat[mat>50])


# In[100]:


marks=70
np.where(marks>68, 'pass','fail')


# In[101]:


non_zero=ri(-10,50,100)
print(non_zero)
np.count_nonzero(non_zero)


# In[104]:


array=np.random.randint(0,20, size=(3,4))
print(array)
array.ravel()


# In[105]:


array.flatten()


# In[107]:


#universal fucntion
mat1=np.array(ri(1,10,9)).reshape(3,3,)
mat2=np.array(ri(1,10,9)).reshape(3,3,)

print("\n-----------\n",mat1)
print("\n-----------\n",mat2)


# In[108]:


print("\nAddition-----------\n",mat1+mat2)


# In[111]:


start= np.zeros((3,3))
start


# In[112]:


add_row= np.array([[1,0,2]])
add_row


# In[113]:


y = start+add_row
y


# In[117]:


new= add_row.T
new


# In[116]:


test= new+start
test


# In[ ]:




