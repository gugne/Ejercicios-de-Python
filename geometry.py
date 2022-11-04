
def cuad(x):
    z=x**2
    return z

def cir(r):
    z=(math.pi)*(r**2)
    return z
def rect(x,y):
    z=x*y
    return z

def tri(b,h):
    z=(b*h)/2
    return z

flag=True
while flag:
    print ("""
Bienvenido a nuestra calculadora de areas.
Menú:
        1. Cuadrado.
        2. Círculo.
        3. Rectángulo.
        4. Tríangulo.
        
        
        5. SALIR.
           """)

    menu=int(input("Digite el numero de extensión: "))
    if menu==1:
        print("1. Cuadrado.")
        val1=int(input("Valor del lado:"))
        operación=cuad(val1)
        print(f"El area del cuadrado con lado '{val1}', es: {operación}")
        break
    elif menu==2:
        print("2. Círculo.")
        val1=int(input("Valor del radio:"))
        operación=cir(val1)
        print(f"El area de un círculo con radio {val1} , es: {operación}")
        break
    elif menu==3:
        print("3. Rectángulo.")
        val1=int(input("Valor del lado x:"))
        val2=int(input("Valor del lado y:"))
        operación=rect(val1,val2)
        print(f"El area de un rectangulo con lados  '{val1}' y '{val2}', es: {operación}")
        break
    elif menu==4:
        print("4. Tríangulo.")
        val1=int(input("Valor de la base:"))
        val2=int(input("Valor de la altura:"))
        operación=tri(val1,val2)
        print(f"El area de un tríangulo con base '{val1}' y altura '{val2}', es: {operación}")
        break
    
    elif menu==5:
        print("Hasta luego")
        break
    else:
        print("Comando no válido, vuelva a intentar de nuevo con un número del 1-4 o ")
        continue
    