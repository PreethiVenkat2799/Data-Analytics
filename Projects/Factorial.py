#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial (num):
    if num == 1:
        return 1 
    else:
        return(num * factorial(num-1))


# In[3]:


factorial(5)


# In[ ]:




