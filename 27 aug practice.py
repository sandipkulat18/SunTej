#!/usr/bin/env python
# coding: utf-8

# In[22]:


name= input("Enter your Name = ")
if name.isalpha():
    print("Enter Name = ", name)
else:
    print("please enter Alpha character.")


# In[50]:


def used_car(car_year,car_brand,kilometer):
    if car_year ==2020:
        
        if 10000 < kilometer <=15000:
            
            if car_brand =='Honda Amez' :
                print('Rs 6,50,000 to Rs 7,50,000')
            elif car_brand =='Honda creta' :
                print('Rs 8,50,000 to Rs 9,50,000')
            else:
                print('No stck availble right know, please visit later')

        elif 15000 < kilometer <=25000:
            if car_brand =='Honda Amez' :
                print('Rs 5,50,000 to Rs 6,00,000')
            elif car_brand =='Honda creta' :
                print('Rs 7,50,000 to Rs 8,50,000')
            else:
                print('No stck availble right know, please visit later')
        else:
            print('no Stock')

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
        print('sorry don not keep cars older 2020')


# In[52]:


car_man = int(input('please Enter Car Manufacture Year ?'))
km_driven= int(input('Please enter kilometer ?'))
car_bnd= input("enter Car brand ? ")
used_car(car_man,car_bnd,km_driven)


# In[39]:


car_man = int(input('please Enter Car Manufacture Year ?'))
km_driven= int(input('Please enter kilometer ?'))
car_bnd= input("enter Car brand ? ")
used_car(car_man,car_bnd,km_driven)


# In[46]:


mark1=int(input('enter marks'))
subject= input('data science')
mark2= int(input('enter marks'))


# In[47]:


try:
    total= mark1+ subject
except TypeError:
    print('you are adding interger and srting, please make sure both are same.')
else :
    print('you enter Total =', total)


# In[ ]:





# In[59]:


try:
    car_num= input('enter Number : ')
    name= input('Enter Your Name :')
    phone_num = input('enter your NUmber :')
    
    if car_num == '':
        raise exception()
    elif name == '':
        raise exception()
    elif phone_num == '':
        raise exception()
    else:
        pass
except:
    if car_num == '':
        print(' The registertion car number field is reuired. \n')
    if name =='':
        print(' The Customer name feild is required. \n')
    if phone_num == '':
        print(' The mobile number field is required.\n')
        
else:
    print('Thanks for all Details')


# In[63]:


##  block: finally ##

try:
    car_num= input('enter Number : ')
    name= input('Enter Your Name :')
    phone_num = input('enter your NUmber :')
    
    if car_num == '':
        raise exception()
    elif name == '':
        raise exception()
    elif phone_num == '':
        raise exception()
    else:
        pass
except:
    if car_num == '':
        print(' The registertion car number field is reuired. \n')
    if name =='':
        print(' The Customer name feild is required. \n')
    if phone_num == '':
        print(' The mobile numberfield is required.\n')
        
finally:
    print('In any case finally block will excute')


# In[76]:


def mobile_num ():
    try:
        val= int(input(' enter the mobile number = '))
    except:
        print('You did  not enter phone number please enter phone number')
    print(val)


# In[77]:


mobile_num()


# In[3]:


def mobile_num ():
    
    while True:
        
        
        try:
            
            val= int(input(' enter the mobile number = '))
            
        
            if len(str(val))!= 10:
                print('mobile number is must 10 Digit ')
                continue
            else:
                print('Thank you')
                break
        
        except:
            print('You did  not enter phone number please enter phone number')
            continue
            
        
        


# In[ ]:


mobile_num()


# In[93]:


san=7028728969
print(san)


# In[92]:


str(san)


# In[95]:


len(str(san))


# In[16]:


def mobile ():
    while True:
        try:
            name= input(' enter Your name = ')
            if name.isalpha():
                if name == 'sandip':
                    print('Thank you ')
                    break
                else:
                    print('Please enter correct name')
                    continue
        except:
            if int(input("")):
                
                print('You enter the integer, please enter alphabet')
                continue
            


# In[ ]:


mobile()


# In[ ]:


mobile()


# In[8]:


name= input ('enter your Name')
if name.isalpha():
        print('you enter name =',name)
else:
    print('please enter alphabet you are adding integer')


# In[ ]:


##sandip


# In[26]:


class Account:
    pass
    def __init__(sandip, name= input('enter your name = '),
                lastname =input('enter your lastname ='),
                city = input('enter your city ='),
                user_id= input('enter your User_id ='),
                password= input('enter your password ='),
               phone= input('enter your phone number =')):
        
        sandip.name= name
        sandip.lastname= lastname
        sandip.city= city
        sandip.user_id= user_id
        sandip.password= password
        sandip.phone= phone
        
    def login(sandip):
    
        while True:
            singin= input('enter your Email Id -')
            password = input('inpur Your password - ')
            if singin== sandip.user_id and password== sandip.password:
                print('successfully logged in')
                break
            else:
                print('user Id and password incorrect')
                continue
        


# In[33]:


bank=Account()


# In[34]:


bank.login()


# In[ ]:




