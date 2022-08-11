#!/usr/bin/env python
# coding: utf-8

# In[45]:


class person:
    def __init__(self,name,surname,year_of_birth):
        self.name=name
        self.surname= surname
        self.year_of_birth=year_of_birth
    def age(self,current_year):
        return current_year - self.year_of_birth
    def __str__(self):
        return "%s %s was born in %d ." %(self.name,self.surname,self.year_of_birth)
    


# In[49]:


alec = person("allec", "Baldwin",1994)


# In[50]:


print(alec)


# In[51]:


print(alec.age(2022))


# In[ ]:





# In[ ]:




