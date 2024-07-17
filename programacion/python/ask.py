from test import Rg

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
    Rg(Name,Age,Country,Gender)
    return (i)

