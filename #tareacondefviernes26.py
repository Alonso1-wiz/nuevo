#tareacondef
import os
os.system("cls")
from colorama import Fore, init
init()
contactos=[]
def Agregar_contacto():
    while True:
        try:
            nombre=input(Fore.RESET+"Ingrese nombre del contacto: ")
            if nombre.strip()=="":
                raise ValueError(Fore.RED+"El nombre no puede estar vacio")# lo mismo, enumeramos el error como raise valueerror, y abajo lo retorna
            if not nombre.isalpha():
                raise ValueError(Fore.RED+"El nombre solo debe contener letras, sin numeros ni simbolos")#enumaramos raise y abajo podemos retornar el error
            print(f"Nombre valido: {nombre}")
            break
        except ValueError as e:#aqui retornamos el error, utiilizando (value error "as" e y print "error" e, para devolver el error mencionado arriba)
            print("Error",e)
    while True:
        try:
            numero=int(input(Fore.RESET+"Ingrese numero del contacto: "))
            if numero<=0:
                print(Fore.RED+"Ingrese un numero entero correcto")
            else: 
                contacto={"nombre":nombre, "numero":numero}
                contactos.append(contacto)
                break
        except ValueError:
            print(Fore.RED+"Ingrese solo numeros")
def Buscar_contacto():
    if contactos==[]:
        print(Fore.RED+"No hay contactos disponibles")
    else:
        busqueda=input(Fore.RESET+"Ingrese el nombre del contacto: ")
        for contacto in contactos:
            if busqueda== contacto["nombre"]:
                print(Fore.GREEN+"Contacto disponible")
                print(f"nombre: {contacto["nombre"]},n\numero: {contacto["numero"]}")
            elif busqueda !=contacto["nombre"]:
                print(Fore.BLUE+"Contacto no encontrado")
def Modificar_contacto():
    if contactos==[]:
        print(Fore.RED+"No hay contactos disponibles")
    else:
        modificar=input(Fore.RESET+"Ingrese el nombre del contacto: ")
        for contacto in contactos:
            if modificar== contacto["nombre"]:
                print(Fore.GREEN+"Contacto disponible")
                contacto["numero"]=int(input("Ingrese el nuevo numero del contacto: "))
            else:
                print(Fore.RED+"Contacto no disnponible")

def Eliminar_contacto():
    if contactos==[]:
        print(Fore.RED+"NO hay contacsos disponibles")
    else:
        eliminar=input(Fore.RESET+"Ingrese nombre del contacto que desea eliminar: ")
        for contacto in contactos:
            if eliminar == contacto["nombre"]:
                print(Fore.RED+"Contacto encontrado. eliminando")
                contactos.remove(contacto)
            elif eliminar!=contacto["nombre"]:
                print(Fore.BLUE+"Cntacto no encontrado")
def Mostrar_contacto():
    if contactos==[]:
        print(Fore.RED+"No hay contactos disnponibles aun")
    else:
        for a in range(len(contactos)):
            print(f"contacto: {a+1}")
            for clave,valor in contactos[a].items():
                print(f"{clave} : {valor}")

def menu():
    while True:
        print(Fore.GREEN+"**Menu**")
        print(Fore.RESET+"1_Agregar contacto")
        print("2_Buscar contactos")
        print("3_Modificar contactos")
        print("4_Eliminar contacto")
        print("5_Mostrar contactos")
        print("6_Salir")
        try:
            op=int(input(Fore.RESET+"Ingrese una opcion: "))
            if op==1:
                print("Agregar contacto")
                Agregar_contacto()
            elif op==2:
                print("Buscar contacto")
                Buscar_contacto()
            elif op==3:
                print("Modificar contacto")
                Modificar_contacto()
            elif op==4:
                print("Eliminar contacto")
                Eliminar_contacto()
            elif op==5:
                print("Mostrar contactos")
                Mostrar_contacto()
            elif op==6:
                print(Fore.BLUE+"Adios")
                break
            else:
                print(Fore.RED+"Ingrese alguna de las opciones disponibles")
        except ValueError:
            print(Fore.RED+"Ingrese solo un numero entero o las opciones disponibles")
menu()