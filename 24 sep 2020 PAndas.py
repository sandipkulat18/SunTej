#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[ ]:





# In[12]:


row={'company':['google','IBM','Qxpree'],
    'Project':['first','2nd','3rd'],
    'sale':[23,34,44]}
df=pd.DataFrame(row, columns=['company','Project','sale'])
df


# In[10]:


row
# Hiracle iNdexing


# In[13]:


df.set_index(['company','Project'],drop=False)
# index butleave columns inplace


# In[14]:


df.set_index(['company','Project'],drop=True,inplace=True)
df
#column replace


# In[17]:


df.swaplevel('company','Project')
# swap the colummn name


# In[19]:


df.sum(level='company')
# sum of company


# In[20]:


df.sum(level='Project')


# In[21]:


df.mean(level='Project')


# In[22]:


#DAta Manupulaation


# In[23]:


titanic_train= pd.read_csv("https://raw.githubusercontent.com/training-ml/Files/main/titanic_train.csv",sep=',')


# In[42]:


titanic_train


# In[43]:


titanic_train.to_csv(r'D:\Software\Sandip\titic_train_copy.csv',index=False,header=True)


# In[44]:


titanic_train.head()


# In[48]:


titanic_train.drop(['Unnamed: 0'],axis=1,inplace= True)
titanic_train.head()


# In[58]:


titanic_train['Survived'].unique()


# In[63]:


titanic_train['Survived'].replace({0:'Died',1:'Survived'},inplace=True)


# In[64]:


titanic_train['Survived'].head()


# In[65]:


titanic_train.head()


# In[66]:


# Similary you can replace category data set
dd=pd.crosstab(titanic_train['Survived'],titanic_train['Sex'],margins=True)
dd


# In[73]:


cc=pd.crosstab(titanic_train['Sex'],titanic_train['Pclass'],margins=True)
cc


# In[69]:


titanic_train.shape


# In[71]:


# Find The Missing Value from  column 
age_mis=titanic_train[titanic_train['Age'].isnull()]
age_mis


# In[72]:


age_mis=titanic_train[titanic_train['Age'].isna()]
age_mis


# In[74]:


age_mis=titanic_train[titanic_train['Age'].notnull()]
age_mis


# In[76]:


titanic_train[titanic_train.Age.isin([25])]
#finf perticular Age data


# In[77]:


# find the all value is not 0
age_mis=titanic_train[titanic_train['Age'].notnull()]
age_mis


# In[88]:


# finding the MAx and Min


# In[92]:


max(titanic_train["Fare"])


# In[93]:


max_= titanic_train[titanic_train.Fare==max(titanic_train['Fare'])]
max_


# In[87]:


titanic_train.head()


# In[91]:


#multiple candito
class_female= titanic_train[titanic_train.Pclass.isin([1]) & titanic_train.Sex.isin(['female'])]
class_female


# In[95]:


max_fare= titanic_train[titanic_train.Fare.isin([max(titanic_train['Fare'])])]
max_fare


# # Series malupulation

# In[96]:


import pandas as pd
import numpy as np


# In[98]:


ser= pd.Series(data=[1,2,3,4],index=['C1','C2','C3','C4'])
ser


# In[107]:


print("\nIndesing by name (positinal value in the Series)\n",'-'*30,sep='')
print('Value for C2 in ser 1: ', ser['C1'])
print('Value for C2 in ser 1: ', ser['C2'])


# In[110]:


ser


# In[111]:


ser[1:4]


# In[119]:


ser1= pd.Series(data=[1,2,3,4],index=['C1','C2','C3','C4'])
ser2= pd.Series(data=[5,26,6,7],index=['C1','c2','D3','C4'])


# In[120]:


print('Ser 1 \n',ser1)
print("*"*30)
print('Ser 2 \n',ser2)


# In[124]:


ser3= ser1+ser2
print('\nAfter Additin two series, the result look like.. \n','-'*50)
print(ser3)
print('\nPython tries to add value wher it find common name index , keep where nan not match')


# # DataFrame Manipulation

# In[126]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')


# In[129]:


matriz_data=np.matrix('22,23,140;23,332,22;12,23,34;44,34,43;36,3,33')
row_label=['Raju','pandey','Sunil','Ashok',"Ganesh"]
column_heading=['Age','Height','Weight']


# In[131]:


df=pd.DataFrame(data=matriz_data, index=row_label,columns=column_heading)
print("\nA new Dataframe\n","*"*50,sep='')
print(df)


# In[132]:


print("\nThe 'Height' column\n","*"*50,sep='')
print(df['Height'])


# In[135]:


print("\nThe 'Height' and Weight column indexed by paasing list\n","*"*50,sep='')
print(df[['Height','Weight']])


# In[138]:


Only=df[["Height","Weight"]]
Only


# In[139]:


df.Age


# # Slicing perticular Element

# In[140]:


df


# In[141]:


df.loc['Raju']


# In[144]:


df.iloc[0]


# In[143]:


print(df)


# In[147]:


print(df.loc['pandey','Height'])


# In[149]:


df.loc['Ganesh',['Height','Weight']]


# In[153]:


df.loc[['Sunil','Ashok'],['Height','Weight']]


# In[154]:


df


# # Select the Condition

# In[158]:


print(df[df['Height']>65])


# In[162]:


boot1=df['Height']>30
boot2=df['Weight']>40


# In[167]:


print(df[(boot1) & (boot2)])


# In[168]:


selected_cond=df[boot1][["Age",'Weight']]


# In[171]:


print(selected_cond)


# In[172]:


df


# In[173]:


df.reset_index()


# In[174]:


df.reset_index(drop=True)


# In[176]:


df['Profession']='Student Teacher Engineer traner instrutor '.split()
df


# In[178]:


print(df.set_index('Profession'))


# In[ ]:




