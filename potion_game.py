#characterhp=45, potion=alleatory 0-100, difficulty= change the hp recieved from the potion
# moredifficult/lesshp
import random
difficulty= int(input("Seleccione una dificultad [1-3]:"))
character_hp=200
potion_used=0
boss1="AR'NARUB"
boss2="BURNA'SHES"
boss3="EL DESOLLADOR"
total_potions=20


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
    character_hpt=character_hp
    character_hp=character_hp-random.randint(damage,damage+20)
    print(f"-{character_hpt-character_hp} hp, su salud es: {character_hp}")
    if character_hp<1:
        print("GAME OVER")
        print(f"Haz usado un total de {potion_used} pociones")
        map2=False
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
    map2=True
    if map==1:
        boss=boss1
        print(f"Felicidades, has llegado a salvo a la guarida de {boss} ")
    elif map==2:
        boss=boss2
        print(f"Felicidades, has llegado a salvo a la guarida de {boss} ")
    else:
        boss=boss3
        print(f"Felicidades, has llegado a salvo a la guarida de {boss} ")

print(f"Haz usado un total de {potion_used} pociones")

flag=True
boss_event=random.randint(1,2)
if map2==True:   
    while flag:
        explore=input("¿Deseas ingresar?[s/n]: ")
        if explore=="s":
            print(f"Has ingresado a la guarida de {boss}")
            if boss_event==1:
                print(f"Haz tenido suerte {boss}, no está en su guarida")
                print(f"Puedes deshatar al rey y usar la herramienta de teletransportación")
                exit=input("Deseas deshatar al rey antes de salir?[s/n]:")
                if exit=="s":
                    print("Rey: ¡Qué haces, yo no quería volver")
                    print("stab")
                    character_hpt=character_hp
                    character_hp=character_hp-character_hpt
                    print(f"-{character_hpt-character_hp} hp, su salud es: {character_hp}")
                    print("Haz muerto a manos del rey")
                    flag=False
                elif exit=="n":
                    print("Has escapado sin el rey. No eres rico ni un heroe pero al menos estás vivo")
                    flag=False
            elif boss_event==2:
                print(f"{boss} Te mira fijamente")
                print(f"{boss} ha utilizado 'Ataque de bienvenida'")
                print("'Ataque de Bienvenida' es muy efectivo")
                welcome_attack=character_hp
                character_hp=character_hp-welcome_attack
                print(f"-{welcome_attack-character_hp} hp, su salud es: {character_hp}")
                print(f"Haz muerto a manos de {boss}")
                flag=False
            else:
                print("Intenta nuevamente, sólo [s/n]")
                continue
        elif explore=="n":
            print(f"Has usado el dispositivo de teletransportación para escapar sin mirar lo que te esperaba en la guarida de {boss}. No eres rico ni un heroe pero al menos estás vivo")
            flag=False
            