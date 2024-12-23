#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = (10,5)
plt.rcParams['figure.dpi'] = 350

df = pd.read_csv('cars.csv')


# In[2]:


df


# In[3]:


# Seaborn Scatterplot

# How engine size affect price of the car
sns.scatterplot(x = df['engine-size'] , y = df['price'])


# In[4]:


# Plotting entire dataset

sns.pairplot(df)


# In[5]:


# How engine size and width are realtable to each other

sns.scatterplot(x = df['engine-size'], y = df['price'])


# In[6]:


# How engine style and body size affects price of cars

sns.set_style('darkgrid')
sns.scatterplot(x = df['engine-size'], y = df['price'], hue = df['body-style'], style = df['fuel-type'])

# Here hue and style are the parameters used to represent the categorical data in the plot.
# Their values will not be represented directly but instead they will use the color patterns and shape pattersns 


# In[7]:


import plotly.express as pe


# In[8]:


pe.scatter_3d(data_frame = df, x = 'width', y ='price', z ='engine-size', color='body-style')


# In[9]:


pe.scatter(data_frame = df, x = 'width', y = 'price', color ='engine-location')


# In[ ]:




