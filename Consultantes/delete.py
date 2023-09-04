from googleapiclient.discovery import build
from google.oauth2 import service_account

scopes = ['https://www.googleapis.com/auth/spreadsheets']
key = 'credentials.json'

# Escribe aquí el ID de tu Documento
spreadsheet_id = '1UYF87Lu9S7Zwa0N10KNCOrAHGty7Bc04U_iMFUFvpTk'

creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Función para buscar por nombre
def search_by_name(name):
    response = sheet.values().get(
        spreadsheetId=spreadsheet_id, range='Consultantes!A2:I100'
    ).execute()
    values = response.get('values', [])
    return [row for row in values if row[2].lower() == name.lower()]

# Función para mostrar una fila completa
def show_row(row):
    print("ID:", row[0])
    print("Sexo:", row[1])
    print("Nombre:", row[2])
    print("Teléfono:", row[3])
    print("Fecha:", row[4])
    print("Detalle:", row[5])
    print("Tipo:", row[6])
    print("Lugar:", row[7])
    print("Descripción:", row[8])

# Función para eliminar una fila por ID
def delete_row_by_id(id):
    # Encuentra la fila con el ID deseado
    rows = search_by_name(id)
    if not rows:
        print(f"No se encontró una fila con el ID {id}.")
        return

    # Obtiene la fila y rango de celdas correspondiente
    row = rows[0]
    start_cell = f'A{int(row[0]) + 1}'
    end_cell = f'I{int(row[0]) + 1}'

    # Elimina la fila utilizando el rango de celdas
    sheet.values().clear(spreadsheetId=spreadsheet_id, range=f'Consultantes!{start_cell}:{end_cell}').execute()
    print(f"Fila con ID {id} eliminada correctamente.")

# ...

# Solicita al usuario el nombre a buscar
name = input("Ingrese el nombre a buscar: ")

# Busca el nombre en la hoja de cálculo
rows = search_by_name(name)

# Si se encontró el nombre, muestra la fila completa
if rows:
    row = rows[0]
    show_row(row)
    print("¿Está seguro de que desea eliminar esta fila?")
    print("1. Sí, eliminar")
    print("2. No, cancelar")
    choice = input("Seleccione una opción (1/2): ")
    if choice == "1":
        # Elimina la fila
        delete_row_by_id(row[0])
        print("Fila eliminada correctamente.")
    elif choice == "2":
        print("Operación de eliminación cancelada.")
    else:
        print("Opción no válida. La fila no ha sido eliminada.")
else:
    print("No se encontró el nombre.")
