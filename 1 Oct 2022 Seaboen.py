#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas.plotting import scatter_matrix
import seaborn as sns


# In[4]:


tips=sns.load_dataset('tips')


# In[5]:


tips.head()


# # Categary data plot
# 

# In[6]:


#catplot()
#striplpt()
#swarmplot()
#countplot()


# In[7]:


sns.catplot(x='day',y='total_bill',data=tips)


# In[8]:


sns.swarmplot(x='day',y='total_bill',data=tips)


# In[10]:


sns.countplot(x='day',data=tips)


# In[11]:


plt.figure(figsize=(10,5))
plt.grid()
sns.countplot(x='size',hue='time',data=tips)
plt.yticks(range(0,110,10))
plt.show()


# In[14]:


sns.stripplot(x='size',y='total_bill',data=tips)
plt.show()


# In[15]:


sns.stripplot(x='smoker',y= 'total_bill',data=tips)
plt.show()


# In[19]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas.plotting import scatter_matrix
import seaborn as sns
from numpy.random  import randn


# In[20]:


import warnings
warnings.filterwarnings('ignore')


# In[21]:


x=randn(10000)


# In[24]:


x


# In[28]:


sns.distplot(x)
plt.show()


# In[29]:


sns.kdeplot(x)
plt.show()


# In[30]:


tips=sns.load_dataset('tips')
tips.tail()


# In[34]:


x=tips['total_bill']
y=tips['tip']


# In[35]:


sns.jointplot(x=x,y=y)


# # Regreation and Reletionsheep

# In[36]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import seaborn as sns


# In[37]:


tips=sns.load_dataset('tips')


# In[38]:


tips.head()


# In[39]:


sns.regplot(x='total_bill',y= 'tip',data=tips)
plt.show()


# In[40]:


sns.lmplot(x='total_bill',y= 'tip',data=tips)
plt.show()


# In[41]:


df=sns.load_dataset('mpg')
df


# In[ ]:


sns.load_dataset()

