#!/usr/bin/env python
# coding: utf-8

# # FUNCIONES ARGUMENTOS

# In[3]:


def funciones(a,b):
    return a-b


    


# In[ ]:


# estructura def funcion(argumento1,argumento2,argumento3):
# si la funcion tiene x cantidad de argumentos, estamos obligados a enviarselos, si no no se ejecuta


# In[5]:


funciones(2,2)


# In[4]:


funciones(b=2,a=1)


# In[6]:


funciones(2,1)


# In[7]:


#podemos enviar los argumentos por nombre como en el ejemplo anterior, para darle el orden que querramos


# In[11]:


def nulos (x=None,i=None):
    if x == None or i == None:
        print('escribi bien los numeros tonto')
        return
    return x/i


# In[12]:


nulos()


# In[13]:


nulos(1,3)


# In[ ]:




