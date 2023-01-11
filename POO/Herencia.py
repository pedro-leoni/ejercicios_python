#!/usr/bin/env python
# coding: utf-8

# In[8]:


# la superclase en este caso es fabrica 
class Fabrica: 
    def __init__(self,marca,nombre,precio,descripcion):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    
    def __str__(self):
        return"""
        MARCA = {}
        NOMBRE = {}
        PRECIO = {}
        DESCRIPCION = {}""".format(self.marca,self.nombre,self.precio,self.descripcion)


# In[9]:


# ahora creamos la subclase (auto)
class Auto(Fabrica):
    pass
z = Auto('Ford','ranger',100.000,'camioneta')
print(z)


# In[32]:


class Deportivo(Fabrica):
    ruedas = ""
    distribuidor = ""
    
    def __str__(self):
        return """MARCA  =\t {}
NOMBRE =\t {}
PRECIO =\t {}
DESCRIPCION =\t {}
RUEDAS =\t {}
DISTRIBUIDOR =\t {}""".format(self.marca,self.nombre,self.precio,self.descripcion,self.ruedas,self.distribuidor)
        


# In[33]:


deportivo = Deportivo('Volkswagen','Vento',54000,'el mejor')


# In[34]:


print(deportivo)


# In[35]:


deportivo = Deportivo('Volkswagen','Vento',54000,'el mejor')
deportivo.ruedas = 3
deportivo.distribuidor = 'tu autito'


# In[36]:


print(deportivo)


# In[ ]:





# In[ ]:




