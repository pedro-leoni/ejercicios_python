#!/usr/bin/env python
# coding: utf-8

# # argumentos y parametros indeterminados dentro de funciones
# ### en este caso por posicion

# In[1]:


#esta alternativa es solo de py


# In[7]:


def argumento(*tu):
    for tus in tu:
        print(tus)


# In[8]:


argumento('alvaro','pedro',10,[1,2,3])


# In[9]:


#asi podria mandar infinitos argumenntos


# ### por nombre (diccionario)

# In[29]:


def nombre_diccionario(*tu,**lo):
    b = 0 
    for tus in tu:
        b+=tus
    print(b)
    for x in lo:
        print(x, " ",lo[x])


# In[30]:


nombre_diccionario(1,2,3,4,alvaro='profesor',pedro='estudiante',calificacion=[7,8,9])


# In[31]:


#b es la flag que va acumulando la sumatoria de tus(tuplas) que le mande 


# In[ ]:




