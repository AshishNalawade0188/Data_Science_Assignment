#!/usr/bin/env python
# coding: utf-8

# # Matplotlib
# 
# 

# Why Visualize ?
#  Important lib: 
#  1.matplotlib(2D)
#  2.seaborn(2D & more attratctive)
#  3.plotly(3D and interactive charts)

# In[13]:


#import library

import matplotlib.pyplot as plt    # pyplot is one of the module from many modules of matplotlib
import numpy as np
import pandas as pd


# # Line Plot

# In[14]:


x = np.linspace(1,20,25)
y = np.random.random_sample(25)


# In[15]:


x


# In[16]:


y


# In[17]:


plt.plot(x,y)


# In[18]:


# Setting graph parameters

plt.rcParams['figure.figsize'] = (10,5)    # This dimension will be applicable for complete jupyter notebook
plt.rcParams['figure.dpi'] = 500

# plt.figure(figsize = (20,12))  This can be used to give dimensions to the particular graph not all


# In[19]:


plt.plot(x,y)


# In[20]:


plt.plot(x, y, color = 'red', linestyle = ':')


# In[21]:


# Multiline Graph


# In[22]:


x = np.arange(1,21)

log = np.log(x)
sqrt = np.sqrt(x)

plt.plot(x,log, label = 'Log')
plt.plot(x,sqrt, label = 'Sqrt')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Line Graph')
plt.legend()    # It will Show all the lables when you use it, it is mandatory to use if lables are to be shown


# In[23]:


plt.figure(figsize = (20,15))

plt.plot(x,y)


# In[24]:


plt.plot(x,y)


# In[25]:


# Importing the dataset

df = pd.read_csv(r'E:\Data Science\Datasets\cars.csv')
df


# In[26]:


plt.hist(df['width'])  # Histogram of matplotlib library


# In[27]:


df['width'].skew()  # Function for Skewness


# In[28]:


df.hist()  #histogram of pandas library
plt.tight_layout()


# In[29]:


df['engine-size'].skew()


# In[30]:


# Median and mean

mean = df['width'].mean()
median = df['width'].median()


# In[31]:


plt.hist(df['width'], edgecolor = 'black')
plt.axvline(mean, color ='red')    # axv means axis vertical line , we also have axhline
plt.axvline(median, color = 'green')
plt.title('Frequency Graph for Width Column')


# In[32]:


import seaborn as sns


# In[33]:


#Countplot

df.head()


# In[34]:


sns.countplot(x = df['body-style'])


# In[35]:


import warnings
warnings.filterwarnings('ignore')


# In[37]:


# Pandas barplot

df['body-style'].value_counts().plot(kind = 'bar')


# In[38]:


barplot_df = df['body-style'].value_counts().plot(kind = 'bar')  # Calling functions usinng the pandas library

for i in barplot_df.containers:
    barplot_df.bar_label(i)


# In[54]:


sns.countplot(x = df['make'])
plt.xticks(rotation = 90)
plt.show


# In[39]:


# Pandas Pie chart

a = [10,65,95,65]
b = ['a','b','c','d']


# In[46]:


plt.pie(a, labels = b, autopct = '%0.0f%%')
plt.show  # Hides the extra comments appered in the output


# In[56]:


df['body-style'].value_counts()


# In[57]:


names = ['sedan','hatchback','wagon','hardtop','convertible']


# In[58]:


df['body-style'].unique()


# In[63]:


plt.pie(df['body-style'].value_counts(),labels = names , autopct = '%0.0f%%')
plt.show


# In[70]:


sns.set_theme(style = 'darkgrid' , palette = 'rainbow')


# In[68]:


# Pandas Pie Chart

df['body-style'].value_counts().plot(kind = 'pie', autopct = '%0.2f%%')


#  # Plotly

# In[71]:


# Histogram

import plotly.express as pe


# In[74]:


pe.box(df['width'])


# In[ ]:




