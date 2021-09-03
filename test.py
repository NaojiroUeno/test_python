from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "タイトル"
10
ws['A1']="Pythonで書いたExcelです"
11
wb.save('Pythonで作成したExcelシート.xlsx')