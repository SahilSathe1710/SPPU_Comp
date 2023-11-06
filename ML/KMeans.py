#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv(r"C:\Users\HP\Downloads\archive (4)\sales_data_sample.csv", encoding = 'unicode_escape')


# In[4]:


df


# In[5]:


df.isnull()


# In[6]:


df.isnull().sum()


# In[7]:


df = df.select_dtypes(include = ["int64"])
df


# In[8]:


sse=[]
k_values=range(1,10)


# In[9]:


from sklearn.cluster import KMeans
for k in k_values:
    kmean=KMeans(n_clusters=k,n_init=10)
    kmean.fit(df)
    sse.append(kmean.inertia_)


# In[10]:


import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.plot(k_values, sse, marker="o")
plt.xlabel("Number of cluster")
plt.ylabel("SSE(Sum Of Square error)")
plt.grid()
plt.show()


# In[ ]:




