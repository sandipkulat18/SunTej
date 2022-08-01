#!/usr/bin/env python
# coding: utf-8

# In[14]:


first_number= input("enter first number:")
second_number =input("enter second number :")
first = int(first_number)
second= int(second_number)
print("---(-,+,/,*,%)-------")
operator= input("enter operator :")
      
if operator == "+":
    print(first + second)
elif operator == "-" :
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print (first / second)
elif operator == "%" :
    print(first % second)
else:
    print("invalid operation")
                   


# In[ ]:





# In[ ]:




