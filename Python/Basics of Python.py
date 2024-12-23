#!/usr/bin/env python
# coding: utf-8

# In[1]:


# variable in python 
10


# In[2]:


a =10


# In[3]:


id(a)  # Address of a


# In[4]:


_ten =10


# In[5]:


# for single line comment we use #

age = 60 #age variable contain 60 value

age


# In[6]:


# for multiple line comment we  use triple quote

'''this is first line
this is second line
this is third line'''


# In[7]:


age 


# In[8]:


print("my age is",age)  # Print statement in python


# - Operators in python
# 

# In[7]:


# Arithematic Operators

num1 = 2511
num2 = 321


# In[11]:


# Here in python we only get the last statements executed
   
num1+num2
num1-num2
num1*num2
num1/num2
num1%num2      


# In[8]:


# print function can show the outputs to many operations at one time

print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1%num2)    


# In[ ]:





# In[9]:


# Comparison Operators in Python

a = 85
b = 75


# In[10]:


a == b


# In[11]:


a != b


# In[12]:


a < b


# In[13]:


a > b


# In[18]:


a <= b


# In[ ]:


# Logical Operators in Python : AND, OR


# In[19]:


x = 10
y = 20


# In[21]:


x > y and x > 5


# In[22]:


x < y and x > 5


# In[23]:


x > y or x > 5


# In[24]:


# Identity operator in python : is, is not


# In[25]:


x,y


# In[27]:


x is y


# In[28]:


x is not y


# In[16]:


# Membership operators in Python : in, not in

course ='Data Science'


# In[17]:


's' in course


# In[18]:


' ' in course


# In[34]:


'y' not in course


# # Data Types in Python

# In[36]:


# Integer


# In[37]:


pin_code = 455156
pin_code 


# In[38]:


type(pin_code)


# In[39]:


temp=25.2
type(temp)


# In[40]:


logical=True
type(logical)


# In[41]:


# String creation


# In[50]:


s = 'we are learning python'
s1 = "we are learning python"
s2 = ''''we are learning python'''


# In[51]:


s==s1


# In[52]:


s==s2


# In[53]:


s==s1


# In[54]:


# Typecasting - is used to change the data types


# In[55]:


age
type(age)


# In[19]:


# String cannot be changed into other

x = str(age)
type(x) 


# In[57]:


float(age)


# In[59]:


zero = 0

bool(zero)


# In[61]:


bool(5)


# In[20]:


# String methods


# In[63]:


s


# In[65]:


s.capitalize() 


# In[66]:


#count


# In[69]:


s.count('a')


# In[71]:


print()


# In[21]:


# Starts with and endswith function


# In[73]:


s


# In[74]:


s.startswith('we')


# In[76]:


s.endswith('o')


# In[22]:


# find in python


# In[23]:


s


# In[79]:


s.find('we')


# In[80]:


# Replace in Python


# In[81]:


s.replace('we','They')


# In[83]:


s


# In[84]:


s = s.replace('we','They')


# In[85]:


s


# In[86]:


# Split in Python


# In[87]:


s


# In[90]:


s[0:4]


# In[91]:


len(s)


# In[92]:


s.split(' ')


# In[93]:


s2 = 'They', 'are', 'learning', 'python'
s2


# In[94]:


# Basic operations in Python


# In[95]:


s.upper()


# In[96]:


s.lower()


# In[97]:


s.swapcase()


# In[98]:


# Join in Python


# In[100]:


s 
'-'.join(s)


# In[101]:


email = 'abc@gmail.com'

email.split('@')


# 

# In[ ]:




