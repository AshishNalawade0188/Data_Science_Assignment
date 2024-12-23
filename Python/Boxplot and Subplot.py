#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Box plot
# !pip install plotly is the command will be used to install the library 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = (10,5)
plt.rcParams['figure.dpi'] = (350)

df = pd.read_csv('cars.csv')


# In[6]:


df.describe()


# In[15]:


plt.boxplot(df['engine-size'], vert = False, notch = True, showmeans = True )
plt.show

# notch is true to show median line and showmeans will show the mean in plot


# In[14]:


df.boxplot()


# In[31]:


sns.set_theme(style = 'dark', palette = 'viridis')

sns.boxplot(df['highway-mpg'])


# In[28]:


sns.boxplot(df['price'], orient = 'h')


# In[21]:


df['make'].unique()


# In[22]:


df[df['price'] > 30000]


# In[24]:


sns.boxplot(x = df['price'], y = df['make'])


# In[30]:


# Plotly Library

import plotly.express as pe
pe.box(df['price'], orientation='h')


# In[38]:


# Subplot and subplots

plt.subplot(2,2,1)
sns.boxplot(df['highway-mpg'])
plt.title('Outlier Detection')

plt.subplot(2,2,2)
sns.scatterplot(x = df['engine-size'], y = df['price'])
plt.xlabel('Engine-Size')
plt.ylabel('Price')
plt.title('Scatter plot')

plt.subplot(2,2,3)
sns.histplot(df['price'])

plt.subplot(2,2,4)
df['body-style'].value_counts().plot(kind = 'pie', autopct = '%0.0f%%')

plt.tight_layout()


# In[50]:


fig, index = plt.subplots(2,2)   # fig will store empty canvas and index will store the index numbers

sns.histplot(x = df['width'], ax = index[0,0])
sns.countplot(x =df['body-style'], ax = index[0,1])
sns.distplot(x = df['engine-size'], ax = index[1,0])
sns.scatterplot(x = df['width'],y = df['price'], ax = index[1,1])

plt.tight_layout()

# Here ax is inbulit function used for the indexing of particular chart number


# In[ ]:




