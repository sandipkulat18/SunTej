#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings 
warnings.filterwarnings('ignore')


# In[2]:


import pandas as pd


# In[20]:


df = pd.DataFrame({'Salary':[24330,3400,45000,67770], 
            'City':['benguru','delhi','hydrabad','Goa'],
            'Gender':['male','Female','male','female'],
            'Exp':[1,2,3,None]})
df


# In[ ]:





# In[9]:


from sklearn.preprocessing import LabelEncoder


# In[11]:


lab_enc=LabelEncoder()


# In[16]:


df2= lab_enc.fit_transform(df['Gender'])
pd.Series(df2)


# In[18]:


df['Gender']=df2

df


# In[19]:


from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import make_column_transformer


# In[23]:


ohe= OneHotEncoder()
si = SimpleImputer()


# In[24]:


df = pd.DataFrame({'Salary':[24330,3400,45000,67770], 
            'City':['benguru','delhi','hydrabad','Goa'],
            'Gender':['male','Female','male','female'],
            'Exp':[1,2,3,None]})
df


# In[25]:


ct = make_column_transformer((ohe,['City','Gender']),
                            (si,['Exp']),
                            remainder = 'passthrough')


# In[30]:


encoded= pd.DataFrame(ct.fit_transform(df))
encoded


# In[35]:


encoded = pd.DataFrame(ct.fit_transform(df),columns= ['City_benguru','City_delhi','City_hydrabad','Gender_male','Gender_Female','Exp','Salary'])


# In[32]:


df


# In[33]:


df1=pd.get_dummies(df[['City','Gender']])
df1


# In[34]:


df1=pd.get_dummies(df[['City','Gender']], drop_first = True)
df1


# In[36]:


from sklearn.preprocessing import OrdinalEncoder


# In[39]:


import pandas as pd

Employee= pd.DataFrame({'Position':['SE','Manager','SSE','TL'],
                        'Project':['A','B','C','D'],
                        'Salary':[23000,25000.45000,None]})
Employee


# In[40]:


import pandas as pd

employee= pd.DataFrame({'Salary':[24330,3400,45000,67770], 
            'Project':['A','B','C','D'],
            'Position':['SM','SSE','manager','TL']})
employee


# In[42]:


ord_enc =OrdinalEncoder(categories=[['SM','SSE','manager','TL'],['A','B','C','D']])
encoded_df= ord_enc.fit_transform(employee[['Position','Project']])


# In[43]:


encoded_df


# In[48]:


import pandas as pd
df3 = pd.DataFrame({'Cat_data':['A','B','C','D','A','B','C','D']})
df3


# In[53]:



from sklearn.preprocessing import OneHotEncoder
from category.encoders  import BinaryEncoders


# In[57]:


pip install category.encoders


# In[59]:


from category.encoders  import BinaryEncoder


# In[52]:





# In[55]:


from sklearn.preprocessing import OneHotEncoder
from category.encoders  import BinaryEncoders


# In[60]:


import pandas as pd
df = pd.DataFrame({'Salary':[24330,3400,45000,67770], 
            'City':['benguru','delhi','hydrabad','Goa'],
            'Gender':['male','Female','male','female'],
            'Exp':[1,2,3,None]})
df


# In[61]:


from sklearn.impute import KNNImputer


# In[62]:


knnimp= KNNImputer(n_neighbors=2)
knn_imp= pd.DataFrame(knnimp.fit_transform(df[['Salary','Exp']]))


# In[63]:


knn_imp


# In[64]:


from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer


# In[65]:


df = pd.DataFrame({'Salary':[24330,3400,45000,67770], 
            'City':['benguru','delhi','hydrabad','Goa'],
            'Gender':['male','Female','male','female'],
            'Exp':[1,2,3,None]})
df


# In[66]:


iter_impute =  IterativeImputer()
iter_imp = pd.DataFrame(iter_impute.fit_transform(df[['Salary','Exp']]),columns= ['Salary','Exp'])


# In[67]:


iter_imp


# In[ ]:




