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
        print("La operacion que elegiste no es valida.")