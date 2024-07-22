"""class estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre= nombre
        self.edad= edad
        self.grado= grado
    def estudiar(self):
        print(f"El estudiante {self.nombre} se encuentra estudiando.")
nombre=input("Cual es su nombre? ")
edad=input("Cual es su edad? ")
grado=input("Cual es su grado? ")

est1=estudiante(nombre,edad,grado)

print(f"El estudiante se llama:{est1.nombre}.\nEl estudiante {est1.nombre} tiene {est1.edad} años.\nEl estudiante {est1.nombre} pertenece al grado {est1.grado}.")


while True:
    a=input("")
    if (a.lower()=="estudiar"):
        est1.estudiar()
    break

class universitario(estudiante):
    def __init__(self,nombre,edad,grado):
        estudiante.__init__(self,nombre,edad,grado)

jorge=universitario("jorge",11,22)

jorge.estudiar()

"""
class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def SeeName(self):
        print(f"{self.nombre}")
    def SeeAge(self):
        print(f"{self.edad}")
class estudiante(persona):
    def __init__(self,nombre,edad,grado):
        persona.__init__(self,nombre,edad)
        self.grado=grado
    def SeeGrado(self):
        print(f"{self.grado}")

santiago=persona("santiago","11")
santiago.SeeName()
santiago.SeeAge()

sergio=estudiante("sergio","12","quinto")
sergio.SeeName()
sergio.SeeAge()
sergio.SeeGrado()