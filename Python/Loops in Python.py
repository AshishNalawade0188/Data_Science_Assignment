#!/usr/bin/env python
# coding: utf-8

# #While Loop
# 
# 

# In[4]:


python = 5

while python > 0:
    print(f"Mi shiktoy re baba {python} vela ")
    python = python - 1
print("Shiklo re baba")


# In[6]:


age = 15 

while age < 18:
    print(f"You are still {age} pehle bade ho jao")
    age = age + 1
print("Tum kr skte ho kar do")


# In[10]:


#Range in Python
list(range(1,20))

#list is used to print the range and range function is used to create the range of values 


# In[11]:


list(range(1,20,2))


# In[15]:


for i in range (12,15):
    print(i)


# In[18]:


list = []

for i in range(1,15):
    list.append(i)
    


# In[19]:


list


# In[21]:


for i in range(1,6):
    print(i**2)


# In[22]:


#Company list

company = ["Flipkart","Amazon","ExcelR"]


# In[23]:


for i in company:
    print("www."+i+".com")


# In[29]:


# Write a program to create a list with the words starting with a

name = ["abhishek","atharva","kunal","riddhesh"]

for i in name:
    if i.startswith('a'):
        print(i)


# In[33]:


# Take a list of numbers and add 5 to each number

num = [1,56,65,657,64]

for i in num:
    print(i+5)


# In[36]:


# Create a list of marks and print only marks grater then 75

marks = [65,85,32,56,95]

for i in marks:
    if i > 75:
        print(i)


# In[ ]:




