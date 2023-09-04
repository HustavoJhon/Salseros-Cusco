from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

scopes = ['https://www.googleapis.com/auth/spreadsheets']
key = 'credentials.json'

# Escribe aqui el Id de tu Docuemnto
spreadsheet_id = '1UYF87Lu9S7Zwa0N10KNCOrAHGty7Bc04U_iMFUFvpTk'


creds = None
creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()


# Funcion para buscar por nombre
def search_by_name(name):
    response = sheet.values().get(
        spreadsheetId=spreadsheet_id, range='Consultantes!A1:I100'
    ).execute()
    values = response.get('values', [])
    return [row for row in values if row[2].lower() == name.lower()]


# Funcion para mostrar una fila completa
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


# Solicita al usuario el nombre a buscar
name = input("Ingrese el nombre a buscar: ")

# Busca el nombre en la hoja de cálculo
rows = search_by_name(name)

# Si se encontró el nombre, muestra la fila completa
if rows:
    row = rows[0]
    show_row(row)
else:
    print("No se encontró el nombre.")
