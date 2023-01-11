#!/usr/bin/env python
# coding: utf-8

# # Devolucion a errores

# In[ ]:


try: 
    variable = float(input("Introduce algo: "))
    a = 2
    print("resultado: ",a*variable)
except:
    print("ingresaste cualquiera rancio")


# In[3]:


while(True):
    try: 
        variable = float(input("Introduce algo: "))
        a = 2
        print("resultado: ",a*variable)
        
    except:
        print("ingresaste cualquiera rancio, manda de nuevo")
    else:
        print("este es el mensaje de confirmacion")
        break
        


# In[4]:


while(True):
    try: 
        variable = float(input("Introduce algo: "))
        a = 2
        print("resultado: ",a*variable)
        
    except:
        print("ingresaste cualquiera rancio, manda de nuevo")
    else:
        print("este es el mensaje de confirmacion")
        break
    finally:
        print("esto lo devolvemos siempre pase lo que pase")


# In[ ]:




