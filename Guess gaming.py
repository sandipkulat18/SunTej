#!/usr/bin/env python
# coding: utf-8

# In[11]:
secert_word="sandip"
guess =""

guess_count=0
guess_limit =3

out_of_guessess= False
while guess != secert_word and not(out_of_guessess):
    if guess_count < guess_limit:
        guess= input(" enter guess :")
        guess_count =guess_count + 1
    else:
        out_of_guessess = True
if out_of_guessess:
    print("Out of Guesses, You Lose!!")
else:
    print("You Win !!")
