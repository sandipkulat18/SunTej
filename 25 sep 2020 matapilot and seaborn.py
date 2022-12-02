#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy.random as randn


# In[21]:


df=pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
df


# In[22]:


df.head(3)


# In[23]:


df.plot.bar()
plt.show()


# In[24]:


df.plot(kind= 'bar')


# In[25]:


df.plot.barh()


# In[26]:


iris=sns.load_dataset('iris')


# In[ ]:


iris.head()


# In[ ]:


iris.sepal_lenght.plot(kind='hist')


# In[ ]:


iris.sepal_lenght.plot(kind='hist',bins= 30)


# In[27]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[35]:


emp={'Age':[10,20,29,20,20,20,2,2,20],'Salary':[23,34,34,22,34,33,34,12,23]}


# In[36]:


df=pd.DataFrame(data=emp)
df


# # Box plot

# plt.figure(figsize=(5,6))
# ax=sns.boxplot(data=df)
# plt.yticks(range(5,60,5))
# plt.xlabel('Age and Salary')
# plt.show()

# In[40]:


plt.figure(figsize=(5,6))
ax=sns.boxplot(data=df) 
plt.yticks(range(5,60,5))
plt.xlabel('Age and Salary')
plt.show()


# In[41]:


df.plot(kind='box',figsize=(8,7),color='r',yticks=range(0,55,5))

#another Way


# In[42]:


sal=[10,23,45,51,23,34,23,23,12]
sal.sort()
sal


# # Outliers

# In[43]:


import pandas as pd
import numpy as np


# In[44]:


ser=pd.Series(sal)


# In[45]:


ser


# In[46]:


ser1=pd.DataFrame(ser)
ser1


# In[48]:


q1=ser.quantile(0.25)
print('Q1',q1)
#iqr= inter qualine range
q3=ser.quantile(0.75)
print('Q3',q3)
iqr= q3-q1
print('IQR',iqr)


# In[49]:


# formula
#upper site=Q3+(1.5*IQR)
#lower_side= Q1-(1.5*IQR)


# In[53]:


upside=q3+ (1.5*iqr)
upside


# In[54]:


lowside=q1-(1.5*iqr)
lowside


# In[55]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas.plotting import scatter_matrix


# In[57]:


iris=sns.load_dataset('iris')
df= iris.drop(['species'],axis=1)
df.head()


# In[61]:


scatter_matrix(df,figsize=(10,8),color='b',diagonal='kde')
plt.show()
#kernal density estimation=kde


# In[62]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas.plotting import scatter_matrix


# In[63]:


ruppes=[1222,3444,900,15000,1500]
fees=['Tution fees','Mobile Bill','Elecrticity','Rent','Misc']


# In[66]:


plt.pie(x=ruppes,labels=fees)
plt.show()


# In[71]:


plt.figure(figsize=(8,8))
plt.pie(x=ruppes,labels=fees,explode=[0,0.1,0.5,0,0],autopct='%.2f',rotatelabels=True)
plt.show()


# # Seaborn Numric data Ploting

# In[72]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas.plotting import scatter_matrix


# In[73]:


tips=sns.load_dataset('tips')
tips.tail()


# In[75]:


sns.relplot(x='total_bill',y='tip',data=tips)
plt.show()


# In[77]:


tips['smoker'].value_counts()


# In[78]:


tips.shape


# In[79]:


sns.relplot(x='total_bill',y='tip',data=tips,size='size')
plt.show()


# In[80]:


sns.scatterplot(x='total_bill',y='tip',data=tips,size='size')
plt.show()


# In[83]:


sns.relplot(x='total_bill',y='tip',data=tips,hue='smoker',style='time')
plt.show()


# In[84]:


sns.lineplot(x='total_bill',y='tip',data=tips)
plt.show()


# In[85]:





# In[ ]:




