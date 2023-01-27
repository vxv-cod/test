import urllib.request
import win32com.client
from time import sleep
from rich import print

def GO():
    '''url, на котором находится список преподователей'''
    link = urllib.request.urlopen(r'file:///C:/Users/vvkhomutskiy/Desktop/27.html')
    lines = []
    for line in link.readlines():
        '''взяли все строки с сотрудниками'''
        '''Каждый сотрудник начинается с тегов <li><a href .....'''
        if line.find(b'<nobr>') != -1 or (line.find(b'<td colspan="6">') != -1 and b'<td colspan="6"><b></b></td>' not in line):
            lines.append(line)
    link.close()

    '''Переводим bytes в str'''
    for i in range(len(lines)):
        lines[i] = lines[i].decode('utf-8')


    datatimes = []
    totals = []
    pokrit = []
    zond = []
    text0 = ''
    for i in range(len(lines)):
        'Зонд, группа, устройство'
        if lines[i].find('<td colspan="6">') != -1:
            text0 = lines[i][lines[i].find('<td colspan="6">') + 16 : lines[i].find('</td>')]

        if lines[i].find('<nobr>') != -1:
            'Дата и время'
            text1 = lines[i][lines[i].find('<nobr>') + 6 : lines[i].find('</nobr>')]
            'Всего'
            text2 = lines[i][lines[i].find('всего">') + 7 : lines[i].find('</td><td class="col-coverage')]
            if '&nbsp;' in text2:
                text2 = '0%'
            if '&lt;1 %' in text2:
                text2 = '1%'
            zond.append(text0)
            datatimes.append(text1)
            totals.append(text2)


    Excel = win32com.client.Dispatch("Excel.Application")
    Excel.Visible = 1
    # wb = Excel.ActiveWorkbook
    wb = Excel.Workbooks.Add()
    sheet = wb.ActiveSheet

    failName = wb.Name
    data = [[failName, zond[i], datatimes[i], totals[i]] for i in range(len(datatimes))]
    data = [['Имя файла', 'Зонд, группа, устройство', 'Дата и время', 'Всего']] + data


    def exportdata(data, sheet, StartRow, StartCol, EndRow, EndCol):
        '''Отправляем данные в диапозон ячеек'''
        if StartCol == EndCol:
            data = [(i, None) for i in data]
        sheet.Range(sheet.Cells(StartRow, StartCol), sheet.Cells(EndRow, EndCol)).Formula = data

    EndRow = len(data)
    exportdata(data, sheet, 1, 1, EndRow, 4)
    sleep(1)

    cels = sheet.Range(sheet.Cells(1, 1), sheet.Cells(EndRow, 4))
    cels.Select
    sheet.ListObjects.Add(1, cels, True, 1)

    cels = sheet.Range(sheet.Cells(1, 1), sheet.Cells(1, 4))
    for i in cels:
        i.Font.Bold == True
        i.HorizontalAlignment = 3

    ColSelect = sheet.Columns("A:D")
    ColSelect.EntireColumn.AutoFit()




def start():
    directory = str(ui.plainTextEdit.toPlainText())[8:]
    print(f"directory = {directory}")




    GO()