from test import Rg
from ID import Aid

def Dp():
    Name = input("What is your name? ")
    Age = input("How old are you? ")
    Country = input("Where are you from?")
    Gender = input("Are you male or female?")
    i = {
        "nombre": Name,
        "edad": Age,
        "pais": Country,
        "genero": Gender
    }
    id=Aid()
    Rg(Name,Age,Country,Gender)
    return (i)

