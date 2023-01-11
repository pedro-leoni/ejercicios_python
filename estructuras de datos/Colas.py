#!/usr/bin/env python
# coding: utf-8

# # COLAS , siempre se atiende al primero que llego , a diferencia de las pilas que van al reves

# In[1]:


from collections import deque


# In[3]:


colas = deque()


# In[4]:


colas


# In[5]:


type(colas)


# In[6]:


colas = deque(['alvaro','estudiantes','familia','genios'])


# In[7]:


colas


# In[8]:


colas.pop()


# In[9]:


colas.popleft()


# In[10]:


# pop left es la funcionalidad que no podemos usar en pilas y si en colas, desapilar al primero con popleft


# In[ ]:




