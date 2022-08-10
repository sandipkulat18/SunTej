#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sqlite3
db =sqlite3.connect("my.database1.db")
db.execute("drop table if exists grades1")
db.execute("create table grades1(id int,name text ,score int)")


# In[10]:


db.commit()


# In[13]:


db.execute("insert into grades1(id,name,score) values(101,'sandip',99)")
db.execute("insert into grades1(id,name,score) values(102,'sachin',98)")
db.execute("insert into grades1(id,name,score) values(103,'Ganesh',97)")
db.execute("insert into grades1(id,name,score) values(104,'Rahul',96)")


# In[14]:


db.commit()


# In[17]:


result = db.execute("select * from grades1 order by id")
for row in result:
    print(row)
print("*" *60)


# In[18]:


result = db.execute("select * from grades1 where name = 'Ganesh' ")
for row in result:
    print(row)
print("*" *60)


# In[25]:


result = db.execute("select * from grades1 where score >= 99")
for row in result:
    print(row)
print("*" *60)


# In[28]:


result = db.execute("select id ,name from grades1 order by score desc ")
for row in result:
    print(row)
print("*" *60)


# In[ ]:




