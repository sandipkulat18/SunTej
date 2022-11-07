#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns 
import pickle
from sklearn.metrics import r2_score
from sklearn import metrics
from sklearn.model_selection import cross_val_score

import warnings
warnings.filterwarnings('ignore')


# In[9]:


data= pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/Sales_LinReg.csv')
data.head()


# In[10]:


data.shape


# In[11]:


data.describe()## undestand data at high point . check the statucs of the data


# In[13]:


data.isnull().sum()### check the null


# In[15]:


data.head()


# In[20]:


data['Republic']=data['Republic'].fillna(data['Republic'].mean())
data['NDTV']=data['NDTV'].fillna(data['NDTV'].mean())
data['TV9']=data['TV9'].fillna(data['TV9'].mean())
data['AajTak']=data['AajTak'].fillna(data['AajTak'].mean())


# In[ ]:


### fill the null value colume


# In[ ]:


#verify it NAN are filled


# In[21]:


data.describe()


# In[22]:


data.isnull().sum()


# In[28]:


#let move on visuvalation
plt.figure(figsize=(20,15),facecolor = 'yellow')
plotnumber =1
for column in data :
    if plotnumber <=6:
        ax=plt.subplot(2,3,plotnumber)
        sns.distplot(data[column])
        plt.xlabel(column,fontsize=10)
    
    plotnumber += 1
plt.tight_layout()


# In[33]:


#divide data set into label
y= data ['sales']
x=data.drop(columns = ['sales'])


# In[34]:


y #


# In[35]:


x


# In[39]:


plt.figure(figsize=(15,10),facecolor = 'red')
plotnumber =1
for column in x :
    if plotnumber <=6:
        ax=plt.subplot(2,3,plotnumber)
        plt.scatter(x[column],y)
        plt.xlabel(column,fontsize=10)
        plt.ylabel('sales',fontsize=10)
    
    plotnumber += 1
plt.tight_layout()


# In[42]:


x.drop(columns=['TV5','TV9'],axis=1,inplace=True)


# In[44]:


#data scaling .formul
scaler =StandardScaler()
x_scaled=scaler.fit_transform(x)


# In[45]:


x_scaled


# In[49]:


x_train,x_test,y_train,y_test=train_test_split(x_scaled,y,test_size=0.25,random_state=100)
y_train.head()


# In[51]:


regression = LinearRegression()
regression.fit(x_train, y_train)
LinearRegression()


# x.tail(2)

# In[52]:


x.tail(2)


# In[58]:


print('sales prediction : ',regression.predict(scaler.transform([[75.5, 10.8, 75.5]])))


# In[59]:


pred=regression.predict(x_train)


# In[60]:


pred


# In[61]:


y_pred=regression.predict(x_test)
y_pred


# In[64]:


print('training score : ' ,r2_score(y_train,pred)*100)
print('testing score : ' ,r2_score(y_test,y_pred)*100)


# In[65]:


from sklearn.metrics import mean_absolute_error,mean_squared_error


# In[66]:


mean_absolute_error(y_test,y_pred)


# In[67]:


mean_squared_error(y_test,y_pred)


# In[68]:


np.sqrt(mean_squared_error(y_test,y_pred))


# In[69]:


print(cross_val_score(regression,x_scaled, y ,cv =5).mean())


# In[ ]:




