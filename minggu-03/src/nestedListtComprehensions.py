#!/usr/bin/env python
# coding: utf-8

# In[1]:


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]


# In[3]:


#transpose kolom menjadi baris dan sebaliknya
[[row[i] for row in matrix] for i in range(4)]


# In[6]:


#transpose menggunakan for
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

transposed


# In[8]:


#transpose menggunakan for
transposed = []
for i in range(4):
    #3 baris impelementasi nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

transposed


# In[ ]:




