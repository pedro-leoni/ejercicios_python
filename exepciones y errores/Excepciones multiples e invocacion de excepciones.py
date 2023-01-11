#!/usr/bin/env python
# coding: utf-8

# In[4]:


try:
    a = input("numero: ")
    10/a
    
except Exception as x:
    print(type(x).__name__)   


# In[6]:


try:
    a = float(input("numero: "))
    10/a
except TypeError:
    print("esto es una cadena")
except ValueError:
    print("esto es un error de valores")
except ZeroDivisionError:
    print("no se puede dividir por 0")
except Exception as x:
    print(type(x).__name__)   


# ### aca asignamos except a los distintos tipos de error que vamos a arrojar

# In[11]:


def profesor(estudiantes=None):
    if estudiantes is None:
        print("debes escribir algo si no no llames a mi funcion")


# In[12]:


profesor()


# In[13]:


# otra forma de mostrar un error 


# In[17]:


def profesor(estudiantes=None):
    if estudiantes is None:
        raise ValueError("este value error se vera reflejado en el mensaje de error")


# In[18]:


profesor()


# In[16]:


# con raise agregamos el texto que querramos al error de la raiz 


# In[ ]:




