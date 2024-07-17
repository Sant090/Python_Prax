from ask import *

def login():
    a=print(f"Hola usuario, desea: \n1. Ingresar a la base de datos\nregistrarse en la base de datos?")
    a=a.upper()
    if a=="INGRESAR" or a=="1":
        print("1")
    elif a=="REGISTRARME" or a=="2":
        print("2")

        """
    user=Dp()
    print(f"hola {user["nombre"]} espero estes bien")
"""

login()