#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[8]:


db= sqlite3.connect('Employee_database.db')


# In[9]:


cursor= db.cursor()


# In[10]:


cursor.execute("create table student_data(phone_number INT Primary key,email_id TEXT,course_name TEXT,fee_paid INT)")


# In[11]:


cursor.execute("insert INTO student_data(phone_number ,email_id ,course_name,fee_paid)values(8928299289,'Student@gmail.com' ,'digitalmarketing', 24000)")
db.commit()
print(cursor.rowcount)


# In[25]:


result= cursor.execute("select * from student_data")
for row in result:
    print(row)


# In[41]:


with open ("Studentdata.csv","r") as file:
    no_record =0
    for row in file:
        
        cursor.execute("insert INTO student_data values ( ?,?,?,? )", row.split(","))
        db.commit()
        no_record += 1
print(no_record)


# In[42]:


result= cursor.execute("select * from student_data")
for row in result:
    print(row)


# In[44]:


sql = "select * from student_data where course_name= 'dS'"
result = cursor.execute(sql)
for row in result:
    print(row)


# In[45]:


sql = "select * from student_data where fee_paid= '24000' "
result = cursor.execute(sql)
for row in result:
    print(row)


# In[48]:


sql = "select * from student_data where fee_paid >'24000' "
result = cursor.execute(sql)
for row in result:
    print(row)


# In[50]:


sql = "delete from student_data where phone_number = 8928299290"
cursor.execute(sql)
db.commit()


# In[51]:


result= cursor.execute("select * from student_data")
for row in result:
    print(row)
    


# In[52]:


result= cursor.execute("select * from student_data order by fee_paid")
for row in result:
    print(row)
    


# In[87]:


sql = "update  student_data set fee_paid= 140000 where phone_number between 8928299467 and 8928299213"
cursor.execute(sql)
db.commit()


# In[91]:


result= cursor.execute("select * from student_data ")
for row in result:
    print(row)
    


# In[92]:


sql2 = "Update student_data set course_name= 'Developer' where phone_number between 8928299211 and 8928299213"
cursor.execute(sql2)

result= cursor.execute("select phone_number ,course_name from student_data where course_name= 'Developer'")
for row in result:
    print(row)


# In[ ]:



    


# In[80]:


print(row)


# In[95]:



result= cursor.execute("select  min(fee_paid) from student_data")
print("miniun fee" , result.fetchone())

result= cursor.execute("select  max(fee_paid) from student_data")
print("miximun fee" , result.fetchone())


# In[ ]:




