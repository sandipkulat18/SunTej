#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sqlite3
db =sqlite3.connect("my.database1.db")
db.execute("create table Emp_data(emp_Id int,Salary int, gender text ,age int)")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100001,20200,'M', 25) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100002,30200,'F', 35) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100003,45200,'M', 20) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100004,20600,'M', 35) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100005,90200,'F', 47) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100006,70200,'M', 50) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100007,15200,'M', 24) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100008,4520,'F', 25) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(100009,345600,'M', 52) ")
db.execute("insert into Emp_data (emp_Id,Salary,gender,age) values(1000010,874200,'F', 32) ")


# In[4]:


db.commit()


# In[12]:


result= db.execute("select * from Emp_data order by emp_Id ")
for row in result:
    print(row)
print("-"* 40)


# In[16]:


result= db.execute("select * from Emp_data where gender = 'M' ")
for row in result:
    print(row)
print("-"* 40)


# In[19]:


result= db.execute("select * from Emp_data where age >=35 ")
for row in result:
    print(row)
print("-"* 40)


# In[21]:


result= db.execute("select salary, age from Emp_data order by salary desc ")
for row in result:
    print(row)
print("-"* 40)


# In[ ]:




