import csv

contactos = []
def opcion_1():
    print("AGREGAR CONTACTO")
    Nombre = input("Ingrese nombre: ")
    Telefono = input("Ingrese telefono: ")
    Correo = input("Ingrese su correo: ")
    contacto = {"Nombre":Nombre,"Telefono":Telefono,"Correo":Correo}
    contactos.append(contacto)
    print("Contacto agregado correctamente :3")
def opcion_2():
    if len(contactos)==0:
        print("No existen contactos :(, primero agregue alguno en la opción 1!)")
    else:
        nombre_archivo = input("Ingrese nombre del archivo: ")
        with open(f"{nombre_archivo}.csv","w") as archivo:
            escritor = csv.DictWriter(archivo,["Nombre","Teléfono","Correo"])
            escritor.writeheader()
            escritor.writerows(contactos)
            print("Archivo creado con éxito :3")
            
    
