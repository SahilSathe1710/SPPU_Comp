#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv(r"C:\Users\HP\Downloads\archive (2)\emails.csv")


# In[3]:


df


# In[4]:


df.info()


# In[5]:


df.shape


# In[6]:


df.size


# In[7]:


df.isnull()


# In[8]:


df.isnull().sum()


# In[11]:


df.dtypes


# In[12]:


df.describe()


# In[14]:


X = df.iloc[:, 1:3001]
X


# In[23]:


Y = df.iloc[:, -1]
Y


# In[24]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.4)


# In[25]:


X_train


# In[26]:


X_test


# In[27]:


Y_train


# In[28]:


Y_test


# In[29]:


from sklearn.svm import SVC
svm = SVC()
svm.fit(X_train, Y_train)
prediction_svm = svm.predict(X_test)


# In[30]:


prediction_svm


# In[31]:


from sklearn.metrics import accuracy_score
acc_svm = accuracy_score(prediction_svm, Y_test)


# In[32]:


acc_svm


# In[33]:


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X_train, Y_train)
prediction_knn = knn.predict(X_test)


# In[34]:


prediction_knn


# In[35]:


from sklearn.metrics import accuracy_score
acc_knn = accuracy_score(prediction_knn, Y_test)


# In[36]:


acc_knn


# In[ ]:




