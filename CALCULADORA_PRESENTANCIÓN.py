import math

def suma(x,y):
    total=x+y
    return total

def resta(x,y):
    diferencia=x-y
    return diferencia

def multiplicacion(x,y):
    producto=x*y
    return producto

def cociente(x,y):
    cociente=x/y
    return cociente

def modulo(x,y):
    modulo=x%y
    return modulo

def potencia(x,y):
    p=pow(x,y)
    return p
        
def raiz(num):
    raiz=math.sqrt(num)
    return raiz

def promedio(vec,tam):
    suma=0
    cant=0
    for i in range (tam):
        x=float(input("Ingrese numero: "))
        vec.append(x)
        suma=suma+x
        cant=cant+1
    prom=suma/cant
    return prom

def mayor(x,y):
    if x>y:
        return x
    else: 
        return y

##PROGRAMA PRINCIPAL

prog=True
while prog==True:
    
    print("")
    print("OPERACIONES MATEMÁTICAS")
    print("")
    print("1-Sumar numeros")
    print("2-Restar numeros")
    print("3-Multiplicar numeros")
    print("4-Dividir numeros")
    print("5-Potencia de un numero")
    print("6-Raíz cuadrada de un numero")
    print("7-Promedio de numeros")
    print("8-Mayor de una lista")
    print("9-sistema contable")
    print("10-Salir")
    print("")
    
    op=int(input("Elegir opción: "))
    if op==1:
        n=int(input("Ingrese cantidad de numeros a sumar: "))
        a=float(input("Ingrese numero: "))
        for i in range (n-1):
            b=float(input("Ingrese numero: "))
            s=suma(a, b)
            a=s
        print("")
        print ("La suma es: ", s)
        
    if op==2:
        n=int(input("Ingrese cantidad de numeros a restar: "))
        a=float(input("Ingrese numero: "))
        for i in range (n-1):
            b=float(input("Ingrese numero: "))
            r=resta(a, b)
            a=r
        print("")
        print ("La resta es: ", r)
        
    if op==3:
        n=int(input("Ingrese cantidad de numeros a multiplicar: "))
        a=float(input("Ingrese numero: "))
        for i in range (n-1):
            b=float(input("Ingrese numero: "))
            p=multiplicacion(a, b)
            a=p
        print("")
        print ("El producto es: ", p)
    
    if op==4:
        a=float(input("Ingrese numero: "))
        b=float(input("Ingrese numero: "))
        c=cociente(a, b)
        m=modulo(a, b)
        print("")
        print("El cociente de",a,"/",b,"=",c)
        print("El modulo de",a,"%",b,"=",m)
        
    if op==5:
        a=float(input("Ingrese numero: "))
        b=float(input("Ingrese exponente: "))
        p=potencia(a, b)
        print("")
        print(a,"^",b,"=",p)
        
    if op==6:
        a=float(input("Ingrese numero: "))
        rc=raiz(a)
        print("")
        print("La raíz cuadrada de",a,"es ",rc)
        
    if op==7:
        numeros=[]
        n=int(input("Ingrese cantidad de numeros a promediar: "))
        p=promedio(numeros, n)
        print("")
        print("El promedio de: ", numeros,"es: ", p)
    
    if op==(8):
        numeros=[]
        n=int(input("Ingrese cantidad de numeros: "))
        a=float(input("Ingrese numero:  "))
        numeros.append(a)
        for i in range (0, n-1):
            b=float(input("Ingrese numero: "))
            numeros.append(b)
            m=mayor(a,b)
            a=m
            may=mayor(a,b)
        print("")
        print ("La lista ingresada contiene: ", numeros)
        print ("El numero mayor es: ", may)
    
    if op==(9):
        '''calcular el total a pagar por la venta de N productos 
        , se debe mostrar:
        1. Subtotal
        2.IVA
        3. Total a pagar'''
        print("Cuantos productos desea evaluar?: ")
        prods = int(input())
        i= 0
        sub=0
        while i<prods :
            print("Valor del Producto " ,i+1," :")
            val = int(input())
            print("Cantidad")
            cant = int(input())
            subpro=val*cant
            sub=sub+subpro
            i+=1
        IVA =sub * 0.21
        total = sub + IVA
        print("Vendieron: ",prods, " Productos")
        print("Subtotal:",sub)
        print("IVA 21%  ",IVA)
        print("Total: ",total)
    if op==10 or op==0:
        prog=False

print("")
print("FIN")