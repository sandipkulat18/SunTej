#!/usr/bin/env python
# coding: utf-8

# In[30]:


def salary_incre(Fixed_sal,House_rent):
    total_sal=(Fixed_sal+House_rent)
    bonus= 1000
    if total_sal <=9000:
        return total_sal + bonus
    
    else:
        return total_sal

    


# In[32]:


print('your new salary=', salary_incre(6500,2000))
    


# In[22]:


cube(9*)


# In[35]:


def cube(num):
    return num*num*num
cube(4)


# In[59]:


def used_car(car_year,car_brand,kilometer):
    if car_year ==2020:
        if 10000 < kilometer <=15000:
            if car_brand =='Honda Amez' :
                print('Rs 6,50,000 to Rs 7,50,000')
            elif car_brand =='Honda creta' :
                print('Rs 8,50,000 to Rs 9,50,000')
            else:
                print('No stck availble right know, please visit later')
                
        elif  15000 < kilometer <=25000:
            if car_brand =='Honda Amez' :
                print('Rs 5,50,000 to Rs 6,00,000')
            elif car_brand =='Honda creta' :
                print('Rs 7,50,000 to Rs 8,50,000')
            else:
                print('No stck availble right know, please visit later')
        else:
            ('no Stock')
            
    elif car_year ==2021:
        if 10000 < kilometer <=15000:
            if car_brand =='Honda Amez' :
                print('Rs 7,50,000 to Rs 8,50,000')
            elif car_brand =='Honda creta' :
                print('Rs 8,50,000 to Rs 9,0,000')
            else:
                print('No stck availble right know, please visit later')
        else:
            ('No stck availble right know, please visit later')
    else:
        ('sorry don not keep cars older 2020')


# In[60]:


used_car(2019,'Honda amez',22000)


# In[64]:


## Lambada ##


# In[ ]:


lambda 


# In[65]:


add= lambda y : y +30
add(50)


# In[66]:


print(add(50))


# In[71]:


multi_num = lambda x,y : x*y
multi_num(20,49)


# In[72]:


multi_num(20,49)


# In[76]:


####### *arg and **kwargs


# In[81]:


def fun(*args):
    for i in args:
        print('my args: - ', i)


# In[82]:


fun("india",45,"benguluru",30.45,3030)


# In[86]:


def func(**kwargs):
    for c, d in kwargs.items():
        print(c,'=',d)


# In[87]:


func(student=['sandip','sachin','ganesh'],age=[30,27,26])


# In[90]:


def grace (marks):
    if marks ==33 :
        print(marks + 2)
    elif marks ==32:
        print(marks + 3)
    elif marks == 34:
        print(marks + 1)
    else:
        return marks
grace(35)


# In[92]:


def grace (marks):
    if marks ==33 :
        return(marks + 2)
    elif marks ==32:
        return (marks + 3)
    elif marks == 34:
        return (marks + 1)
    else:
        return marks
grace(32)


# In[93]:


score=[32,50,33,34,90,45,12,34]


# In[94]:


total= list(map(grace,score))


# In[95]:


total


# In[96]:


total.count(35)


# In[112]:


def fun(marks):
    if marks < 35:
        return marks


# In[113]:


score=[32,50,33,34,45,34]


# In[115]:


list(map(lambda var: var%2 == 0, [1,2,3]))


# In[116]:


list(filter(lambda var: var%2 == 0, [1,2,3]))


# In[120]:


extra= 10


# In[121]:


def total ():
    print('print inside function', 35 + extra)


# In[123]:


tatal()


# In[124]:


print('print inside function', 35 + extra)


# In[127]:


def total_score():
    same=30
    print('print inside function', 50 + same)


# In[128]:


total_score()


# In[129]:


def local_global():
    global var12
    var12 = "this is fantastic"
    print(var12)
    


# In[130]:


local_global()


# In[131]:


print(var12)


# In[ ]:




