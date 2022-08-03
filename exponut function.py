#!/usr/bin/env python
# coding: utf-8

# In[23]:


secert_word = "sandip"
guess = " "
guess_count =0
guess_limit =3

out_of_gussess = False

while guess != secert_word and not(out_of_gussess):
    if guess_count < guess_limit:
        guess=input ("enter gussess :")
        guess_count +=1
    else :
        out_of_gussess = True
if out_of_gussess :
    print("out of gussess, YOU LOSE!!")
else:
    print("YOU WIN !!")


# In[34]:


secert_word= "sandip"
guess =" "
guess_count=0
guess_limit=5
out_of_guessess = False

while guess != secert_word and not(out_of_guessess):
    if guess_count < guess_limit:
        guess=input("enter guessess :")
        guess_count +=1
    else:
        out_of_guessess = True
if out_of_guessess:
    print("out of guessess, You Lose !!")
else:
    print("You Win!!")


# In[42]:


def raise_of_power(base_num , pow_num):
    result = 1
    for index in range(pow_num):
        result=result * base_num
    return result
print(raise_of_power (3,4))


# In[ ]:





# In[ ]:




