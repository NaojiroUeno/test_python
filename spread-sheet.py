import gspread
from oauth2client.service_account import ServiceAccountCredentials
import datetime

#ここで現在の月日を取得する
dt_now = datetime.datetime.now()
month = dt_now.month
day = dt_now.day
#　"月/日"　の形で表示
now = str(month) + '/' + str(day)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('spread-sheet-python2021-da13278bce55.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open('python_sample').sheet1

#A1セルに書きこむとバグが起きるっぽい
wks.update_acell('A2', now)
print(wks.acell('A2'))