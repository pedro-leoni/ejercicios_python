#!/usr/bin/env python
# coding: utf-8

# In[26]:


class encapsulamiento: 
    __privado_atributo = "soy un atributo encapsulado"
    def __privado_met(self):
        print("soy un metodo que no vas a poder a cceder desde afuera de la clase ")


# In[27]:


e = encapsulamiento ()


# In[28]:


e


# In[29]:


e.__privado_atributo


# ## como resolver esto:

# In[22]:


class encapsulamiento: 
    __privado_atributo = "soy un atributo encapsulado"
    def __privado_metodo(self):
        print("soy un metodo que no vas a poder a cceder desde afuera de la clase ")
    def publico_atributo(self):
        return self.__privado_atributo
    def publico_metodo(self):
        return self.__privado_metodo()
    


# In[23]:


e = encapsulamiento()


# In[24]:


e.publico_atributo()


# In[25]:


e.publico_metodo()


# In[30]:


# es medio rebuscado, pero es es el biri magico para desencapsular algo 


# In[ ]:




