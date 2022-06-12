import json
import gspread
from google.oauth2.service_account import Credentials

# connect to your google sheet
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('key.json', scopes=scope)
gc = gspread.authorize(credentials)
wks = gc.open("your spreadsheet name").sheet1

# Let's say you have some json values
x =  '{ "receiver_email_1":6, "receiver_email_2":8, "receiver_email_3":10 }'
y = json.loads(x)

result = []
for key in y:
    result.append([key,y[key]])

wks.update('A1', result)