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


# llamada a la api
result = sheet.values().get(spreadsheetId=spreadsheet_id, range='Consultantes!A1:A2').execute()

#extraemos values del resultado
values = result.get('values',[])
print(values)