#!/usr/bin/env python
# coding: utf-8

# In[5]:


knights = {'gallahad': 'the pure','robin':'the brave'}


# In[6]:


for k, v in knights.items():
    print(k,v)
    


# In[9]:


for i, v in enumerate(['tic','tac','toe']):
    print(i,v)
    


# In[10]:


#loop lebih dari 2 list bersamaan zip()
questions = ['name','quest','favorite color']
answers = ['lancelot','the holy grail','blue']
for q,a in zip(questions, answers):
    print('What is your {0}? It is {1}.'.format(q,a))
    


# In[11]:


#loop dengan reversed
for i in reversed(range(1,10,2)):
    print(i)


# In[13]:


#loop disebuah list yang disorting menggunakan sorted()
basket = ['apple','orange','apple','pear','orange','banan']
for f in sorted(set(basket)):
    print(f)


# In[16]:


import math
raw_data = [56.2, float('NaN'), 51.7,55.3,52.5,float('NaN'),47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
    

filtered_data


# In[ ]:




