import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1BJDDRTPsr4Pxinz1Ob2HMoK2gXJ3tkRnqov0Oczs06I"
sheet = client.open_by_key(sheet_id).sheet1

# sheet.update_cell(1, 1, "Hello, World")
values_list = sheet.get_all_values()
print(values_list)
