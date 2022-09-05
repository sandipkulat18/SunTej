#!/usr/bin/env python
# coding: utf-8

# In[3]:



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


# In[4]:


bank=Account()


# In[5]:


bank.login()


# In[29]:


class User_Account(Account):
    pass
    def __init__(sandip,Account_num, Balance, *args):
        super(User_Account,sandip).__init__(*args)
        sandip.Account_num= Account
        sandip.Balance= Balance
    def user_details(sandip):
        while True:
            account= int (input('enter your bank account :'))
            if account == sandip.Account_num:
                print('Name = ', sandip.name)
                print('Account Number =', sandip.Account_num)
                print('current Balance =',sandip.Balance)
                break
            else:
                ('Account number is invalide')
                continue
    def deposite(sandip):
        print('Your previous balance =',sandip.Balance)
        add_cash= int(input('Deposite cash ='))
        sandip.Balance += add_cash
        print('\n HDFC bank : Rs ',add_cash, 'Deposite to your account = ', andip.Account_num, 
              'and Your current balance = ',sandip.Balance)
        
    def transfer(sandip):
        print('Your previous balance =',sandip.Balance)
        withdrown_cash= int(input('Deposite cash ='))
        if withdown_cash <= sandip.Balance:
            sandip.Balance -= withdrown_cash
            print('\n HDFc bank : Rs ', withdrown_cash, 'Deposite to your account =', sandip.Account_num, 
              'and Your currenr balance = ',sandip.Balance)
        else:
            print("\n Alret : Hello boss, you don't have sufficient balance" )
        
        
        
        


# In[ ]:


bank_details= User_Account(55555,0)


# In[ ]:


bank_details.login()


# In[ ]:


bank_details.user_details()


# In[31]:


bank_details.deposite()


# In[ ]:




