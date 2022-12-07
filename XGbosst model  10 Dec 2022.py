#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import  train_test_split, GridSearchCV

from sklearn.metrics import r2_score,mean_squared_error
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')


# In[8]:


df= pd.read_csv('vehicles_data_students.csv')


# In[12]:


df.head()


# In[14]:


drop_columns=['Unnamed: 0','id','title_status','size','lat','long','county']
df=df.drop(columns=drop_columns,axis=1)


# In[7]:


get_ipython().system('pip install xgboost')


# In[15]:


df.shape


# In[16]:


import xgboost as xgb


# In[17]:


df.isnull().sum()


# In[18]:


df=df.dropna()
df.head(5)


# In[19]:


df.shape


# In[20]:


df.describe()


# In[21]:


df.drop_duplicates(inplace=True)


# In[22]:


df.shape


# In[27]:


numerics=['int8','int16','int32','int64','float16','float32','float64']
categorical_columns=[]

features=df.columns.values.tolist()

for col in features:
    if df[col].dtype in numerics:
        continue
    categorical_columns.append(col)
    


# In[28]:


categorical_columns


# In[ ]:




