#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


ipl=pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/matches.csv')
ipl


# In[24]:


ipl1=pd.read_csv(‪'r''D:\matches.csv')
ipl1


# In[19]:


ipl.head()


# In[20]:


ipl.tail()


# In[27]:


ipl.sample(n=7)


# In[33]:


L=pd.set_option('display.max_rows',None)
L


# In[34]:


ipl.shape


# In[35]:


type(ipl)


# In[41]:


excel=pd.read_excel(r'Rosa - DATA.xlsx',sheet_name='Rosa -IPD')
excel


# In[42]:


ipl.to_csv("ipl_copy.csv")


# In[45]:


ipl.to_csv(r"D:\Software\Sandip\ipl_copy.csv",index=False,header=True)


# In[54]:


url="https://www.basketball-reference.com/leagues/NBA_2015_totals.html"


# In[55]:


bb_data=pd.read_html(url)


# In[57]:


bb_data[0].head()


# In[59]:


bb_data[0].shape


# In[60]:


bb_data[0].columns


# In[65]:


selected =bb_data[0][['Rk','Pos','AST']].head()


# In[64]:


bb_data[0][['Rk']].head()


# In[66]:


selected


# In[67]:


selected.head()


# In[68]:


import numpy as np


# In[76]:


date_range=pd.date_range('4/12/2021',periods=12,freq="M")
dates=pd.DataFrame(date_range,columns=['Dates'])


# In[77]:


dates


# In[73]:


dates['Day']=dates['Date'].dt.day
dates['Month']=dates['Date'].dt.month
dates['Year']=dates['Date'].dt.year
dates


# In[79]:


df=pd.DataFrame({'DATE_TIME':['Jan 1 12:00 am','Jan 1 12:00 am'  ]})
df


# In[81]:


df['Date']=pd.to_datetime(df['DATE_TIME'],format='%b %d %I:%M %p')
df


# In[82]:


df.drop['Date']
df


# In[84]:


#Data Cleaning


# In[86]:


val1=np.array([1,np.nan,7,1,8])
val1


# In[87]:


6+ np.nan


# In[88]:


7*np.nan


# In[ ]:





# In[89]:


np.nansum(val1)


# In[91]:


val1


# In[92]:


np.nansum([6,np.nan])


# In[94]:


raw={'Name':['sandip',np.nan,'rahul'],
     'Age':[21,np.nan,34],
     'sex':['m','f',np.nan]}


# In[96]:


df=pd.DataFrame(raw,columns=['Name','Age','sex'])
df


# In[97]:


df.isnull().sum()


# In[98]:


df.isna().sum()


# In[100]:


df.notnull().sum()


# In[102]:


df_no_missing=df.dropna()


# In[103]:


df_no_missing


# In[104]:


df


# In[105]:


df_clean=df.dropna(how='all')


# In[106]:


df_clean


# In[107]:


df['Final_Score']=np.nan
df


# In[108]:


df.dropna(axis=1,how='all')


# In[111]:


df['Age'].fillna(df['Age'].mean(),inplace=True)
df


# In[112]:


df['sex'].fillna(df['sex'].mean(),inplace=True)
df


# In[113]:


df.fillna(method=ffill)


# In[114]:


df


# In[116]:


df.loc[1]=['Yash',34,'m',45]
df


# In[ ]:




