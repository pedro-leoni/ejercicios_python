#!/usr/bin/env python
# coding: utf-8

# # Funciones recursivas y funciones integradas

# In[1]:


#las funciones recursivas son aquellas que se llaman a si mismas


# In[2]:


#hay que tener cuidado con no caer en el bucle infinito


# In[7]:


def atras(segundos):
    segundos -= 1
    if segundos >= 0:
        print(segundos)
        atras(segundos)
    else:
        print("termino la cuenta atras")


# In[8]:


atras(10)


# In[9]:


#la funcion integrada es la que transforma una cadena a un entero por ejemplo 


# In[10]:


e = int("15")


# In[11]:


e


# In[12]:


#en este caso integramos una funcion int a una string


# In[13]:


bin(15)


# In[14]:


#pedimos el  binario de lo que sea


# In[15]:


hex(15)


# In[16]:


#pedimos el hexadecimal de lo que sea


# In[17]:


abs(-10)


# In[18]:


#el valor abs (absoluto) va a ser siempre positivo


# In[20]:


round(4.4)


# In[21]:


round(4.6)


# In[22]:


#con round redondeamos


# In[23]:


len("alvaro")


# In[24]:


help()


# In[25]:


#tutorial 


# In[ ]:




