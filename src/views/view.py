
#1. Crear la interfaz en consola para el consumo de la API desde el CLI
import requests

BASE_URL = "https://t1-fastapi-3quc.onrender.com"

# 1. Función que simula el formulario en consola para crear un aprendiz
def crear_aprendiz():
    print("\n--- FORMULARIO DE REGISTRO DE APRENDIZ ---")
    document = input("Ingrese el documento: ")
    first_name = input("Ingrese el nombre (first_name): ")
    last_name = input("Ingrese el apellido (last_name): ")
    email = input("Ingrese el correo electrónico (email): ")
    
    # Convertimos a entero los campos numéricos
    try:
        age = int(input("Ingrese la edad (age): "))
        record_number = int(input("Ingrese el número de ficha (record_number): "))
    except ValueError:
        print("\n[!] Error: La edad y el número de ficha deben ser números enteros.")
        return

    program = input("Ingrese el programa de formación (program): ")

    # Estructura del JSON que espera tu API
    data = {
        "document": document,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "program": program,
        "record_number": record_number
    }

    try:
        # Petición POST a tu API desplegada en Render
        response = requests.post(f"{BASE_URL}/trainee/", json=data)
        
        if response.status_code in [200, 201]:
            print("\n ¡Aprendiz registrado con éxito en la base de datos!")
            print(response.json())
        else:
            print(f"\n[X] Error del servidor (Código {response.status_code}):")
            print(response.json())
            
    except requests.exceptions.RequestException as e:
        print(f"\n[X] No se pudo conectar a la API: {e}")

# 2. Función extra para ver la lista de aprendices
def listar_aprendices():
    print("\n--- LISTA DE APRENDICES REGISTRADOS ---")
    try:
        response = requests.get(f"{BASE_URL}/trainees/")
        if response.status_code == 200:
            aprendices = response.json()
            if not aprendices:
                print("No hay aprendices registrados todavía.")
            for idx, a in enumerate(aprendices, start=1):
                print(f"{idx}. {a.get('first_name')} {a.get('last_name')} - {a.get('program')}")
        else:
            print("Error al obtener los datos.")
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")

# 3. Menú principal en consola
def menu():
    while True:
        print("\n==============================")
        print("    GESTOR DE APRENDICES CLI")
        print("==============================")
        print("1. Registrar nuevo aprendiz (Formulario)")
        print("2. Ver todos los aprendices")
        print("3. Salir")
        
        opcion = input("\nElige una opción (1-3): ")
        
        if opcion == "1":
            crear_aprendiz()
        elif opcion == "2":
            listar_aprendices()
        elif opcion == "3":
            print("\n¡Saliendo del sistema CLI. Hasta luego!")
            break
        else:
            print("\n[!] Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()