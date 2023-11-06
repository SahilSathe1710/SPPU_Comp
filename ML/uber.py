#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[4]:


df=pd.read_csv(r"C:\Users\HP\Downloads\archive (1)\uber.csv", encoding = 'unicode_escape')


# In[5]:


df


# In[9]:


df.isnull()


# In[11]:


df.dropna(inplace=True)


# In[12]:


df.isnull().sum()


# In[13]:


col=['fare_amount']
df.boxplot(col)


# In[14]:


df.corr(numeric_only=True)


# In[17]:


X = df.iloc[:, 4:8]
X


# In[22]:


Y = df.iloc[:, 2:3]
Y


# In[25]:


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3)


# In[26]:


X_train


# In[27]:


X_test


# In[28]:


Y_train


# In[29]:


Y_test


# In[35]:


from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train, Y_train)
prediction_lr = lr.predict(X_test)


# In[36]:


prediction_lr


# In[37]:


from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators = 5, random_state = 100)
rf.fit(X_train, Y_train)
prediction_rf = rf.predict(X_test)


# In[38]:


prediction_rf


# In[39]:


from sklearn.metrics import mean_squared_error
rmse_lr = np.sqrt(mean_squared_error(prediction_lr, Y_test))
rmse_rf = np.sqrt(mean_squared_error(prediction_rf, Y_test))


# In[40]:


rmse_lr


# In[41]:


rmse_rf


# In[43]:


from sklearn.metrics import r2_score
r2_lr = r2_score(prediction_lr, Y_test)
r2_rf = r2_score(prediction_rf, Y_test)


# In[44]:


r2_lr


# In[45]:


r2_rf


# In[ ]:




