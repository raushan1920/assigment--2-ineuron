#!/usr/bin/env python
# coding: utf-8
create a pattern
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
# In[2]:



for i in range(0,6):
    for j in range(0,i):
        print("*",end="")
    print(" ")
for a in range(0,6):
       for b in range(-6,-a):
        print("*",end="")
    
       print(" ")

2. Write a Python program to reverse a word after accepting the input from the user.
Input word: ineuron
Output: norueni
# In[3]:


enter_name = input('enter name---')
print('reverse name---',enter_name[::-1])


# In[ ]:




