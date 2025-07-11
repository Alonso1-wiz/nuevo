
# ZAPATILLAS STRIKE - RESERVAS

reservas = {}

def reservar_zapatillas():
    print("-- Reservar Zapatillas --")
    nombre = input("Nombre del comprador: ").strip()
    
    if nombre in reservas:
        print("Ya existe una reserva con ese nombre.")
        return
    
    total_pares = sum(reservas.values())
    if total_pares >= 20:
        print("No hay stock disponible para más reservas.")
        return
    
    clave = input("Digite la palabra secreta para confirmar la reserva: ").strip()
    if clave != "EstoyEnListaDeReserva":
        print("Palabra secreta incorrecta. No se puede realizar la reserva.")
        return
    
    #
def buscar_reservas():
    print("-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ").strip()
    
    if nombre in reservas:
        pares = reservas[nombre]
        tipo = "VIP" if pares == 2 else "estándar"
        print(f"Reserva encontrada: {nombre} - {pares} par(es) ({tipo}).")
        
        if pares == 1:
            respuesta = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").strip().lower()
            if respuesta == "s":
                reservas[nombre] = 2
                print(f"Reserva actualizada a VIP. Ahora {nombre} tiene 2 pares reservados.")
            else:
                print("Manteniendo reserva actual.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")
def cancelar_reserva():
    print("-- Cancelar Reserva --")
    nombre = input("Nombre del comprador cuya reserva desea cancelar: ").strip()
    
    ##

def menu():
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Cancelar reserva de zapatillas")
        print("4.- Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            reservar_zapatillas()
        elif opcion == "2":
            buscar_reservas()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

menu()