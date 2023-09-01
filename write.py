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
id_autoincrement = 0  # Inicializa el ID autoincrementable
while True:
    sexo = input("Ingrese Sexo (M/F): ").upper()
    if sexo not in ('M', 'F'):
        print("El sexo debe ser 'M' o 'F'. Inténtelo de nuevo.")
        continue
    
    nombre = input("Ingrese Nombre: ").capitalize()
    telefono = input("Ingrese Teléfono: ")
    fecha = datetime.now().strftime('%d/%m/%Y')
    
    lugar = input("Ingrese Lugar (limacpampa/prado): ").lower()
    if lugar not in ('limacpampa', 'prado'):
        print("El lugar debe ser 'limacpampa' o 'prado'. Inténtelo de nuevo.")
        continue
    
    detalle = input("Ingrese Detalle: ")
    tipo = input("Ingrese Tipo: ")
    descripcion = input("Ingrese Descripción: ")

    # Construye los valores a insertar
    values_to_insert = [[str(id_autoincrement + 1), sexo, nombre, telefono, fecha, detalle, tipo, lugar, descripcion]]

    # Intenta enviar los datos y maneja los errores si ocurren
    try:
        result = sheet.values().append(
            spreadsheetId=spreadsheet_id,
            range='Consultantes!A1',  # NombreDeLaPagina
            valueInputOption='USER_ENTERED',
            body={'values': values_to_insert}
        ).execute()

        updated_cells = result.get('updates').get('updatedCells')

        if updated_cells is not None:
            print(f"Datos insertados correctamente en 'NombreDeLaPagina'. {updated_cells} celdas actualizadas.")
        else:
            print("No se pudo determinar el número de celdas actualizadas.")

    except Exception as e:
        print(f"Ocurrió un error al insertar datos: {str(e)}")

    id_autoincrement += 1
