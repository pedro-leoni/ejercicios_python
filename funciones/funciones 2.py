#!/usr/bin/env python
# coding: utf-8

# # Funciones - argumentos por valor, referencia y parametros indeterminados

# In[1]:


#lo que sucede en la funcion queda en la funcion, no afecta a la variable afuera


# In[5]:


def estudiantes(valor):
    valor*=3

variable = 15
estudiantes(variable)
variable


# In[6]:


variable


# In[7]:


#si yo tengo una variable y quiero usarla para lo que sea, su valor no va a modificarse, si hubiera mostrado lo de dentro de la 
#funcion con un print solo se hubiera ejecutado para eso, nos hubiera mostrado el resultado y la variable conservaria el valor


# In[8]:


# NO ASI pasa con las LISTAS 


# In[12]:


def listas(numero):
    for x,i in enumerate(numero):
        numero[x] *= 3 
        
lista = [50,100,150]
listas(lista)


# In[13]:


lista


# In[15]:


#la variable se modifico por mas que la incluimos dentro de la funcion, en realidad las variables no se modifican 
#pero las listas si


# In[16]:


# para hacer una lista inmodificable usamos el [:]


# In[18]:


def listas(numero):
    for x,i in enumerate(numero):
        numero[x] *= 3
    
lista=[50,100,150]
listas(lista[:])


# In[19]:


lista


# In[21]:


def estudiantes(valor):
    return valor*3
variable = 15
variable = estudiantes(variable)
variable


# In[ ]:




