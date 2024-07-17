import pandas as pd

"""
dt=pd.read_csv("../datos/datos.csv",index_col=0)
print(dt.head)
dt1=pd.DataFrame({"Nombre":["santiago"],"Edad":[20],"Pais":["venezuela"],"Genero":[1]})
dt=pd.concat([dt,dt1])
dt.to_csv("../datos/datos.csv")
print(dt.head)"""


def Rg(Name,Age,Country,Gender):
    dt=pd.read_csv("../datos/datos.csv",index_col=0)
    dt1=pd.DataFrame({"Nombre":[Name],"Edad":[Age],"Pais":[Country],"Genero":[Gender]})
    dt=pd.concat([dt,dt1])
    dt.to_csv("../datos/datos.csv")
