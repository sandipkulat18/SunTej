#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import pickle 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data =pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/Advertising.csv')


# In[ ]:


data.head()


# In[5]:


data.to_csv('D:\sandip\Adv.csv')


# In[6]:


data.shape


# In[8]:


data.describe()


# In[9]:


data.info()


# In[11]:


data.isnull().sum()


# In[14]:


fig, axs=plt.subplots(1,3)
data.plot(kind='scatter',x='TV',y='sales',ax=axs[0],figsize=(12,6))
data.plot(kind='scatter',x='radio',y='sales',ax=axs[1])
data.plot(kind='scatter',x='newspaper',y='sales',ax=axs[2])
fig.savefig('testdata.jpg')


# In[23]:


X=data[['TV']]
y=data.sales

from sklearn.linear_model import LinearRegression

lm=LinearRegression()

lm.fit(X, y)


# In[24]:


print(lm.intercept_)
print(lm.coef_)


# In[28]:


7.032594+0.0475337*50


# In[27]:


lm.predict([[50]])


# # Metrics

# In[29]:


from sklearn.metrics import r2_score


# In[30]:


preducted_sales=lm.predict(X)


# In[31]:


X.head()


# In[32]:


preducted_sales


# In[33]:


r2_score(y_true=y,y_pred=preducted_sales)


# # Multiple Linear Regresion

# In[37]:


x=data[['TV','radio','newspaper']]
from sklearn.linear_model import LinearRegression

lm=LinearRegression()

lm.fit(x, y)


# In[41]:


print('Intercept    ->',lm.intercept_)
print('TV:          ->',lm.coef_[0])
print('Radio:       ->',lm.coef_[1])
print('Newspepar:   ->',lm.coef_[2])


# # Feuture Selection

# In[42]:


x=data[['TV','radio',]]
from sklearn.linear_model import LinearRegression

lm=LinearRegression()

lm.fit(x, y)


# In[43]:


preducted_sales=lm.predict(x)
r2_score(y,preducted_sales)


# In[44]:


x=data[['TV','radio','newspaper']]
from sklearn.linear_model import LinearRegression

lm=LinearRegression()

lm.fit(x, y)


# In[45]:


preducted_sales=lm.predict(x)
r2_score(y,preducted_sales)


# # Project 1 with Linear Regression

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pickle

import warnings
warnings.filterwarnings('ignore')


# In[4]:


df=pd.read_csv('Admission.csv')


# In[5]:


df.to_csv('D:\sandip\Admission.csv')


# In[6]:


df


# In[7]:


df.head()


# In[8]:


df.shape


# In[9]:


df.describe()


# In[10]:


df['University Rating']=df['University Rating'].fillna(df['University Rating'].mode()[0])
df['TOEFL Score']=df['TOEFL Score'].fillna(df['TOEFL Score'].mean())
df['GRE Score']=df['GRE Score'].fillna(df['GRE Score'].mean())


# In[11]:


df.describe()


# In[12]:


df.describe()


# In[13]:


df=df.drop(columns=['Serial No.'])
df.head()


# In[14]:


y=df['Chance of Admit']
x=df.drop(columns=['Chance of Admit'])


# In[15]:


plt.figure(figsize=(20,25),facecolor='red')
plotnumber=1

for column in df:
    if plotnumber <=8:
        ax=plt.subplot(3,3,plotnumber)
        sns.distplot(df[column])
        plt.xlabel(column,fontsize=15)
        
    plotnumber+=1
plt.tight_layout()


# In[ ]:





# In[16]:


y=df['Chance of Admit']
x=df.drop(columns=['Unnamed: 0','Chance of Admit'])


# In[17]:


x


# In[18]:


y


# In[ ]:





# In[19]:


plt.figure(figsize=(15,10),facecolor='yellow')
plotnumber=1

for column in x:
    if plotnumber <=8:
        ax=plt.subplot(3,3,plotnumber)
        plt.scatter(x[column],y)
        plt.xlabel(column,fontsize=10)
        plt.ylabel('Chance of Admit',fontsize=10)
        
    plotnumber+=1
    
plt.tight_layout()


# In[20]:


scaler= StandardScaler()
x_scaled=scaler.fit_transform(x)


# In[21]:


x_scaled


# In[22]:


help(LinearRegression)


# In[ ]:





# In[23]:


x_train,x_test,y_train,y_test = train_test_split(x_scaled,y,test_size=0.25,random_state=348)
y_train.head()


# In[24]:


regression=LinearRegression()
regression.fit(x_train,y_train)


# In[25]:


df.tail(2)


# In[26]:


print('Chance of Admission is :',regression.predict(scaler.transform([[327.0, 113.0, 4.0, 4.5, 4.5, 9.04, 0]])))


# In[27]:


#you have save model and later you can use prediction


# In[28]:


pickle.dump(regression,open('reg_model','wb'))


# In[29]:


loaded_model=pickle.load(open('reg_model','rb'))
a=loaded_model.predict(scaler.transform([[314,103,2,2,3,8.21,0]]))


# # lets check how well modell fit on train data 

# In[30]:


regression.score(x_train,y_train)


# In[31]:


regression.score(x_test,y_test)


# In[32]:


y_pred=regression.predict(x_test)


# In[33]:


y_pred


# In[34]:


plt.scatter(y_test,y_pred)
plt.xlabel('Actual chance of Admission')
plt.ylabel('Predicted Chance of Admission')
plt.title('Actual VS model predicted')
plt.show()


# In[35]:


from sklearn.metrics import mean_squared_error,mean_absolute_error


# In[36]:


y_pred=regression.predict(x_test)


# In[37]:


mean_absolute_error(y_test,y_pred)   


# In[38]:


mean_squared_error(y_test,y_pred)


# In[39]:


np.sqrt(mean_squared_error(y_test,y_pred))


# In[40]:


from sklearn.linear_model import Ridge,Lasso,RidgeCV,LassoCV


# In[41]:


lasscv=LassoCV(alphas=None,max_iter=100,normalize=True)
lasscv.fit(x_train,y_train)


# In[42]:


alpha=lasscv.alpha_
alpha


# In[43]:


lasso_reg=Lasso(alpha)
lasso_reg.fit(x_train,y_train)


# In[44]:


lasso_reg.score(x_test,y_test)


# # Ridge Regreasion model

# In[46]:


ridgescv=RidgeCV(alphas=np.arange(0.001,0.1,0.01),normalize=True)
ridgescv.fit(x_train,y_train)


# In[47]:


ridgescv.alpha_


# In[48]:


ridge_model=Ridge(alpha=ridgescv.alpha_)
ridge_model.fit(x_train,y_train)


# In[49]:


ridge_model.score(x_test,y_test)


# In[52]:


np.arange(1,10,2)


# In[ ]:




