import random
difficulty= int(input("Seleccione una dificultad [1-3]:"))
character_hp=200
potion_used=0


print("""
Bienvenido a Hell of a World
El ambiente en este mundo es 
hostil y cada momento que pasa
pierdes un poco de tu salud
Usa tus pociones e intenta sobrevivir.
Selecciona un mundo:
    1. El desierto de ar'narub (Tormentas de Arena)
    2. El crater de burna'shes (Fuego)
    3. Tierras devastas (Veneno)""")
flag=True
while flag:
    map= int(input("Selecciona un mapa[1-3]:"))
    if map==1 or map==2 or map==3:
        flag=False
    else:
        print("Opción no válida")
        continue
if map==1:
    duration=random.randint(15,20)
    if difficulty==1:
        damage=random.randint(1,10)
    elif difficulty==2:
        damage=random.randint(8,15)
    elif difficulty==3:
        damage=random.randint(10,25)
elif map==2:
    duration=random.randint(10,15)
    if difficulty==1:
        damage=random.randint(1,20)
    elif difficulty==2:
        damage=random.randint(15,25)
    elif difficulty==3:
        damage=random.randint(25,30)
elif map==3:
    duration=random.randint(12,18)
    if difficulty==1:
        damage=random.randint(5,20)
    elif difficulty==2:
        damage=random.randint(12,22)
    elif difficulty==3:
        damage=random.randint(15,25)
#print(f"{duration},Duración y {damage}, Daño")
    
for i in range(0,duration,1):
    character_hp=character_hp-random.randint(damage,damage+20)
    print(f"-{damage} hp, su salud es: {character_hp}")
    if character_hp<1:
        print("GAME OVER")
        print(f"Haz usado un total de {potion_used} pociones")
        break
    wtd=input("Desea beber una poción?[s/n]:")
    if wtd=="s":           
        if difficulty==1:
            potion=random.randint(50,100)
            if potion<=90:
                print("Ha sacado un crítico en la poción")
        elif difficulty==2:
            potion=random.randint(30,80)
            if potion<=70:
                print("Ha sacado un crítico en la poción")
        else:
            potion=random.randint(10,50)
            if potion<=40:
                print("Ha sacado un crítico en la poción")
        drink_potion=character_hp+potion
        character_hp=drink_potion
        potion_used+=1
        print(f"Ha bebido una poción, su nueva salud es {character_hp}")    
    else:
        continue
else:
    print("Felicidades, has sobrevivido")
    print(f"Haz usado un total de {potion_used} pociones")

