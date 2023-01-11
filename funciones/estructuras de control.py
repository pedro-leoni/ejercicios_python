#!/usr/bin/env python
# coding: utf-8

# # if

# In[ ]:


if True:
    print('evaluacion verdadera')


# In[ ]:


if False:
    print('no va a imprimir porque la primer sentencia es verdadera')


# In[ ]:


pedro = 25 


# In[ ]:


if pedro == 25:
    print('pedro tiene 25')


# In[ ]:


if pedro == 23:
    print('esta mal')


# ### el if funciona como todos los if, si la primer condicion no se cumple el codigo no se ejecuta, de cumplirse sigue hasta la condicion en la que no se cumpla. tener en cuenta. Esto se llama jerarquizacion

# In[ ]:


pedro = 1
if pedro == 1 :
    print('estamos en la primer parte del codigo')
    if pedro == 2-1: 
        print('estamos en la segunda parte del codigo')
        


# # if and else if

# In[ ]:


pedro = 13


# In[ ]:


if pedro % 2 == 0:
    print('el resto es 0')
else:
    print('el resto no es 0')


# In[ ]:


frase = "hola"
if frase == "NO":
    print('bienvenido')
elif frase == "hola":
    print('nos dan la bienvenida')
else:
    print('esto va cuando no se cumple ninguna condicion')


# In[2]:


final = float(input('coloca la nota '))
if final >= 9:
    print('excelente')
elif final <= 8:
    print('aprobaste pero falta')
elif final <= 5: 
    print('desaprobaste lacra')
else:
    print('pone bien la nota rancio')


# # While

# In[4]:


iteracion = 1
while iteracion <= 3:
    iteracion += 1
    print('estoy iterando, van = ',iteracion)


# In[5]:


iteracion = 0
while iteracion <= 3:
    iteracion += 1
    print('estoy iterando, van = ',iteracion)


# In[7]:


iteracion = 0
while iteracion <= 3:
    iteracion += 1
    print('estoy iterando, van = ',iteracion)
else:
    print('el else marca el fin del bucle y siempre aparece')


# ### con el break podemos cortar la secuencia donde querramos

# In[8]:


iteracion = 0
while iteracion <= 10:
    iteracion += 1
    if(iteracion == 4):
        print('estoy iterando, van = ',iteracion)
        break
else:
    print('el else marca el fin del bucle y siempre aparece')


# ### me muestra solo el 4 porque es lo que yo le pedi en el if, si yo quisiera que me muestra numero por numero como antes tengo que hacer el print por fuera 

# In[10]:


iteracion = 0
while iteracion <= 10:
    iteracion += 1
    print('estoy iterando, van = ',iteracion)
    if(iteracion == 4):
        print('llegaste al break, esta es la iteracion numero ',iteracion)
        break
else:
    print('el else marca el fin del bucle y siempre aparece')


# In[ ]:




