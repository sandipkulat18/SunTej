#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Ensemble Technique


# In[ ]:


# Bagging Classfier


# In[1]:


from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
import warnings
warnings.filterwarnings('ignore')


# In[3]:


from sklearn.datasets import load_breast_cancer
dataset= load_breast_cancer()
x= dataset.data
y=dataset.target


# In[4]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y, random_state= 4)


# In[5]:


knn= KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
knn.score(x_test,y_test)


# In[25]:


bag_knn=BaggingClassifier(KNeighborsClassifier(n_neighbors=5),
                         n_estimators=9,max_samples=0.7,
                         bootstrap=True,random_state=3,oob_score=True
                         )


# In[26]:


bag_knn.fit(x_train,y_train)
bag_knn.score(x_test,y_test)


# In[ ]:





# In[27]:


Pasting_knn =BaggingClassifier(KNeighborsClassifier(n_neighbors=5),
                         n_estimators=9,max_samples=0.7,
                         bootstrap=False, random_state=3)


# In[29]:


Pasting_knn.fit(x_train,y_train)
Pasting_knn.score(x_test,y_test)


# In[ ]:





# In[ ]:


# random Forest


# In[30]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# prepocessing normalize
from sklearn.preprocessing import  StandardScaler
#models
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
# metrics
from sklearn.metrics  import accuracy_score, confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[31]:


df= pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/cardio_train.csv', sep=";")
df.head()


# In[32]:


df.shape


# In[33]:


df.describe()


# In[34]:


df.drop ('id',axis=1,inplace= True)
df.drop_duplicates(inplace=True)


# In[36]:


df.shape


# In[38]:


plt.figure(figsize=(20,15))
plotnumber= 1
for column in df[['age','height','ap_hi','weight','ap_lo']]:
    if plotnumber<= 6:
        ax=plt.subplot(3,2,plotnumber)
        sns.distplot(df[column])
        plt.xlabel(column,fontsize=20)
        
    plotnumber +=1
plt.tight_layout()


# In[42]:


from scipy.stats import zscore
z_score=zscore(df[['age','height','ap_hi','weight','ap_lo']])
ads_z_score=np.abs(z_score)
filtering_entry=(ads_z_score< 3).all (axis=1)
df=df[filtering_entry]
df.describe()


# In[43]:


df.head()


# In[ ]:




