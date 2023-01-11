#!/usr/bin/env python
# coding: utf-8

# In[4]:


class primera:
    def __init__(self):
        print("soy la primer clase")
class segunda:
    def __init__(self):
        print("soy la segunda clase")
class tercera(primera, segunda):
    pass


# In[5]:


herencia_multiple = tercera()


# In[8]:


#python va a dar prioridad a las clases que se encuentran mas a la izquierda al momento de declarar la subclase


# In[9]:


class primera:
    def __init__(self):
        print("soy la primer clase")
class segunda:
    def __init__(self):
        print("soy la segunda clase")
class tercera(segunda, primera):
    pass


# In[10]:


herencia_mutiple = tercera()


# In[16]:


class primera:
    def __init__(self):
        print("soy la primer clase")
    def primera(self):
        print("este es el metodo heredado de la primera")
class segunda:
    def __init__(self):
        print("soy la segunda clase")
    def segunda(self):
        print("este es el metodo heredado de la segunda")
class tercera(primera, segunda):
    def tercera(self):
        print("este es el metodo heredado de tercera")


# In[17]:


herencia_multiple = tercera()


# In[18]:


herencia_multiple.primera()
herencia_multiple.segunda()
herencia_multiple.tercera()


# In[ ]:




