#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Fabrica:
    def __init__(self, tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("se creo el auto", self.nombre)
    def __str__ (self):
        return "{}({})".format(self.nombre,self.tiempo)


# In[4]:


class Listado:
    autos = []
    
    def __init__(self,autos=[]):
        self.autos = autos
        
    def adicionar(self,x):
        #x el objeto del auto        
        self.autos.append(x)
        #estamos fabricando el objeto
    def visualizar(self):
        for x in self.autos:
            print(x)


# In[6]:


a = Fabrica(10,"ford",4)


# In[10]:


l = Listado([a])
# de esta manera agregamos al auto a la lista


# In[13]:


l.visualizar()
# de esta manera visualizamos la lista 


# In[14]:


l.adicionar(Fabrica(15,"chevrolet",3))


# In[15]:


l.visualizar()


# In[ ]:




