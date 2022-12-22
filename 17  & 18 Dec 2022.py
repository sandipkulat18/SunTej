#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


dataset = pd.read_csv('https://raw.githubusercontent.com/training-ml/Files/main/Mall_Customers.csv')


# In[4]:


dataset.head()


# In[5]:


dataset.to_csv('D:\sandip\mall.csv')


# In[10]:


x=dataset[['Annual Income (k$)','Spending Score (1-100)']]
x.head()


# In[12]:


from sklearn.cluster import KMeans

wcss=[]
for i in range (1,11):
    kmeans=KMeans(n_clusters=i, random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number Of cluster')
plt.ylabel('WCSS')
plt.show()
    


# In[13]:


dataset.shape


# In[14]:


x.head()


# In[15]:


kmeans=KMeans(n_clusters=5, random_state=42)
y_kmeans=kmeans.fit_predict(x)
print(y_kmeans)


# # model Evalution

# In[16]:


from sklearn.metrics import silhouette_score


# In[17]:


silhouette_score(x,y_kmeans)


# In[18]:


x.head()


# # sample prediction

# In[19]:


test=kmeans.predict(np.asarray([[15,39]]))
test[0]


# In[20]:


cluster_4_customers=dataset[y_kmeans==4]
print(cluster_4_customers)


# In[46]:


plt.figure(figsize=(8,5))
plt.scatter(x[y_kmeans==0]['Annual Income (k$)'],x[y_kmeans==0]['Spending Score (1-100)'],s=100,c='red',label='Cluster 1')
plt.scatter(x[y_kmeans==1]['Annual Income (k$)'],x[y_kmeans==1]['Spending Score (1-100)'],s=100,c='blue',label='Cluster 2')
plt.scatter(x[y_kmeans==2]['Annual Income (k$)'],x[y_kmeans==2]['Spending Score (1-100)'],s=100,c='green',label='Cluster 3')
plt.scatter(x[y_kmeans==3]['Annual Income (k$)'],x[y_kmeans==2]['Spending Score (1-100)'],s=100,c='cyan',label='Cluster 4')
plt.scatter(x[y_kmeans==4]['Annual Income (k$)'],x[y_kmeans==4]['Spending Score (1-100)'],s=100,c='magenta',label='Cluster 5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centroids')
plt.title('Cluster Of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()


# In[48]:


plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,0],s=300,c='yellow',label='Centroids')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='Centroids')


# In[25]:


from sklearn.cluster import MiniBatchKMeans
minibatch_kmeans=MiniBatchKMeans(n_clusters=5)
minibatch_kmeans.fit_predict(x)


# In[28]:


import scipy.cluster.hierarchy as sch


# In[34]:


plt.figure(figsize=(20,6))
dendo=sch.dendrogram(sch.linkage(x,method='ward'))
#method= ward,average,complete,single
plt.title('Dendogram')
plt.xlabel('Customer data')
plt.ylabel('Eucl Distance')
plt.show()


# In[31]:


from sklearn.cluster import AgglomerativeClustering


# In[36]:


group =AgglomerativeClustering(n_clusters=3)
cluster=group.fit_predict(x)
print(cluster)


# In[37]:


from sklearn.metrics import silhouette_score
silhouette_score(x,cluster)


# In[38]:


customer_cluster_0= dataset[cluster==0]
customer_cluster_1= dataset[cluster==1]
customer_cluster_2= dataset[cluster==2]


# In[44]:


print(customer_cluster_2)


# # DBScan Culster

# In[ ]:





# In[ ]:


# density based  spatial  clustering  of applocation with noise


# In[49]:


import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler


# In[50]:


centers=[[1,1],[-1,-1],[1,-1]]
x, label_true=make_blobs(n_samples=750,centers=centers,cluster_std=0.4,random_state=0)


# In[51]:


x=StandardScaler().fit_transform(x)
x[:5]


# In[52]:


db=DBSCAN(eps=0.2,min_samples=3).fit(x)


# In[53]:


labels=db.labels_
print(labels)


# In[54]:


len(set(labels))


# In[56]:


1 if -1  in labels else 0


# In[57]:


n_clusters=len(set(labels))-(1 if -1  in labels else 0)
n_noise=list(labels).count(-1)


# In[58]:


print(n_clusters)
print(n_noise)


# # for demonstration purpose only

# In[ ]:


core_samlpe_mask=np.zeros_like(db.labels_)


# In[59]:


np.unique(labels,return_counts=True)


# In[60]:


noises=x[labels== -1]
print(noises)


# In[ ]:




