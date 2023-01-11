#!/usr/bin/env python
# coding: utf-8

# In[1]:


diccionario = {'alvaro':'chirou', 'pedro':'leoni'}


# In[2]:


diccionario


# In[3]:


type(diccionario)


# In[4]:


diccionario['alvaro']


# In[6]:


diccionario[1]


# no puedo llamar por indice

# In[7]:


del(diccionario['alvaro'])
diccionario


# con del eliminamos 

# In[8]:


edades_estudiantes = {'estudiante':20, 'otros':30}


# In[9]:


edades_estudiantes


# In[10]:


edades_estudiantes['estudiante']+=1


# In[11]:


edades_estudiantes


# In[12]:


edades_estudiantes['estudiante']+edades_estudiantes['otros']


# In[13]:


# sumamos los 2 grupos


# In[15]:


for edades in edades_estudiantes:
    print(edades)


# In[16]:


for edades in edades_estudiantes:
    print(edades,edades_estudiantes[edades])


# In[18]:


# diccionario{'valores':'claves','valores':'claves'}
# edades es declarado en el for


# In[19]:


lista = []


# In[20]:


lista.append(edades_estudiantes)


# In[21]:


lista


# In[22]:


edades_estudiantes = {'agregando':2, 'alalistaanterior':'rrocasa'}


# In[23]:


lista.append(edades_estudiantes)


# In[24]:


lista


# In[25]:


### en este caso vamos agregando los diccionarios a la variable lista 


# In[ ]:




