import pandas as pd
from rich import print
import os

# Definir el nombre del archivo CSV
archivo_csv = "mi_archivo.csv"

# Función para crear una nueva fila
def crear_fila(datos):
    df = pd.read_csv(archivo_csv)
    
    # Generar automáticamente un nuevo ID
    if df.empty:
        nuevo_id = 1
    else:
        nuevo_id = df['ID'].max() + 1
    
    datos['ID'] = nuevo_id
    nueva_fila = pd.DataFrame([datos], columns=df.columns)
    df = pd.concat([df, nueva_fila], ignore_index=True)
    df.to_csv(archivo_csv, index=False)
    print("[bold green]Registro creado con éxito.[/bold green]")

# Función para contar hombres y mujeres
def contar_hombres_y_mujeres():
    df = pd.read_csv(archivo_csv)
    hombres = df[df['Sexo'] == 'Hombre'].shape[0]
    mujeres = df[df['Sexo'] == 'Mujer'].shape[0]
    print(f"Hombres: [bold blue]{hombres}[/bold blue]")
    print(f"Mujeres: [bold magenta]{mujeres}[/bold magenta]")

# Función para limpiar la consola
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

# Menú principal
while True:
    limpiar_consola()
    print("\n[bold cyan]Menú Principal:[/bold cyan]")
    print("1. Crear Registro")
    print("2. Listar Registros")
    print("3. Buscar por Nombre")
    print("4. Actualizar Registro por ID")
    print("5. Eliminar Registro por ID")
    print("6. Contar Hombres y Mujeres")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nueva_fila = {
            "Nombre": input("Ingrese el Nombre: "),
            "Teléfono": input("Ingrese el Teléfono: "),
            "Correo": input("Ingrese el Correo: "),
            "Sexo": input("Ingrese el Sexo (Hombre/Mujer): "),
            "Curso": input("Ingrese el Curso: "),
            "Horario": input("Ingrese el Horario: "),
            "Días": input("Ingrese los Días: "),
            "Promoción": input("Ingrese la Promoción: "),
            "Asistencia": input("Ingrese la Asistencia: "),
            "Descripción": input("Ingrese la Descripción: "),
            "Lugar": input("Ingrese el Lugar: "),
            "Fecha de Pago": input("Ingrese la Fecha de Pago: "),
            "Fecha de Inicio": input("Ingrese la Fecha de Inicio: "),
            "Fecha de Fin": input("Ingrese la Fecha de Fin: ")
        }
        crear_fila(nueva_fila)
    elif opcion == '2':
        df = pd.read_csv(archivo_csv)
        print(df)
    elif opcion == '3':
        nombre = input("Ingrese el nombre a buscar: ")
        df = pd.read_csv(archivo_csv)
        resultado = df[df['Nombre'] == nombre]
        if not resultado.empty:
            print(resultado)
        else:
            print(f"No se encontraron registros para el nombre '{nombre}'.")
    elif opcion == '4':
        ID = int(input("Ingrese el ID del registro a actualizar: "))
        nuevos_datos = {"Edad": int(input("Ingrese la nueva Edad: "))}
        actualizar_registro_por_id(ID, nuevos_datos)
    elif opcion == '5':
        ID = int(input("Ingrese el ID del registro a eliminar: "))
        eliminar_registro_por_id(ID)
    elif opcion == '6':
        contar_hombres_y_mujeres()
    elif opcion == '7':
        break
    else:
        print("[bold red]Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5/6/7).[/bold red]")
