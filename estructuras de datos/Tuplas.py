#!/usr/bin/env python
# coding: utf-8

# # tuplas
# son como listas pero inmutables, no se puede modificar su contenido

# In[1]:


t = ('pedro', 'leoni', 'estudiantes', 10, [1,2,8], 10, -80)


# In[2]:


t


# tienen en comun con las listas la indexacion y el slicing

# In[3]:


t[0]


# In[4]:


t[3]


# In[6]:


t[4:]


# In[7]:


len(t)


# In[9]:


t[0] = 'los estudiantes'


# aqui vemos como python nos prohibe asignar un item en un elemento del tipo tuple

# In[10]:


t.index('estudiantes')


# FUNCION INVERSA AL INDICE JEJEEJEJEJEJEJEJEJEJ EPICO, YA SABES PARA QUE USARLA COCHINOTE 

# In[11]:


t.index('tumami')


# In[12]:


t.count(10)


# contamos los 10, efectivamente tenemos 2 (siempre mirar la tupla t declarada arriba)

# In[ ]:




