#!/usr/bin/env python
# coding: utf-8

# In[1]:


basket = {'apple','orange','apple','pear','orange','banana'}


# In[2]:


print(basket)


# In[3]:


'orange' in basket


# In[4]:


'crabgrass' in basket


# In[5]:


a = set('abracadabra')
b = set('alacazam')


# In[6]:


a


# In[7]:


a - b


# In[8]:


a | b


# In[9]:


a & b


# In[10]:


a ^ b


# In[14]:


a = [x for x in 'abracadabra' if x not in 'abc']


# In[15]:


a


# In[ ]:




