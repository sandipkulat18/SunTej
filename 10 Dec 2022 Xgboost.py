#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import  train_test_split, GridSearchCV

from sklearn.metrics import r2_score,mean_squared_error
import xgboost as xgb
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df= pd.read_csv('vehicles_data_students.csv')


# In[3]:


df.head()


# In[4]:


drop_columns=['Unnamed: 0','id','title_status','size','lat','long','county']
df=df.drop(columns=drop_columns,axis=1)


# In[5]:


get_ipython().system('pip install xgboost')


# In[6]:


df.shape


# In[7]:


import xgboost as xgb


# In[8]:


df.isnull().sum()


# In[9]:


df=df.dropna()
df.head(5)


# In[10]:


df.shape


# In[11]:


df.describe()


# In[12]:


df.drop_duplicates(inplace=True)


# In[13]:


df.shape


# In[15]:


numerics=['int8','int16','int32','int64','float16','float32','float64']
categorical_columns=[]

features=df.columns.values.tolist()

for col in features:
    if df[col].dtype in numerics:
        continue
    categorical_columns.append(col)
    


# In[16]:


categorical_columns


# # Endonding categories get Dumies

# In[18]:


df_dumies=pd.get_dummies(df[categorical_columns],drop_first=True)


# In[19]:


df_dumies.head()


# In[20]:


df_dumies.shape


# In[21]:


df=df.join(df_dumies)


# In[22]:


df.shape


# In[23]:


df.head()


# In[24]:


df.drop(columns=categorical_columns,axis=1,inplace=True)


# In[25]:


df.head(2)


# In[26]:


df.info


# In[27]:


df.describe()


# In[28]:


df=df[df['price']>1000]
df=df[df['price']<40000]


# In[29]:


df.shape


# In[30]:


y=df['price']
x=df.drop(['price'],axis=1)


# In[31]:


train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.25,random_state=10)


# # XGB

# In[35]:


import xgboost as xgb
xgb=xgb.XGBRegressor()
xgb.fit(train_x,train_y)


# In[36]:


y_pred=xgb.predict(test_x)


# In[37]:


r2_score(test_y,y_pred)


# # SVM

# In[40]:


#support  Vecotr machine


# In[42]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import  train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score
import  seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[60]:


df1=pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/breast%20cancer.csv',index_col=0)
df1.head()


# In[61]:


print(df1.shape)
print(df1.info())


# In[62]:


df1=df1.drop(['Unnamed: 32'],axis=1)


# In[63]:


df1.shape


# In[64]:


df1.describe()


# In[65]:


scaler=StandardScaler()
x=df1.drop('diagnosis',axis=1)
x_scaled=scaler.fit_transform(x)


# # priciple componut analysis

# In[66]:


pca=PCA()
pca.fit_transform(x_scaled)


# In[67]:


df1.to_csv('D:\sandip\df1.csv')


# In[69]:


plt.figure()
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Principal Components')
plt.ylabel('Variance Covered')
plt.title('PCA')
plt.show()


# In[70]:


pca=PCA(n_components=13)
new_pcomp=pca.fit_transform(x_scaled)
prici_comp=pd.DataFrame(new_pcomp,columns=['PC1','PC2','PC3','PC4','PC5','PC6','PC7','PC8','PC9','PC10','PC11','PC12','PC13'])
prici_comp


# In[71]:


df1['diagnosis']=df1['diagnosis'].replace({'M':1,'B':0})
y=df1['diagnosis']    


# In[72]:


x_train,x_test,y_train,y_test= train_test_split(prici_comp,y,test_size=0.25,random_state=335)


# In[90]:


# Metrics
def print_score(clf,x_train,x_test,y_train,y_test,train=True):
    if train:
        y_pred=clf.predict(x_train)
        
        print('\n-------Train Result--------')
        
        print(f'Accurancy score:{accuracy_score(y_train,y_pred)*100:.2f}%')
        
    elif train==False:
        pred=clf.predict(x_test)
        
          
        print('\n-------Train Result--------')
        
        print(f'Accurancy score:{accuracy_score(y_test,pred)*100:.2f}%')
        
        print(classification_report(y_test,pred,digits=2))
        
        


# In[87]:





# In[89]:


from sklearn.svm import SVC
svc=SVC()
svc.fit(x_train,y_train)
print_score(svc,x_train,x_test,y_train,y_test,train=True)
print_score(svc,x_train,x_test,y_train,y_test,train=False)


# In[91]:


from sklearn.ensemble import GradientBoostingClassifier
gbdt=GradientBoostingClassifier()


# In[92]:


gbdt.fit(x_train,y_train)
print_score(gbdt,x_train,x_test,y_train,y_test,train=True)
print_score(gbdt,x_train,x_test,y_train,y_test,train=False)


# In[93]:


from sklearn.ensemble import RandomForestClassifier
rf= RandomForestClassifier()


# In[94]:


rf.fit(x_train,y_train)
print_score(rf,x_train,x_test,y_train,y_test,train=True)
print_score(rf,x_train,x_test,y_train,y_test,train=False)


# # Hyper parameter Tunning

# In[95]:


from sklearn.model_selection import  GridSearchCV


# In[96]:


param_grid={'C':[1,5,10,20],
           'gamma':[0.001,0.01,0.02,0.002]}


# In[97]:


gridsearch=GridSearchCV(svc,param_grid)
gridsearch.fit(x_train,y_train)
gridsearch.best_params_


# In[100]:


svc=SVC(C= 5, gamma=0.02)
svc.fit(x_train,y_train)

print_score(svc,x_train,x_test,y_train,y_test,train=True)
print_score(svc,x_train,x_test,y_train,y_test,train=False)


# #Creating Pipline 

# # Creating Pipeline

# In[108]:


from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


# In[104]:


x=df1.drop(['diagnosis'],axis=1,)
y=df1.diagnosis

x_train,x_test,y_train,y_test= train_test_split(prici_comp,y,test_size=0.25,random_state=335)


# In[110]:


pipe=Pipeline([('Sacler',StandardScaler()),
              ('PCA',PCA(n_components=13)),
              ('SVM',SVC(C=7,gamma=0.01))])


# In[111]:


pipe.fit(x_train,y_train)


# In[112]:


y_pred=pipe.predict(x_test)


# In[113]:


accuracy_score(y_test,y_pred)


# In[ ]:




