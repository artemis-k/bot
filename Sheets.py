import gspread
import json
from google.oauth2.service_account import (Credentials as ServiceAccountCredentials)

# Файл, полученный в Google Developer Console
gc = gspread.service_account(filename='creds.json')
#ID Google Sheets документа
sh = gc.open_by_key("1EMpg8-zLWytFHIHPA_JzLOkBA6U7m4wKv33XetenSVg")

DEFAULT_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive',
]
with open('creds.json', 'r') as f:
    credentials = json.load(f)
creds = ServiceAccountCredentials.from_service_account_info(credentials, scopes=DEFAULT_SCOPES)
gc = gspread.Client(auth=creds)

worksheet = sh.sheet1

### retrieve data ###

res = worksheet.get_all_records() # list of dictionaries
print(res[0])
print(res[1])