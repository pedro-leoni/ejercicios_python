#!/usr/bin/env python
# coding: utf-8

# # RETORNO DE VALORES

# In[1]:


def estudiante():
    return "los estudiantes se la comen"


# In[2]:


estudiante()


# In[3]:


print(estudiante())


# In[4]:


#cuando hablamos de return hablamos de cualquier tipo de valor


# In[5]:


def estudiante():
    return[5,6,7,8]


# In[6]:


print(estudiante())


# In[8]:


print(estudiante()[0:2])


# In[9]:


def estudiante():
    return "alvaro chirou","los estudiantes",19,[5,6,7,3,1,43]


# In[10]:


estudiante()


# In[11]:


a,b,c,d = estudiante()


# In[12]:


a


# In[13]:


b


# In[14]:


c


# In[15]:


d


# In[16]:


#asignacion multiple, en orden al return de la funcion 


# # ENVIO DE VALORES

# In[24]:


def suma(i,x):
    return i+x


# In[25]:


suma(5,5)


# In[20]:


#asi podemos asignarle los valores que querramos hacer para siempre con una sola funcion, entender que esto aplica para
#cosas mucho mas complejas y este es un ejemplo estupido, pero recordar, es importante


# In[26]:


def mutiplicacion(a,b):
    return a*b


# In[32]:


variable = mutiplicacion(3,5)


# In[33]:


variable


# In[31]:


#otro ej


# In[ ]:




