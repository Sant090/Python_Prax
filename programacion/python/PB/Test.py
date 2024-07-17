#calculadora basica
"""
A=int(input("elije un numero " ))
B=int(input("elije otro numero " ))
resultado=0
Operaciones=["1.Suma","2.resta","3.Multiplicacion","4.Division"]

while 0==0:
    print("\nelije alguna de las siguientes operaciones:")
    for op in Operaciones:
        print(op)
    
    el=int(input())
    if el==1:
        resultado = A+B
        print(f"Al sumar{A} y {B} da como resultado: {resultado}")
        break
    elif el==2:
        resultado = A-B
        print(f"Al restar{A} y {B} da como resultado: {resultado}")
        break
    elif el==3:
        resultado =A*B
        print(f"Al multiplicar{A} y {B} da como resultado: {resultado}")
        break
    elif el==4:
        resultado = A/B
        print(f"Al dividir {A} y {B} da como resultado: {resultado}")
        break
    else:
        print("La operacion que elegiste no es valida.")"""
#salu3 internautas

#determinar mayor y menor entre 3 numeros
"""
a=int(input("Ingrese el primer numero "))
b=int(input("Ingrese el segundo numero "))
c=int(input("Ingrese el tercer numero "))

if a>=b and a>=c:
     print(f"{a} es mayor")
elif b>=c and b>=a:
    print(f"{b} es mayor")
else:
    print(f"{c} es mayor")

if a<=b and a<=c:
     print(f"{a} es mayor")
elif b<=c and b<=a:
    print(f"{b} es mayor")
else:
    print(f"{c} es mayor")
"""

#multiplos de un numero hasta el 10

a=int(input("ingrese un numero "))
x=1
print(f"la tabla de multiplicar del 1 al 10 de {a} es:")
while x<=10:
    print(f" {x}x{a} = ({x*a})")
    x+=1






