#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=2  # Starting Point
lr=0.01  # Learning Rate
precision=0.00001  # Upto what decimal point or upto what precision
previous_step_size=1
max_iterator=1000 # how many iteration you want
iters=1
gf=lambda x: (x+3)**2


# In[2]:


gd=[]
while precision <previous_step_size and iters <max_iterator:
    prev=x
    x=x- lr * gf(prev)
    previous_step_size=abs(x-prev)
    iters=iters+1
    print(f"Iterators:{iters} value:{x}")
    gd.append(x)


# In[3]:


print("Local minima",x)


# In[4]:


import matplotlib.pyplot as plt
plt.plot(gd)


# In[ ]:




