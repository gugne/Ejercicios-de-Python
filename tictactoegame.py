

tablero= [" " for i in range(9)]
print (tablero)

def print_tablero():
    fila1="| {} | {} | {} |".format(tablero[0],tablero[1],tablero[2])
    fila2="| {} | {} | {} |".format(tablero[3],tablero[4],tablero[5])
    fila3="| {} | {} | {} |".format(tablero[6],tablero[7],tablero[8])
    print()
    print(fila1)
    print(fila2)
    print(fila3)
    print()

def jugador_mov(icono):
    if icono =="X":
        numero=1
    elif icono=="O":
        numero=2
    print (f"Tu turno judador {numero}")
    eleccion=int(input("Ingrese un número [1-9]: "))
    if tablero[eleccion-1]==" ":
        tablero[eleccion-1]=icono
    else:
        print()
        print("Ese espacio ya está ocupado")

def victory(icono):
    if (tablero[0]==icono and tablero[1]==icono and tablero[2]==icono) or \
    (tablero[3]==icono and tablero[4]==icono and tablero[5]==icono) or \
    (tablero[6]==icono and tablero[7]==icono and tablero[8]==icono) or \
    (tablero[0]==icono and tablero[3]==icono and tablero[6]==icono) or \
    (tablero[1]==icono and tablero[4]==icono and tablero[7]==icono) or \
    (tablero[2]==icono and tablero[5]==icono and tablero[8]==icono) or \
    (tablero[0]==icono and tablero[4]==icono and tablero[8]==icono) or \
    (tablero[2]==icono and tablero[4]==icono and tablero[6]==icono):
        return True
    else:
        return False

def draw():
    if " " not in tablero:
        return True
    else:
        return False
    
while True:
    print_tablero()
    jugador_mov("X")
    print_tablero()
    if victory("X"):
        print("El jugador 'X' es el ganador.")
        break
    elif draw():
        print("No quedan más casillas para continuar. EMPATE")
        break
    jugador_mov("O")
    if victory("O"):
        print("El jugador 'O' es el ganador.")
        break
    elif draw():
        print("No quedan más casillas para continuar. EMPATE")
        break
    
    