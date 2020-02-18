#!/usr/bin/env python
# coding: utf-8

# In[1]:


squares = []


# In[2]:


for x in range(10):
   squares.append(x**2)


# In[3]:


squares


# In[4]:


squares = list(map(lambda x: x**2, range(10))) #bentuk lain deklarasi list bil pangkat


# In[8]:


squares = [x**2 for x in range(10)] #bentuk lain deklarasi list bil pangkat


# In[9]:


[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y] #list baru kombinasi 2 elemen yang tidak sama


# In[10]:


#contoh lain
combs = []
for x in [1,2,3]:
    for y in [3,1,3]:
        if x != y:
            combs.append((x,y))
        
    
combs


# In[11]:


vec  = [-4,-2,0,2,4]


# In[12]:


#membuat list baru dari vec bernilai 2 kalinya
[x*2 for x in vec]


# In[13]:


#filter yang ditampilkan hanya yg bukan negatif
[x for x in vec if x >=0]


# In[14]:


#fungsi abs() ke semua elemen
[abs(x) for x in vec]


# In[15]:


#panggil method di setiap elemen
freshfruit = [' banana',' loganberry ','passion fruit ']
[weapon.strip() for weapon in freshfruit]


# In[17]:


#buat list 2 field kombinasi angka dan pangkatnya
[(x,x**2) for x in range(6)]


# In[18]:


#field harus pewarisan, jika tidak akan error
[x,x**2 for x in range(6)]


# In[19]:


#membuat list menggunakan listcomp dengan 2 for
vec = [[1,2,3],[4,5,6],[7,8,9]]
[num for elem in vec for num in elem]


# In[20]:


#list dengan complex expression dan fungsi
from math import pi
[str(round(pi,i)) for i in range(1,6)]


# In[ ]:




