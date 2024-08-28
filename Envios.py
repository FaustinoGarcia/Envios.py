import random

def generarId(ids):
    id_unico = random.randint(1000, 9999) 
    unico = False 
    while not unico:  
        if id_unico not in ids:  
            unico = True 
        else:
            id_unico = random.randint(1000, 9999) 
    print('El ID asignado es:', id_unico)
    return id_unico

def ingresoNuevosEnvios (ids, costos, peso, destinos):
    opcion = int(input('Ingrese -1 para finalizar la carga, o 1 para continuar: '))   
    while(opcion != -1):
        ids_nuevos = generarId (ids)
        ids.append(ids_nuevos)
        costo_nuevo = float(input('Ingrese el costo del envio: '))
        costos.append(costo_nuevo)
        peso_nuevo = float(input('Ingrese el peso total del envio a ingresar en KG: '))
        peso.append(peso_nuevo)
        destino_nuevo = int(input('Ingrese 1, si su envio tiene destino Nacional. Ingrese 2 si su envio corresponde a un destino Internacional'))
        destinos.append(destino_nuevo)

        print('Se ingresaron los siguiente datos: \n ID:', ids_nuevos, '\n Costo: $', costos, '\n Peso:', peso,'kg.')
        opcion = int(input('Ingrese -1 para finalizar la carga, o 1 para continuar: '))
        
def mostrarEnvios (ids, costos, peso, destinos):
    for i in range(len(ids)):
        print('El ID', ids[i])
    for i in range(len(costos)):
        print('El costo', i)

    for i in range(len(peso)):
        print('El peso', i)

    for i in range(len(destinos)):
        print('El peso', i)



def mostrarMenu ():
    print("1. Si desea ingresar un nuevo envio.")
    print("2. Si desea buscar un envio por su ID.")
    print("3. Si desea ordenar los envios por su costo.")
    print("4. Si desea encontrar un envio por su costo maximo o minimo.")
    print("5. Si desea ver el estado final, hasta el momento, de todos sus envios.")
    print("6. Salir")

def main():
    ids = []
    costos = []
    peso = []
    destinos = []

    mostrarMenu()
    
    opcion = int(input("Seleccione una opcion: "))
    while (opcion != 6):
        if (opcion == 1):
            ingresoNuevosEnvios(ids, costos, peso, destinos)
        elif (opcion == 2):
            generarId(ids)
        elif (opcion == 3): 
            mostrarEnvios(ids, costos, peso, destinos) 
        elif (opcion == 4):
            print('proximamente')
        elif (opcion == 5):
            print('proximamente')
        else:
            print('Error - Ingrese una opcion correcta')
        mostrarMenu()
        opcion = int(input("Seleccione una opcion: "))
    print('Hasta luego')

    
if __name__ == "__main__":
    main()