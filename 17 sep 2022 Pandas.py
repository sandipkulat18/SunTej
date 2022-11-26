#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')


# In[2]:


ser=pd.Series()
ser


# In[5]:


ser=pd.Series([0,10,20,30,40,50])
ser


# In[8]:


ser=pd.Series([20,15.7,'10'])


# In[9]:


ser


# In[10]:


dict= {'A':[1,2,3],'B':[3,4,5],'C':[6,7,8]}


# In[11]:


df=pd.DataFrame(dict)
df


# In[15]:


df['D']='one Two Ten'.split()
df


# In[16]:


df['E']=[10,20,30]
df


# In[18]:


dict= {'A':[1,2,np.nan],'B':[3,np.nan,np.nan],'C':[6,7,8]}


# In[19]:


dict


# In[26]:


df1 =pd.DataFrame(dict)


# In[27]:


df1


# In[29]:


print('\nDropping any column with a NAN value\n','-'*35,sep='')
print(df1.dropna(axis=1))


# In[30]:


print('\nDropping any row with a NAN value\n','-'*35)
print(df.dropna(axis=0))


# In[31]:


df


# In[32]:


print('\nDropping value with default value\n','-'*35,sep='')
print(df.fillna(value=50))


# In[33]:


df


# In[35]:


df.fillna(value=df['C'].mean(),inplace=True)
df


# In[41]:


DATA={'company':['goog','goog','micro','micro','fb','fb'],
     'person':['sam','sandip','sachin','ganesh','yash','om'],
     'sale':[200,100,540,200,400,988],
      'profit':[40,24,60,45,34,76]}


# In[42]:


df=pd.DataFrame(DATA)
df


# In[51]:


avg_sale=df.groupby('company',as_index=False)['sale'].mean()
avg_sale


# In[47]:


total_sale=df.groupby('company')[['sale','profit']].sum()
total_sale


# In[45]:


state_sale=df.groupby('company'),[['sale','profit']].sum()
state_sale


# In[48]:


state_sale=df.groupby('company')[['sale','profit']].agg(['mean','sum'])
state_sale


# In[55]:


df.groupby('company')['sale'].nlargest(1)


# In[53]:


df.groupby('company')['sale'].nsmallest(1)


# In[58]:


class_a=pd.DataFrame({'math':[10,20,30],
                     'eng':[20,40,40],
                     'marathi':[50,59,50]},
                    index=['ravi','om','ganesh',])

class_a


# In[61]:


class_b=pd.DataFrame({'math':[40,40,30],
                     'eng':[30,40,40],
                     'marathi':[50,59,50]},
                    index=['ravi','om','ganesh',])

class_b


# In[65]:


class_c=pd.DataFrame({'math':[40,40,30],
                     'eng':[30,40,40],
                     'alegebra':[50,59,50]},
                    index=['ravi','om','ganesh',])

class_c


# In[70]:


all_student=pd.concat([class_a,class_b,class_c],axis=0)
print('\nAfter concont along with row \n','-'*50,sep='')
all_student


# In[71]:


payer_id= pd.DataFrame({'ID':[10,20,30,40,50,60,70],
                      'name':['virat','rohit','rahul','ms','bumrah','messi','ronaldo']})
payer_id


# In[76]:


payer_detl= pd.DataFrame({'ID':[10,20,30,40,50,],
                          'age':[30,34,21,34,21],
                          'country':['india','france','uprope','itali','londan',]})
payer_detl


# In[77]:


pd.merge(payer_id,payer_detl, on = 'ID')


# In[86]:


left= pd.DataFrame({'A':['A0','A1','A3'],
                     'B':['B0','B1','B2']},
                    index=['K0','K1','K2'] )
left


# In[90]:


right= pd.DataFrame({'C':['C0','C1','C3'],
                     'D':['D0','D1','D2']},
                    index=['K0','K1','K2'] )


# In[91]:


right


# In[92]:


left.join(right)


# In[93]:


left.join(right,how='outer')


# In[94]:


df=pd.DataFrame({'Dept':[1,2,3,4,5,],
                'Name':['sandip','sachin','rahul','ganesh','om'],
                 'salary':(23000,34444,542123,53123,34567)
                        }
                        )
df


# In[97]:


def salary_hike(x):
    if(x >30000):
        return np.ceil(x+(x* .30))
    else:
        return np.ceil(x+(x* 1.5))


# In[98]:


df['New_salary']=df['salary'].apply(salary_hike)
df


# In[99]:


df['incresed_sal']=df['New_salary']-df['salary']
df


# In[109]:


print("MAx and MIn column 'New_salary' Are : ",df['New_salary'].min(), 'And',df['New_salary'].max())


# In[103]:


df['New_salary'].sum()


# In[104]:


df.columns


# In[105]:


i=list(df.columns)


# In[106]:


i


# In[ ]:




