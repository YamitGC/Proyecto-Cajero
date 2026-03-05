from clean_screen import *
from progress_bar import *
from logica_atm import *

def menu(usuario):
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Historial")
    print("5. Salir del cajero")

    opcion = int(input("Ingresa la opcion (1-5): "))

    if opcion == 1:
        clean_screen()
        progress_bar()
        consultar_saldo(usuario)
        
    
    elif opcion == 2:
        clean_screen()
        progress_bar()
        depositar_dinero(usuario)
    
    elif retirar_dinero(usuario):
        clean_screen()
        progress_bar()
        print("Hola")

    elif opcion == 4:
        clean_screen()
        progress_bar()
        print("Hola")

    elif opcion == 5:
        print("Cerrando el cajero...")

    else:
        print("Opcion incorrecta, dijite una opcion valida (1-5).")

if __name__ == "__main__":
    menu()
     

