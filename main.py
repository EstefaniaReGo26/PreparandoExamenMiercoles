bandas=[]
banda={}

opcion=100
while(opcion != 5):   
    print ("****FESTIVAL ALTAVOZ****")
    print("***************************")
    print("1.Registrar banda")
    print("2.Ver el cartel del festival")
    print("3.Buscar banda")
    print("4.Modificar banda")
    print("5.Finalizar")
    opcion=int(input("Digita una opcion: "))

    if opcion == 1:
        banda={}
        #se llena el objeto de banda
        banda["id"]=int(input("Digite el id: "))
        banda["nombre"]=(input("Nombre: "))
        banda["genero"]=(input("Genero: "))
        banda["costo"]=(input("Costo: "))
        
        #como agrego un diccionadio a una lista
        bandas.append(banda)
        print(bandas)

    elif opcion == 2:
        for bandaAuxiliar in bandas:
            print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")

    elif opcion == 3:
        #buscando un elemento dentro de una lista
        bandaBuscada=input("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas: 
            if bandaAuxiliar["nombre"]==bandaBuscada:
                print("oe, la encontré")
            else:
                print("no lo encontraste")
                
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        print("opcion invalida")
