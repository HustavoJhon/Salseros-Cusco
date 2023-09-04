from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime

# Importar la librería Rich
import rich

# Define las credenciales y el alcance
scopes = ['https://www.googleapis.com/auth/spreadsheets']
key = 'credentials.json'

# Escribe aquí el ID de tu documento
spreadsheet_id = '1UYF87Lu9S7Zwa0N10KNCOrAHGty7Bc04U_iMFUFvpTk'

# Inicializa las credenciales y crea el cliente de servicio
creds = service_account.Credentials.from_service_account_file(key, scopes=scopes)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Devuelve una lista de todas las filas del documento
def get_all_rows():
    response = sheet.values().get(
        spreadsheetId=spreadsheet_id, range='Consultantes!A1:I100'
    ).execute()
    return response.get('values', [])

# Devuelve una lista de todas las filas que coinciden con el nombre especificado
def search_by_name(name):
    rows = get_all_rows()
    return [row for row in rows if row[2].lower() == name.lower()]

# Elimina la fila que coincide con el ID especificado
def delete_row(id):
    rows = get_all_rows()
    for i, row in enumerate(rows):
        if row[0] == id:
            rows.pop(i)
            break

    result = sheet.values().update(
        spreadsheetId=spreadsheet_id,
        range='Consultantes!A1:I100',
        valueInputOption='USER_ENTERED',
        body={'values': rows}
    ).execute()

    updated_cells = result.get('updates').get('updatedCells')

    if updated_cells is not None:
        print(f"Fila eliminada correctamente. {updated_cells} celdas actualizadas.")
    else:
        print("No se pudo determinar el número de celdas actualizadas.")


# Imprime el menú
def print_menu():
    rich.print(
        """
        Menú:
        1. Buscar por nombre
        2. Eliminar
        3. Salir
        """
    )


# Obtiene la entrada del usuario
def get_user_input(prompt):
    return input(prompt)


# Ejecuta el programa
def main():
    # Imprime el menú
    print_menu()

    # Obtiene la entrada del usuario
    choice = get_user_input("Ingrese su elección: ")

    # Ejecuta la acción correspondiente a la elección del usuario
    if choice == "1":
        name = get_user_input("Ingrese el nombre del consultante: ")
        rows = search_by_name(name)
        if rows:
            table = rich.table(rows)
            print(table)
        else:
            print("No se encontraron resultados.")
    elif choice == "2":
        id = get_user_input("Ingrese el ID de la fila a eliminar: ")
        delete_row(id)
    else:
        print("Saliendo...")


if __name__ == "__main__":
    main()