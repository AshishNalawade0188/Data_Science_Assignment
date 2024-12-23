#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing pandas

import pandas as pd


# In[2]:


# creating a dataframe with the help of dictionry

df = pd.DataFrame({
    'Name' : ['Abhishek','Atharva','Riddhesh'],
    'Age' : [21,20,22],
    'Subject Name' :['ML','DL','Python'],
    'Location' : ['Pune','Mumbai','Satara']
})


# In[3]:


df


# In[4]:


# Extracting th records of dataframe
df.Age  # Approch-1



# In[5]:


df['Subject Name']  #Approch-2


# In[6]:


# Load Externel file in jupytrt notebook\

df = pd.read_csv(r'E:\Data Science\Datasets\Salaries.csv')


# In[7]:


df


# In[8]:


# Reading first 5 records

df.head()


# In[9]:


df.head(25)


# In[10]:


df.tail()


# In[11]:


# Extracting only clolumn names

df.columns


# In[12]:


df.shape   # number of rows and columns


# 

# In[13]:


df.ndim # dimnensions


# In[14]:


df[['rank']]


# In[15]:


df[['rank','gender','salary']]


# In[16]:


# Descriptive stats of df

df.describe()


# In[17]:


df.describe(include=object)


# In[18]:


df.describe(include='all')


# In[19]:


df.info()


# In[20]:


df.dtypes


# In[21]:


# Extract records from 30 to 35 from service column to salary column 
# loc stands for label location
# it allows to put column names

df.loc[30:35,'service':'salary']


# In[22]:


# iloc stands for integer location uses only row numbers and column numbers in attribute
# iloc function excludes the last value in the atribute like [30:35] 35 would be excluded

df.iloc[30:35,3:6]


# In[23]:


# Extract the 5th and 18th row from rank and ahd column 

df.loc[[5,18]]


# In[24]:


df.loc[[5,18],['rank','phd']]


# In[25]:


# Unique values and their frequency 

df['rank'].unique()


# In[26]:


df['gender'].unique()


# In[27]:


df['rank'].nunique()


# In[28]:


df['rank'].value_counts()


# # Pandas filtering and groupby

# In[29]:


# Extract recordes where gender is female

df['gender'] == 'Female'


# In[30]:


df[df['gender']=='Female']  #Masking


# In[31]:


# Gender is female and salary is greater then 150000

df[(df['gender']=='Female') & (df['salary']>150000)]


# In[32]:


# What is the average salary of rank professor

df[df['rank'] == 'Prof']['salary'].mean()


# In[33]:


# Average salary of professor and gernder is male

df[(df['rank'] == 'Prof') & (df['gender'] == 'Female')]['salary'].mean()


# In[34]:


# Groupby Aggregate method

df.groupby('rank')['salary'].mean()


# In[35]:


df.groupby('gender')['salary'].mean()


# In[36]:


df.groupby('rank')['salary'].agg({'mean','median','min','max'})  # agg can only be used with groupby


# # Inclass Activity

# In[37]:


df = pd.read_csv(r'E:\Data Science\Datasets\nba.csv')


# In[38]:


df


# In[39]:


# Extract the data where team is boston celtics and weight is less then 100

df[(df['Team'] == 'Boston Celtics') & (df['Weight'] > 100.0)]


# In[40]:


# What is the average salary of players of team 'Los Angles Lakers'

df[df['Team'] == 'Los Angeles Lakers']['Salary'].mean()


# In[41]:


# What is the average salary of players based on various positions

df.groupby('Position')['Salary'].mean()


# In[49]:


# Which Player belongs to San Deigo Saint College

df[df['College'] == 'San Deigo State']


# In[46]:


# Which player from Torrento Raptors has maximum Salary

df[df['Team'] == 'Toronto Raptors']['Salary'].max()


# In[47]:


df[(df['Team'] == 'Toronto Raptors') & (df['Salary'] == 13600000.0)]


# # Introduction to Numpy

# In[50]:


# Why array are faster then list in python


# In[51]:


# Importing the library 

import numpy as np


# In[55]:


# Ceate arrays with varioud dimensions

a = np.array([1,2,3,4,5])  # Every sqaure bracket defines a dimension

a


# In[56]:


type(a)


# In[57]:


a.ndim


# In[60]:


b = np.array([1,'Ábhi',True])

b


# In[61]:


a = np.array([1,2,98,65], dtype = float)

a


# # Array Creation methods
# 
# 1.arange 
# 2.linspace 
# 3.random

# In[67]:


# arange function

x = np.arange(1,51) #last number excluded
x


# In[70]:


# linspace function : used to generate specified numbers in the given range with same difference
# retstat is used to show the difference between two numbers

y = np.linspace(5,20,50,retstep=True)  # last mumber included

y


# In[72]:


# random function : used to generate the random numbers

z = np.random.rand(5,2)

z


# In[73]:


np.random.randn(5,5)


# In[75]:


a = np.random.random_sample(200)


# In[78]:


# Aggregate Functions

a.sum()


# In[77]:


a.min()


# In[ ]:




