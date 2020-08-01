#!/usr/bin/env python
# coding: utf-8

# In[5]:


#QUESTION 1
import re 

def isValid(s): 
    

    # 2) They contains 7 or 8 or 9. 

    # 3) Then contains 9 digits 

    Pattern = re.compile("[7-9][0-9]{9}") 

    return Pattern.match(s) 


s =input("Enter the mobile no :-")

if (isValid(s)):  

    print ("Valid Number")      

else : 

    print ("Invalid Number")


# In[2]:


#Question 2
user1 = ["aman","raj","ayush","gracie"]

user2 = ["akshay","rakesh","raj","ram"]

#Merging the given two lists
user_list = user1+ user2


#creating a function to remove the duplicates
#the list is converted into dictionary using the list values as keys and then again
#converting them back into a list which will remove the duplicates
def my_function(x):
  return list(dict.fromkeys(x))

new_list = my_function(user_list)

print(new_list)

