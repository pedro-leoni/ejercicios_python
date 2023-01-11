#!/usr/bin/env python
# coding: utf-8

# ### Metodo constructor ||| Metodo destructor

# In[2]:


# __init__  ||| __del__


# In[3]:


class Fabrica:
    def __init__(self, tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("se creo el auto", self.nombre)
    def __del__ (self):
        print("se elimino el auto", self.nombre)


# In[7]:


a = Fabrica(10,"chevrolet",4)


# In[10]:


# mientras el objeto este vacio usara el init, pero una vez que el objeto ya este cargado usara el del, creando un ciclo sin fin 
# con 1 solo lugar de memoria (elobjeto)(simbolicamente hablando)


# In[11]:


class Fabrica:
    def __init__(self, tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("se creo el auto", self.nombre)
    def __del__ (self):
        print("se elimino el auto", self.nombre)
        
    def __str__(self):
        return "{} se fabrico con exito, en el tiempo {} y tiene esta cantidad de ruedas {}".format(self.nombre,self.tiempo,self.ruedas)


# In[13]:


a = Fabrica(10,"ford",4)


# In[14]:


str(a)


# ### otro metodo es el str del ejemplo que me sirve para enviar una string 

# In[15]:


# __str__ 


# tambien podemos medir la longitud de un objeto

# In[16]:


class Fabrica:
    def __init__(self, tiempo,nombre,ruedas):
        self.tiempo = tiempo
        self.nombre = nombre
        self.ruedas = ruedas
        print("se creo el auto", self.nombre)
    def __del__ (self):
        print("se elimino el auto", self.nombre)
        
    def __len__(self):
        return self.tiempo


# In[17]:


a = Fabrica(10,"ford",4)


# In[18]:


len(a)


# In[19]:


# recordar, que el metodo este entre __metodo__ significa que son metodos especiales/magicos
# proporcionan características sintácticas especiales o hacen cosas especiales al usarlos


# In[ ]:




