msj=input("Escriba un mensaje:")

def mensaje():
    print(msj)

mensaje()

#viaje de bus 
#y=precio final
#x=kilometros recorridos

def bustrip(x):
    y=(1.5*x)+4
    print(f"El precio de su vaije es {y} MXD")
    
kmxprice=float(input("Inserte cuántos kilometros tiene su recorrido:"))

bustrip(kmxprice)

#Actividad 1: Escribir una función que pida un número entero entre 1 y 10 y guarde
# en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
# donde n es el número introducido.

