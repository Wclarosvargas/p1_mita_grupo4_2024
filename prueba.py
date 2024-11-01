from validaciones import validar_promedio
def promedio_recursivo(Notas):
    if 1==len(Notas):
        return Notas[0]
    else:
        return Notas[0]+ promedio_recursivo(Notas[1:])

Autorizacion=0
while Autorizacion==0:
    print("Ingrese su nota de Matematica")
    Mat=float(input())
    if validar_promedio(Mat)==1:
        Autorizacion=1
    else:
        print("Ingrese un numero del 1 al 10")
while Autorizacion==1:
    print("Ingrese su nota de Historia")
    Histori=float(input())
    if validar_promedio(Histori)==1:
        Autorizacion=0
    else:
        print("Ingrese un numero del 1 al 10")
while Autorizacion==0:
    print("Ingrese su nota de Biologia")
    Biology=float(input())
    if validar_promedio(Biology)==1:
        Autorizacion=1
    else:
        print("Ingrese un numero del 1 al 10")
while Autorizacion==1:
    print("Ingrese su nota de Literatura")
    Literature=float(input())
    if validar_promedio(Literature)==1:
        Autorizacion=0
    else:
        print("Ingrese un numero del 1 al 10")
Notas=[Mat,Histori,Biology,Literature]
promedio=int((promedio_recursivo(Notas))//4)

print(Notas)
print(promedio)