#hacer un diccionario con varias películas. Nombre de la película [edad requerida,boletos existentes]
#debe verificar edad y si quedan boletos, imprimir "disfruta la película", si no cumple la edad debe decirlo 
# e igualmente, si no hay boletos debe imprimir un mensaje que diga que no hay boletos

movies= {
    "Seven":[14,5],
    "Titanic":[8,5],
    "Star Trek":[5,5],
    "Jurasic Park": [12,5]    
}
flag=True
while flag:
    your_movie=input("¿Qué película deseas ver?: ").strip().title()
    if your_movie in movies:
        age=int(input("¿Qué edad tienes:"))
        if age >= movies[your_movie][0]:
            tickets=movies[your_movie][1]
            if tickets>0:
                movies[your_movie][1]-=1   
                print("Muy bien, disfruta la película!")         
            else:
                print("Lo sentimos, no quedan boletos")
        else:
            print("Lo sentimos, no tienes edad suficiente para ver la película")
    else:
        print("Lo sentimos, esta película no está en cartelera")
    