#!/usr/bin/env python
# coding: utf-8

# In[43]:


class Fabrica:
    def __init__(self,marca,nombre,precio,descripcion):
        self.marca = marca
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
    def __str__(self):
        return""""MARCA\t{}
NOMBRE\t{}
PRECIO\t{}
DESCRIPCION\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion)
    
class Auto(Fabrica):
    pass

class Deportivo(Fabrica):
    ruedas = ""
    distribuidor = ""
    
    def __str__(self):
        return"""MARCA\t{}
NOMBRE\t{}
PRECIO\t{}
DESCRIPCION\t{}
RUEDAS\t{}
DISTRIBUIDOR\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion,self.ruedas,self.distribuidor)
    
class Accesorios(Fabrica):
    autor = ""
    fabricante = ""
    
    def __str__(self):
        return"""MARCA\t{}
NOMBRE\t{}
PRECIO\t{}
DESCRIPCION\t{}
RUEDAS\t{}
DISTRIBUIDOR\t{}
AUTOR ACCESORIOS\t{}
FABRICANTE ACCESORIOS\t{}""".format(self.marca,self.nombre,self.precio,self.descripcion,self.ruedas,self.distribuidor,self.autor,self.fabricante)


# In[44]:


a = Auto('Ford','Ranger',100000,'Camioneta')
deportivo = Deportivo('Volkswagen','Vento',54000,'el mejor')
deportivo.ruedas = 3 
deportivo.distribuidor = 'tu autito'

accesorios = Accesorios('Fiat','Luces de neon',10000,'iluminan mejor')
accesorios.autor= 'tutia'
accesorios.fabricante = 'tu tia abuela'


# In[45]:


fabrica = [accesorios, deportivo] 


# In[46]:


fabrica.append(a)


# In[47]:


fabrica


# In[48]:


#formas de recorrer la infomacion que ya almacenamos en esta superclase 


# In[49]:


for x in fabrica:
    print(x,"\n")


# In[50]:


accesorios.ruedas = 6


# In[51]:


for x in fabrica:
    print(x,"\n")


# In[52]:


accesorios.distribuidor = 'tonto'


# In[54]:


for x in fabrica:
    print(x,"\n")


# In[55]:


# con el "\n" hacemos que nos haga un salto de linea entre elemento y elemento 


# In[56]:


for x in fabrica:
    print(x.marca,x.precio)


# In[58]:


for x in fabrica :
    print(x.autor)


# In[64]:


# en el ejemplo de abajo muestro como recorrer los atributos que no tienen todos los elementos con isinstance
# lo que hace el isinstance es tratar a cada subclase de manera distinta, evaluandolas por si mismas


# In[62]:


for x in fabrica:
    if(isinstance(x, Auto)):
        print(x.marca,x.nombre)
    elif(isinstance(x, Deportivo)):
        print(x.marca,x.nombre,x.ruedas)
    elif(isinstance(x, Accesorios)):
        print(x.marca,x.nombre,x.fabricante)
        


# In[66]:


#ahora vamos a ver como recibir objetos mediante funciones 
#lo que hagamos dentro de la funcion va a afectar de una manera directa al objeto (POLIMORFIRMOS)


# In[69]:


def Descuento_accesorios(t, descuento):
    t.precio = t.precio - (t.precio/100 * descuento)


# In[70]:


Descuento_accesorios(accesorios, 10)


# In[71]:


accesorios.precio


# In[77]:


#lo que paso aca es que modificamos bien el valor del precio aplicando el descuento
#pero tambien sin querer modificamos el objeto
#para hacerlo bien, sin tocar el objeto tenemos que importar copy y trabajar con la copia
#el polimorfismo es implicito en python 


# In[78]:


import copy


# In[79]:


copia_deportivo = copy.copy(accesorios)


# In[80]:


print(copia_deportivo)


# In[ ]:




