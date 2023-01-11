#!/usr/bin/env python
# coding: utf-8

# In[1]:


con = {5,4,3}


# In[2]:


con


# In[3]:


con.add(2)


# In[4]:


con


# In[5]:


con.add(6)


# In[6]:


con


# ### un conjunto es una coleccion NO ORDENADA de objetos unicos
# el conjunto va siempre entre llaves, para ordenar utiliza su criterio interno
# ### para crear un conjunto vacio tenemos que escribir 
# #### con = set()

# In[7]:


con.add('H')


# In[8]:


con


# In[9]:


con.add('B')


# In[10]:


con.add('Y')


# In[11]:


con


# In[12]:


coleccion = {'estudiantes', 'yo', 'vos'}


# In[13]:


'vos' in coleccion


# In[14]:


'cualquier' in coleccion


# In[15]:


repetido = {'repetido','repetido','repetido'}


# In[16]:


repetido


# conjunto no nos muestra elementos repetidos 

# In[17]:


lista = [5,5,6,6,7,7]


# In[18]:


lista


# In[19]:


conjunto = set(lista)


# In[20]:


conjunto


# transformamos la lista en un conjunto como lo escribi antes (conjunto vacio), y automaticamente nos elimina los valores repetidos

# In[21]:


cadena = "me gusta la droguita mucho mucho mucho"


# In[22]:


set(cadena)


# nos limpia la cadena de caracteres repetidos 

# In[ ]:




