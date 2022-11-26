#!/usr/bin/env python
# coding: utf-8

# In[1]:


emp_sal= [12000,23000,45000,50000,12345,218787]
emp_sal


# In[13]:


less_sal=[]
for val in emp_sal:
    if val <25000:
        less_sal.append(val)
  


# In[14]:


print(less_sal)


# In[23]:


emp_sal= [12000,23000,45000,50000,12345,218787]
emp_name =['sandip','sachin', 'Rohit','ganesh','om','yash']


# In[25]:


for val in emp_name:
    if val == 'Rohit':
        name_index= emp_name.index(val)
        print('Dear '+ val + ' your salary is',emp_sal[name_index])


# In[31]:


def check_premium(gender,year_of_birth,smoker):
    smoker= 'Your annual premium is  = Rs '
    non_smoker= 'your Disconted anual prenium is = Rs'
    
    if gender == 'male' :
        if year_of_birth> 1990 and year_of_birth<=2000 :
            if smoker== 'Yes' :
                print(smoker, 35000)
            else:
                print(non_smoker, 35000- (35000 * 0.1))
            
        elif year_of_birth> 1970 and year_of_birth<=1990 :
            if smoker== 'Yes' :
                print(smoker, 40000)
            else:
                print(non_smoker, 40000- (40000 * 0.5))
                
    elif gender == 'female' :
        if year_of_birth> 1990 and year_of_birth<=2000 :
            if smoker== 'Yes' :
                print(smoker, 30000)
            else:
                print(non_smoker, 30000- (30000 * 0.1))
            
        if year_of_birth> 1970 and year_of_birth<=1990 :
            if smoker== 'Yes' :
                print(smoker, 35000)
            else:
                print(non_smoker, 35000- (35000 * 0.5))
        


# In[40]:


gender = input('select male or female  ')
dob= int(input('enter your dob ?'))
smoker= input('select yes or no')
check_premium(gender,dob,smoker)


# In[38]:


check_premium(gender,smoker)


# In[ ]:





# In[ ]:




