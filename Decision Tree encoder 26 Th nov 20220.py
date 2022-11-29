#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:


# DEcision Tree 
#GIni IMpuruty = lowwest First
# entropgy\ higest one
#classfire tree = last one is label


# In[2]:


df= pd.read_csv("https://raw.githubusercontent.com/training-ml/Files/main/wine.csv")
df


# In[3]:


df.describe()


# In[4]:


df.head()


# In[12]:


df.isnull().sum()


# In[8]:


df.to_csv("D:\Software\Sandip\df_copy.csv",index=False,header=True)


# In[9]:


import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split,GridSearchCV
from  sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score,roc_curve,classification_report
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[10]:


df


# In[13]:


df.isnull().sum()


# In[14]:


df.shape


# In[15]:


from sklearn.preprocessing import OrdinalEncoder


# In[17]:


ord_Encoder= OrdinalEncoder(categories=[['Low','Medium','High']])
df1=ord_Encoder.fit_transform(df[["Alcohol_content"]])
df1


# In[18]:


df["Alcohol_content"]=df1
df.head()


# In[ ]:


# PLoting Header


# In[23]:


df_occure=df.corr().abs()
plt.figure(figsize=(12,8))
sns.heatmap(df_occure,annot=True,annot_kws={"size":10})
plt.show()


# In[24]:


plt.scatter(df.alcohol,df.Alcohol_content)
plt.xlabel('Alcohol')
plt.xlabel('Alcohol_content')
plt.title('Alcohol vs Alcohol)content')
plt.show()


# In[25]:


x= df.drop(columns=['quality','Alcohol_content'])
y=df['quality']


# In[26]:


x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.25,random_state=41)


# In[40]:


def metric_score(clf,x_train,x_test,y_train,y_test,train=True):
    if train:
        y_pred= clf.predict(x_train)
        print(f"Accurancy_score: {accuracy_score(y_train,y_pred)* 100:.2f}%")
    elif train== False:
        
        pred= clf.predict(x_test)
        print(f"Accurancy_score: {accuracy_score(y_test,pred)* 100:.2f}%")
        
        print(classification_report(y_test,pred,digits=2))
        
        


# In[41]:


clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)


# In[42]:


metric_score(clf,x_train,x_test,y_train,y_test,train=True)
metric_score(clf,x_train,x_test,y_train,y_test,train=False)


# In[45]:


feuture_name=list(x.columns)
class_a=list(y_train.unique())
feuture_name


# In[60]:



grid_param={'criteria' :['gini','entropy'],
     'max':range (10,15),
     'min_sample':range(2,3)}


# In[61]:



grid_search=GridSearchCV(estimator=clf,
                        param_grid=grid_param,
                        cv=5,
                         n_jobs=1)


# In[63]:


grid_search.fit(x_train,y_train)


# In[ ]:




