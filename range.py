import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

# Define las credenciales y el alcance
scopes = ['https://www.googleapis.com/auth/spreadsheets']
key = 'credentials.json'

# Escribe aquí el ID de tu documento
spreadsheet_id = '1UYF87Lu9S7Zwa0N10KNCOrAHGty7Bc04U_iMFUFvpTk'

# Inicializa las credenciales y crea el cliente de servicio
creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Solicita al usuario ingresar datos
id_autoincrement = 0
while True:
    sexo = input("Ingrese sezo (M/F): ").upper()
    nombre = input("Ingrese Nombre")

# Función para contar cuántos alumnos hay
def contar_alumnos():
    try:
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range='Consultantes'
        ).execute()
        
        values = result.get('values', [])
        if not values:
            print("No hay datos en la hoja.")
            return
        else:
            num_alumnos = len(values) - 1  # Resta 1 para excluir la fila de encabezado
            print(f"Total de alumnos: {num_alumnos}")

    except Exception as e:
        print(f"Ocurrió un error al contar alumnos: {str(e)}")

# Función para buscar por nombre
def buscar_por_nombre(nombre_buscar):
    try:
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range='Consultantes'
        ).execute()

        values = result.get('values', [])
        if not values:
            print("No hay datos en la hoja.")
            return

        df = pd.DataFrame(values[1:], columns=values[0])  # Crea un DataFrame excluyendo la fila de encabezado
        resultado = df[df['Nombre'] == nombre_buscar]

        if not resultado.empty:
            print("Resultados de la búsqueda:")
            print(resultado)
        else:
            print(f"No se encontraron registros para el nombre '{nombre_buscar}'.")

    except Exception as e:
        print(f"Ocurrió un error al buscar por nombre: {str(e)}")

# Función para eliminar filas
def eliminar_fila(fila):
    try:
        result = sheet.values().get(
            spreadsheetId=spreadsheet_id,
            range='Consultantes'
        ).execute()

        values = result.get('values', [])
        if not values:
            print("No hay datos en la hoja.")
            return

        df = pd.DataFrame(values[1:], columns=values[0])  # Crea un DataFrame excluyendo la fila de encabezado

        # Encuentra el índice de la fila a eliminar
        index_to_delete = df[df['ID'] == fila].index

        if not index_to_delete.empty:
            df = df.drop(index_to_delete)  # Elimina la fila
            df.reset_index(drop=True, inplace=True)  # Reajusta los índices
            df.insert(0, 'ID', range(1, len(df) + 1))  # Reajusta los IDs

            # Actualiza la hoja de Google Sheets con el DataFrame actualizado
            values_to_update = df.values.tolist()
            result = sheet.values().update(
                spreadsheetId=spreadsheet_id,
                range='Consultantes',
                valueInputOption='RAW',
                body={'values': [df.columns.tolist()] + values_to_update}
            ).execute()

            updated_cells = result.get('updatedCells')
            if updated_cells is not None:
                print(f"Fila {fila} eliminada correctamente. {updated_cells} celdas actualizadas.")
            else:
                print("No se pudo determinar el número de celdas actualizadas.")

        else:
            print(f"No se encontró una fila con el ID {fila}.")

    except Exception as e:
        print(f"Ocurrió un error al eliminar fila: {str(e)}")

# Función principal
def main():
    while True:
        print("\nMenú Principal:")
        print("1. Contar Alumnos")
        print("2. Buscar por Nombre")
        print("3. Eliminar Fila")
        print("4. Salir")

        opcion = input("Seleccione una opción (1/2/3/4): ")

        if opcion == '1':
            contar_alumnos()
        elif opcion == '2':
            nombre_buscar = input("Ingrese el nombre a buscar: ").capitalize()
            buscar_por_nombre(nombre_buscar)
        elif opcion == '3':
            fila = int(input("Ingrese el ID de la fila a eliminar: "))
            eliminar_fila(fila)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida (1/2/3/4).")

if __name__ == "__main__":
    main()
