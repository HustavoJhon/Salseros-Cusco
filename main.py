import pandas as pd
import csv


# Definir el nombre del archivo CSV
archivo_csv = "data.csv"


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
    print("Registro creado con éxito.")
    

# Función para leer todos los registros
def listar_registros():
    df = pd.read_csv(archivo_csv)
    print(df)

# Función para buscar registros por nombre
def buscar_por_nombre(nombre):
    df = pd.read_csv(archivo_csv)
    resultado = df[df['NOMBRE'] == nombre]
    if not resultado.empty:
        print(resultado)
    else:
        print(f"No se encontraron registros para el nombre '{nombre}'.")

# Función para actualizar un registro por ID
def actualizar_registro_por_id(ID, nuevos_datos):
    df = pd.read_csv(archivo_csv)
    indice = df.index[df['ID'] == ID]
    
    if not indice.empty:
        indice = indice[0]
        for columna, valor in nuevos_datos.items():
            df.at[indice, columna] = valor
        df.to_csv(archivo_csv, index=False)
        print(f"Registro con ID {ID} actualizado.")
    else:
        print(f"No se encontró un registro con el ID {ID}.")

# Función para eliminar un registro por ID
def eliminar_registro_por_id(ID):
    df = pd.read_csv(archivo_csv)
    indice = df.index[df['ID'] == ID]
    
    if not indice.empty:
        indice = indice[0]
        df = df.drop(index=indice).reset_index(drop=True)
        df.to_csv(archivo_csv, index=False)
        print(f"Registro con ID {ID} eliminado.")
    else:
        print(f"No se encontró un registro con el ID {ID}.")

# Menú principal
while True:
    print("\nMenú Principal:")
    print("1. Crear Registro")
    print("2. Listar Registros")
    print("3. Buscar por Nombre")
    print("4. Actualizar Registro por ID")
    print("5. Eliminar Registro por ID")
    print("6. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    if opcion == '1':
        nueva_fila = {
            "NOMBRE": input("Ingrese el Nombre: "),
            "TELEFONO": input("Ingrese el Teléfono: "),
            "CORREO": input("Ingrese el Correo: "),
            "SEXO": input("Ingrese el Sexo: "),
            "CURSO": input("Ingrese el Curso: "),
            "HORARIO": input("Ingrese el Horario: "),
            "HORA": input("Ingrese los Días: "),
            "ASISTENCIA": input("Ingrese la Asistencia: "),
            "DESCRIPCION": input("Ingrese la Descripción: "),
            "PAGO": input("Ingrese la Fecha de Pago: "),
            "INICIO": input("Ingrese la Fecha de Inicio: "),
            "FIN": input("Ingrese la Fecha de Fin: ")
        }
        crear_fila(nueva_fila)
    elif opcion == '2':
        listar_registros()
    elif opcion == '3':
        nombre = input("Ingrese el nombre a buscar: ")
        buscar_por_nombre(nombre)
    elif opcion == '4':
        ID = int(input("Ingrese el ID del registro a actualizar: "))
        nuevos_datos = {"ASISTENCIA": input("Asistencia: ")}
        actualizar_registro_por_id(ID, nuevos_datos)
    elif opcion == '5':
        ID = int(input("Ingrese el ID del registro a eliminar: "))
        eliminar_registro_por_id(ID)
    elif opcion == '6':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4/5/6).")