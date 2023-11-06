#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv(r"C:\Users\HP\Downloads\archive (3)\diabetes.csv")


# In[5]:


df


# In[6]:


df.info()


# In[7]:


df.shape


# In[8]:


df.size


# In[9]:


df.isnull()


# In[10]:


df.isnull().sum()


# In[11]:


df.dtypes


# In[12]:


df.describe()


# In[13]:


X = df.iloc[:, 0:8]
X


# In[15]:


Y = df.iloc[:, -1]
Y


# In[16]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)


# In[17]:


X_train


# In[18]:


X_test


# In[19]:


Y_train


# In[20]:


Y_test


# In[21]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, Y_train)
prediction = knn.predict(X_test)


# In[22]:


prediction


# In[23]:


from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
cm = confusion_matrix(prediction, Y_test)


# In[24]:


cm


# In[25]:


acc = accuracy_score(prediction, Y_test)
acc


# In[28]:


prc = precision_score(prediction, Y_test)
prc


# In[29]:


rec = recall_score(prediction, Y_test)
rec


# In[ ]:




