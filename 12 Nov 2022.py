#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import accuracy_score, confusion_matrix,roc_curve,roc_auc_score
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[2]:


data = pd.read_csv("diabetes.csv")


# In[3]:


data.head()


# In[ ]:


data.shape


# In[ ]:


data.describe()


# In[ ]:


plt.figure(figsize=(20,25),facecolor= 'red')
plotnumber =1
 
for column i data:
    if plotnumber <= 9:
        ax=plt.subplot(3,3,plotnumber)
        sns.distplot(data[column])
        plt.xlabel(column,fontsize=20)
        
    plotnumber += 1

plt.show

        


# In[ ]:


data['BMI']= data['BMI'].replace(0,data['BMI'].mean())
data['BloodPressure']= data['BloodPressure'].replace(0,data['BloodPressure'].mean())
data['Glucose']= data['Glucose'].replace(0,data['Glucose'].mean())
data['insulin']= data['Insulin'].replace(0,data['Insulin'].mean())
data['SkinThickness']= data['SkinThickness'].replace(0,data['SkinThickness'].mean())





# In[ ]:


plt.figure(figsize=(20,25))
plotnumber =1
for column in data:
    if plotnumber <= 9:
        ax= plt.subplot(3,3,plotnumber)
        sns.displot(data[column])
        plt.xlabel(column,fontsize=20)
    plotnumber +=1
plt.show()


# In[ ]:


df_feature= data.drop('Outcome',axis=1)


# In[ ]:


plt.figure(figsize=(20,25))
plotnumber =1
for column in df_feature:
    if graph <= 9:
        ax= plt.subplot(3,3,plotnumber)
        sns.displot(data=df_feature[column])
        plt.xlabel(column,fontsize=20)
    graph +=1
plt.show()


# In[ ]:


data.shape


# In[ ]:


q1=data.quantile (0.25)
q3=data.quantile(0.75)
iqr= q3-q1


# In[ ]:


preg_high=(q3.pregnacies + (1.5* iqr.pregnacies))
preg_high


# In[ ]:


index= np.where(data['pregnacies'])> preg_high)
index


# In[ ]:


data.reset_index()


# In[ ]:


index


# In[ ]:


x= data.drop(columns=['Outcome'])


# In[ ]:


plt.figure(figsize=(20,25))
plotnumber =1
for column in data:
    if plotnumber <= 9:
        ax= plt.subplot(3,3,plotnumber)
        sns.displot(data[column])
        plt.xlabel(column,fontsize=20)
    plotnumber +=1
plt.show()


# In[ ]:


scalar.StandardScalar()
X_scaled= scalar.fit_transform(X)


# In[ ]:


X_scaled.shape()


# In[ ]:


vif=pd.Dataframe()
vif["vif"]=[variance_inflation_factor(X_scaled, i ) for i range (X_scaled.shape[1])]
vif["features"]= X.columns

vif


# In[ ]:


log_reg= LogisticRegression()
log_reg.fit(x_train, y_train)


# In[ ]:


y_pred= log_reg.predict(x_test)


# In[ ]:


y_pred


# In[ ]:


accuracy= accuracy_score(y_test,y_pred)
accuracy


# In[ ]:


conf_mat=confusion_matrix(y_test,y_pred)
conf_mat


# In[ ]:


from sklearn.metrics import classification_report


# In[ ]:


print(classification_report(y_test,y_pred))


# In[ ]:


fpr,tpr,therholds=roc_curve(y_test,y_pred)


# In[ ]:




