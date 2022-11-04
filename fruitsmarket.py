
fruits={
    "Plátano": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}
print(fruits)

flag=True
while flag:
    print("""
Bienvenido al supermercado virtuarl.
Las frutas que tenemos son:
        * Plátano.
        * Manzana.
        * Pera.
        * Naranja
          """)
    fruta=input("Qué fruta desea comprar?: ").strip().capitalize()
    if fruta in fruits:
        cantidad=int(input(f"¿Cuántos kilos de {fruta} desea adquirir?: "))
        total= cantidad*fruits[fruta]
        print(f"Su total es: {total}")
        print("Gracias por su compra.")
        break
    else:
        print("Lo siento, no tenemos la fruta que desea adquirir.")
        print("Intenta con una de las frutas del menú de frutas")