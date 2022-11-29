#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[64]:


db=sqlite3.connect("salary_det.db")


# In[65]:


cursor=db.cursor()


# In[66]:


cursor.execute("CREATE TABLE student_det(phone_number INT PRIMARY KEY, student_name TEXT, enrolled_date int, marks INT)")


# In[67]:


with open ('sql_copy.csv', 'r') as file:
    no_record = 0
    for row in file:
        cursor.execute("INSERT INTO student_det VALUES(?,?,?,?)",row.split(","))
        db.commit()
        no_record +=1
print (no_record,'Record Instrted","\n')


# In[73]:


df=cursor.execute('select * from student_det')
print(df)


# In[34]:





# In[68]:


cursor.execute('select * from student_det')
df=pd.DataFrame(cursor.fetchall())
print(df)


# In[69]:


cursor.description


# In[77]:


list(df.columns)


# In[ ]:


df.


# In[71]:


df=pd.DataFrame(cursor.fetchall())
print(df)


# In[75]:





# In[76]:


list(df.columns)


# In[ ]:




