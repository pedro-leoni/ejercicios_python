#!/usr/bin/env python
# coding: utf-8

# # PROGRAMACION ORIENTADA A OBJETOS
# ## OBJETO: ENTIDAD QUE AGRUPA UN ESTADO(SE DEFINE A TRAVES DE VARIABLES LLAMADAS ATRIBUTOS) Y UNA FUNCIONALIDAD RELACIONADA(SE MOLDEA A TRAVES DE FUNCIONES LLAMADAS METODOS)
# 
# ### Los objetos se crean a raiz de las clases
# ## Clase es la plantilla generica a partir de la cual creamos nuestros objetos
# 

# In[ ]:


class Clase:
    pass


# In[ ]:


Clase = Clase()


# In[ ]:


type(Clase)


# esto, significa que Clase es un objeto

# In[ ]:


def Clase1():
    pass
type(Clase1)


# In[ ]:


class Auto:
    pass


# In[ ]:


consecionaria = Auto()
#de esta forma instanciamos la clase y creamos el objeto cuya variable es consecionaria y su clase es Auto


# In[ ]:


consecionaria.color = "Rojo"
consecionaria.puertas = "Muchas"
#hacemos una referencia de variables internas (creamos atributos para auto)


# In[ ]:


print("Mi aunto es de color: ", consecionaria.color)


# In[ ]:


class Auto:
    Rojo = False


# In[ ]:


c = Auto()


# In[ ]:


c.Rojo


# ### Con el def __init__ inicializamos el objeto, es muy comun verlo como en el ejemplo de abajo

# In[7]:


class Auto:
    Rojo = False
    
    def __init__(self):
        print("se creo un auto")
    def Fabricar(self):
        self.Rojo = True

    def confirmar_fabricacion(self):
        if (self.Rojo):
            print("auto coloreado rojo")
        else:
            print("aun no esta coloreado")
a = Auto()
a.confirmar_fabricacion()
a.Fabricar()
a.confirmar_fabricacion()
a.Rojo


# ### el self es el parametro del metodo para acceder a los metodos y atributos de las instancias u objetos y los envia a la clase
# en criollo el self se usa para que ese atributo declarado se pase a la class

# Va el ejemplo de nuevo pero instanciado

# In[17]:


class Auto:
    Rojo = False 
    
    def __init__(self, puertas=None, color=None):
        self.puertas = puertas
        self.color = color
        if puertas is not None and color is not None:
            print("se creo un auto con puertas{} y color{}".format(puertas, color))
    #Validacion: con el none y este if lo unico que hago es que me permita ingresar a la funcion Auto con argumentos vacios
    def Fabricar(self):
        self.Rojo = True
    def confirmar_fabricacion(self):
        if (self.Rojo):
            print("auto coloreado rojo")
        else:
            print("aun no esta coloreado")


# In[15]:


a = Auto()


# In[ ]:




