#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[13]:


df= pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/cardio_train.csv', sep=";")
df.head()


# In[14]:


df.shape


# In[59]:


df.to_csv('D:\sandip\Cardio.csv')


# In[15]:



df.describe()


# In[16]:


df.drop ('id',axis=1,inplace= True)
df.drop_duplicates(inplace=True)


# In[17]:



plt.figure(figsize=(20,15))
plotnumber= 1
for column in df[['age','height','ap_hi','weight','ap_lo']]:
    if plotnumber<= 6:
        ax=plt.subplot(3,2,plotnumber)
        sns.distplot(df[column])
        plt.xlabel(column,fontsize=20)
        
    plotnumber +=1
plt.tight_layout()


# In[18]:


from scipy.stats import zscore
z_score=zscore(df[['age','height','ap_hi','weight','ap_lo']])
ads_z_score=np.abs(z_score)
filtering_entry=(ads_z_score< 3).all (axis=1)
df=df[filtering_entry]
df.describe()


# In[19]:



df.head()


# In[20]:


df.shape


# In[21]:


df.head()


# In[22]:


x=df.drop(columns=['cardio'],axis=1)
y=df['cardio']


# In[23]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=41)


# In[31]:


def metric_score(clf,x_train,x_test,y_train,y_test,train=True):
    if train:
        y_pred=clf.predict(x_train)
        
        print('\=============Train Result=================')
        
        print(f'Accurancy Score: {accuracy_score(y_train,y_pred)*100:.2f}%')
        
        
    elif train== False:
        pred=clf.predict(x_test)
        
        print('\=============Train Result=================')
        
        print(f'Accurancy Score: {accuracy_score(y_test,pred)*100:.2f}%')
        
        print('\n \n Test clarssification Report \n', classification_report(y_test,pred,digits=2))


# In[32]:


random_clf=RandomForestClassifier()
random_clf.fit(x_train,y_train)


# In[33]:


metric_score(random_clf,x_train,x_test,y_train,y_test,train=True)
metric_score(random_clf,x_train,x_test,y_train,y_test,train=False)


#     #parameter using of gridsearch

# # random forest calssifire
# params={'n_estimators':[13,15],
#        'criterion':['entropy','gini'],
#        'max_depth':[10,15],
#        'min_samples_split':[10,11],
#        'min_samples_leaf':[5,6]
#        }
# 
# grd=GridSearchCV(random_clf,param_grid=params)
# grd.fit(x_train,y_train)
# 
# print('best Params=>',grd.best_params_)

# In[39]:


random_clf=grd.best_estimator_


# In[40]:


random_clf.fit(x_train,y_train)


# In[41]:


metric_score(random_clf,x_train,x_test,y_train,y_test,train=True)
metric_score(random_clf,x_train,x_test,y_train,y_test,train=False)


# # Roc AUC curve 

# In[43]:


from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve,roc_auc_score
from sklearn.metrics import plot_roc_curve


# In[49]:


lr= LogisticRegression()
kn=KNeighborsClassifier()
dt=DecisionTreeClassifier()
rf= RandomForestClassifier()


# In[50]:


x=df.drop(columns=['cardio'],axis=1)
y=df['cardio']
    
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.25,random_state=41)

lr.fit(x_train,y_train)
kn.fit(x_train,y_train)
rf.fit(x_train,y_train)
dt.fit(x_train,y_train)

print('All models are trained')


# In[51]:


lr.score(x_test,y_test)
kn.score(x_test,y_test)
dt.score(x_test,y_test)
rf.score(x_test,y_test)

print('All  models are test score captured')


# # RoC AUC curve for  fitted  models

# In[52]:


disp= plot_roc_curve(dt,x_train,y_train)
plot_roc_curve(lr,x_train,y_train,ax=disp.ax_)
plot_roc_curve(kn,x_train,y_train,ax=disp.ax_)
plot_roc_curve(rf,x_train,y_train,ax=disp.ax_)

plt.legend(prop={'size':10},loc='lower right')
plt.show()


# In[54]:


disp= plot_roc_curve(dt,x_test,y_test)
plot_roc_curve(lr,x_test,y_test,ax=disp.ax_)
plot_roc_curve(kn,x_test,y_test,ax=disp.ax_)
plot_roc_curve(rf,x_test,y_test,ax=disp.ax_)

plt.legend(prop={'size':11},loc='lower right')
plt.show()


# In[62]:


import pandas as pd
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

import warnings
warnings.filterwarnings('ignore')


# In[88]:


data=pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/boston_house_rent.csv')


# In[89]:


data.to_csv("D:\sandip\house_csv")


# In[90]:


data.shape


# In[91]:


data.head()


# In[92]:


data.isnull().sum()


# In[93]:


data.describe()


# In[94]:


corr=data.corr()
corr.shape


# In[95]:


corr


# In[96]:


plt.figure(figsize=(12,10))
sns.heatmap(corr,annot=True)
plt.show()


# # Seems RAD AND TAX correleted

# In[97]:


plt.scatter(data.TAX,data.RAD)
plt.xlabel('TAX')
plt.ylabel('RAD')
plt.title('TAX VS RAD')
plt.show()


# In[98]:


x=data.drop(columns=['PRICE'],axis=1)
y=data['PRICE']


# In[99]:


from sklearn.model_selection import train_test_split


# In[100]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=100)


# # ADABoost model REgreation

# In[101]:


from sklearn.ensemble import AdaBoostRegressor


# In[102]:


ada=AdaBoostRegressor()


# In[103]:


ada.fit(x_train,y_train)


# In[104]:


y_pred=ada.predict(x_train)


# In[105]:


y_pred[:6]


# In[106]:


accuracy= metrics.r2_score(y_train,y_pred)
print('R Square Score :',accuracy)


# In[107]:


y_test_pred=ada.predict(x_test)


# In[108]:


accuracy= metrics.r2_score(y_test,y_test_pred)
print('R Square Score :',accuracy)


# # HYperparameter turning  using Randamized serch cv

# In[109]:


from sklearn.model_selection import RandomizedSearchCV


# In[116]:


params={'n_estimators':[47,50,60,70],'learning_rate':[0.25,0.30,0.40]}


# In[117]:


rnd_srch=RandomizedSearchCV(AdaBoostRegressor(),cv=5,param_distributions=params)


# In[118]:


rnd_srch.fit(x_train,y_train)


# In[119]:


rnd_srch.best_estimator_


# In[121]:


ada=AdaBoostRegressor(learning_rate=0.25,n_estimators=62)
ada.fit(x_train,y_train)
y_pred=ada.predict(x_test)

print('*** accurancy post tuning *****')
print(metrics.r2_score(y_test,y_pred))


# # GBDT=Gradient Booested Tree

# In[132]:


import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# In[147]:


row=pd.read_csv('Heart.csv')


# In[148]:


row.to_csv("D:\Sandip\Heart.csv")


# In[149]:


row.head


# In[150]:


row.describe()


# In[151]:


row.head()


# In[153]:


row.drop('Unnamed: 0.1',axis=1,inplace=True)
row.head()


# In[154]:


row.drop('Unnamed: 0',axis=1,inplace=True)
row.head()


# In[155]:


row.describe()


# In[156]:


row.isnull().sum()


# In[158]:


row.drop('target',axis=1).corrwith(row.target)


# In[159]:


row.drop('target',axis=1).corrwith(row.target).plot(kind='bar',grid=True,figsize=(10,7),
                                                   title="correletion with target")
plt.show()


# In[160]:


from sklearn.feature_selection import SelectPercentile, chi2


# In[162]:


X= row.drop(['target'],axis=1)
y=row.target
SPercentile=SelectPercentile(score_func=chi2,percentile=80)
SPercentile=SPercentile.fit(X,y)


# In[166]:


cols=SPercentile.get_support(indices=True)
print("Feuture index =",cols)
features=X.columns[cols]
print('Feuture =',list(features))


# In[167]:


row_score=pd.DataFrame({'features':X.columns,'Chi2Score':SPercentile.scores_,'pValue':SPercentile.pvalues_})
row_score.sort_values(by="Chi2Score",ascending=False)


# In[168]:


X=row[features]


# In[169]:


y=row.target


# In[170]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# In[172]:


scaler=StandardScaler()
X_scaler=scaler.fit_transform(X)
x_train,x_test,y_train,y_test=train_test_split(X_scaler,y,test_size=0.3,random_state=42)


# In[173]:


from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report,accuracy_score


# In[178]:


def metric_score(clf,x_train,x_test,y_train,y_test,train=True):
    if train:
        y_pred=clf.predict(x_train)
        
        print('\=============Train Result=================')
        
        print(f'Accurancy Score: {accuracy_score(y_train,y_pred)*100:.2f}%')
        
        
    elif train== False:
        pred=clf.predict(x_test)
        
        print('\=============Train Result=================')
        
        print(f'Accurancy Score: {accuracy_score(y_test,pred)*100:.2f}%')
        
        print('\n \n Test clarssification Report \n', classification_report(y_test,pred,digits=2))


# In[179]:


gbdt_clf=GradientBoostingClassifier()
gbdt_clf.fit(x_train,y_train)


# # metric_score(gbdt_clf,x_train,x_test,y_train,y_test,train=True)
# metric_score(gbdt_clf,x_train,x_test,y_train,y_test,train=False)

# In[180]:


metric_score(gbdt_clf,x_train,x_test,y_train,y_test,train=True)
metric_score(gbdt_clf,x_train,x_test,y_train,y_test,train=False)


# #Hyperparameter tuning 

# In[181]:


from sklearn.model_selection import GridSearchCV


# In[185]:


grid_param={'max_depth':range(4,8),
           'min_samples_split': range(2,8,2),
           'learning_rate':np.arange(0.1,0.3)}


# In[186]:


grid=GridSearchCV(GradientBoostingClassifier(),param_grid=grid_param)
grid.fit(x_train,y_train)


# In[187]:


grid.best_params_


# In[188]:


gbdt_clf=GradientBoostingClassifier(max_depth=8,
                                   min_samples_leaf=2,learning_rate=0.2)


# In[189]:


gbdt_clf.fit(x_train,y_train)


# In[190]:


metric_score(gbdt_clf,x_train,x_test,y_train,y_test,train=True)
metric_score(gbdt_clf,x_train,x_test,y_train,y_test,train=False)


# #XGBOOSt 

# In[199]:





# In[ ]:




