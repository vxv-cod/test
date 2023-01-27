# from rich import print
# from rich import inspect
import os
os.system('CLS')
# aaa = 5
# bbb = 9
# ccc = 15
# if aaa == 1 or bbb == 1 or ccc == 15:
#     print("+++++++++++++++")
# ddd , lll = 555, 888

# print(ddd)
# print(lll)

# import numpy as np
# aaa = [0.253, 0.256, 0.244, 0.261, 0.244, 0.319, 0.264, 0.277, 0.273, 0.256]
# lll = np.std(aaa, ddof = 1.0)
# print(lll)


# aaa = [[111], [222, 333]]
# xxx = [aaa[g] + aaa[g + 1] for g in range(0, len(aaa) - 1)]
# sss = aaa[0] + aaa[1]
# print(f"sss = {sss}")
# print(f"xxx = {xxx}")

# print(f"sum(aaa) = {sum(aaa)}")

# prom = []
# prom = tuple([None] * 7)
# print(f"prom = {prom}")
# prom = None, None, None, None, None, None, None
# print(f"prom000 = {prom}")


# dict = {}
# for x in codeNomer:
#     xxx = []
#     for i in datasort:
#         if i[-1] == x:
#             xxx.append(i)
#     dict[x] = xxx

# import numpy as np
# # sssssss = 0.196339434276206
# sssssss = 0.44, 0.428140097


# dddd = np.std(sssssss, ddof = 1.0)
# print(f"0000000000000 = {dddd}")


# import sys, traceback, os
# from PyQt5 import QtCore, QtWidgets
# # os.system('CLS')

# app = QtWidgets.QApplication(sys.argv)

# def SMS(Text):
#     QtWidgets.QMessageBox.information(QtWidgets.QWidget(), 'Ошибка', Text)

# def GO():
#     try:
#         a = 5 / 0
#         print(f"a = {a}")
#     except:
#         SMS(traceback.format_exc())


# if __name__ == "__main__":
#     GO()
#     # SMS("Проверка")
#     # app = QtWidgets.QApplication(sys.argv)
#     sys.exit(app.exec_())    


# mygenerator = (x*x for x in range(3))
# mygenerator = [x*x for x in range(3)]
# print(f"mygenerator = {mygenerator}")
# for i in mygenerator :
#     print(i)
# for i in mygenerator :
# #     print(i)

# aaa = [1,3,5,7]

# def aaafff(aaa):
#     yield from aaa
#         # print(i)
# # bbb = [8,9,10,11]
# ddd = aaafff(aaa)
# # for b in ddd:
# #     print(b)
# print(next(ddd))
# print(next(ddd))
# # print(next(ddd))
# # print(next(ddd))




# import wmi
 
# # Initializing the wmi constructor
# f = wmi.WMI()
 
# # Printing the header for the later columns
# print("pid   Process name")
 
# # Iterating through all the running processes
# for process in f.Win32_Process():
     
#     # Displaying the P_ID and P_Name of the process
#     print(f"{process.ProcessId:<10} {process.Name}")



# import wmi
# import win32com.client
# f = wmi.WMI()
# for process in f.Win32_Process():
#     if process.Name == 'EXCEL.EXE':
#         print(f"EXCEL")
#         Excel = win32com.client.Dispatch("Excel.Application")
#         wb = Excel.ActiveWorkbook
#         print(f"wb = {wb}")


# import os
# import sys
# os.system('CLS')
# import win32com.client
# import subprocess


# # progs = str(subprocess.check_output('tasklist'))
# progs = subprocess.check_output('tasklist')
# # tasks = str(subprocess.check_output('tasklist').split("\r\n"))
# print(progs)
# # for prog in tasks:
# #     if prog == win32com.client.Dispatch("Excel.Application"):
# #         print(prog)
# # for process_name in progs:
# #     if process_name == 'EXCEL.EXE':
# #         print(f"EXCEL")

# import subprocess
# progs = subprocess.check_output('tasklist').Name()
# for process_name in progs:
#     print(f"{process_name}")
#     # if process_name == 'EXCEL.EXE':
#     #     print(f"{process_name}")

# oExcel = win32com.client.Dispatch("Excel.Application")
# XL = sys.Runtime.InteropServices.Marshal.GetActiveObject("Excel.Application")


# import win32com.client as win32

# excel = win32.gencache.EnsureDispatch('Excel.Application')
# excel = win32com.client.GetActiveObject(ProgID=15448)
# excel = win32com.client.GetActiveObject('Excel.Application')




# excel = win32com.client.GetActiveObject('Excel.Application')
# for wb in excel.Workbooks:
#     print(wb.Name)




# inspect(win32.gencache.EnsureDispatch)

# wb = win32com.client
# wb = System.Runtime.InteropServices.Marshal.BindToMoniker
# Excel = Microsoft.Office.Interop.Excel
# inspect(wb)




# import subprocess
# '''Ищем запущен ли процесс acad.exe'''
# def process_exists(process_name):
#     progs = str(subprocess.check_output('tasklist'))
#     if process_name in progs:
#         return True
#     else:
#         return False

# if process_exists('EXCEL.EXE'):
#     print("Найдено подключение к Excel")    
# else:
#     pass

# process_exists('EXCEL.EXE')

# progs = str(subprocess.check_output('tasklist'))

# subprocess.check_output( "taskkill /F /IM excel.exe")

"""tasklist /F /IM excel.exe"""


# import win32com.client

# def find_process(name):
#     objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
#     objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
#     colItems = objSWbemServices.ExecQuery(
#          f"Select * from Win32_Process where Caption = '{name}'")
            # "SELECT * FROM Win32_Process WHERE Name = 'EXCEL.EXE'"
    
#     Excel = win32com.client.GetActiveObject('Excel.Application')
#     # inspect(colItems[0]Excel.ActiveWorkbook.Name)
#     inspect(colItems[0])
#     inspect(colItems[1])
#     return len(colItems)

# print (find_process("EXCEL.EXE"))




# import win32com.client

# def find_process(name):
#     objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
#     objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
#     procExcel = objSWbemServices.ExecQuery(
#          f"Select * from Win32_Process where Caption = '{name}'")
#     # inspect(procExcel)
#     return procExcel

# print (find_process("EXCEL.EXE"))

# procExcel = find_process("EXCEL.EXE")
# inspect(procExcel[0])

# HandleExcels = [i.Handle for i in procExcel]
# inspect(HandleExcels)





# xxllxx = []
# for proc in procExcel:
#     # Excel = win32com.client.Dispatch("Excel.Application")
#     inspect(proc)
#     # Excel = win32com.client.GetObject(r"C:\Users\\vvkhomutskiy\AppData\Local\Temp" + "\"" + FileToOpen)
#     xxllxx.append(Excel)
    

# print (f"xxllxx = {xxllxx}")
# inspect(procExcel[0])
# inspect(xxllxx[2])
# wb = xxllxx[0].ActiveWorkbook
# wb.Close()


# # fff = procExcel[0].ExecutablePath
# # print(f"fff = {fff}")
# Excel = win32com.client.GetActiveObject('Excel.Application')
# print (f"Excel = {dir(Excel)}")
# inspect(Excel)
# # inspect(Excel.CLSID)
# # inspect(Excel.coclass_interfaces)
# # wb = procExcel[0].Workbooks.Open(f"{fff}")
# # procExcel[0].ActiveWorkbook.Name
# # print (procExcel[0].Workbook.Name)



# import ctypes
# import win32gui
# from ctypes import*
# xxx = ctypes.windll.user32
# fff = xxx.FindWindow = "HWND"
# inspect(fff)  
# hWndThis = fff(0, 0)
# title = win32gui.GetWindowText("hwnd")

# FindWindow = FindWindowFunction(None,None,1)
# hwnds = FindWindow()



# inspect(subprocess.signal)


# import win32gui

# def enumHandler(hwnd, lParam):
#     if win32gui.IsWindowVisible(hwnd):
#         if 'Stack Overflow' in win32gui.GetWindowText(hwnd):
#             win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)

# fff = win32gui.EnumWindows(enumHandler, None)
# inspect(fff)










# import ctypes
# import win32gui
# EnumWindows = ctypes.windll.user32.EnumWindows
# EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
# GetWindowText = ctypes.windll.user32.GetWindowTextW
# GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
# IsWindowVisible = ctypes.windll.user32.IsWindowVisible

# titles = []
# objectExList = []
# def foreach_window(hwnd, lParam):
#     if IsWindowVisible(hwnd):
#         length = GetWindowTextLength(hwnd)
#         buff = ctypes.create_unicode_buffer(length + 1)
#         GetWindowText(hwnd, buff, length + 1)
#         titles.append((hwnd, buff.value))
#     return True
# EnumWindows(EnumWindowsProc(foreach_window), 0)

# for i in range(len(titles)):
#     # print(titles)[i]
#     # print(titles[i])
#     xxx = titles[i][1]
    
#     if "- Excel" in  xxx:
#         # print(titles[i][0], " ", xxx)
#         objectExList.append(titles[i])
#         inspect(titles[i])
#         print(i)
        
        # titles[i].Workbook.Name

# # fff = ctypes.windll.user32.MoveWindow(titles[5][0], 0, 0, 760, 500, True)
# # inspect(fff)
# fff = ctypes.windll.user32.MoveWindow(titles[4][0], 0, 0, 1000, 1000, True)
# titles[4][0].Save()
# # inspect(fff.ActiveWorkbook.Name)
# # wb.Activate()
# fff.SaveAs(r"C:\Users\vvkhomutskiy\Desktop\999", FileFormat=1, CreateBackup=0)
# inspect(fff)
# # inspect(titles[1])
# print(objectExList)

# # print(objectExList[-1][0])
# fff = rf"C:\Users\\vvkhomutskiy\AppData\Local\Temp\{objectExList[0][1]}"[:-8]
# print(fff)
# # Excel = win32com.client.GetObject(fff)
# # SH_Excel = win32com.client.Dispatch("Excel.Application")
# # print(SH_Excel)
# # SH_wb = SH_Excel.Workbooks.Open(fff)

# # import pymem    
# # import pymem.process   






'''Скрипт из EVA'''
# import os
# import win32com.client
# from time import sleep
# os.system('CLS')

# def find_process():
#     objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
#     objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
#     colItems = objSWbemServices.ExecQuery(
#             # f"Select * from Win32_Process where Caption = '{name}'")
#             f"SELECT * FROM Win32_Process WHERE Name = 'EXCEL.EXE'")
#     return colItems

# colExcelInstances = find_process()
# # inspect(colExcelInstances)

# strPath = r"C:\vxvproj\tnnc-Excel\CorrectReportApp\CorrectReport\Сметы"
# inspect(strPath)
# os.getcwd() + "\savefile"
# # strPath = os.getcwd() + "\Сметы"
# inspect(strPath)
# for objInstancei in colExcelInstances:
#     objExcel = win32com.client.GetObject(None, "Excel.Application")
#     objExcel.DisplayAlerts = False      # отключение уведомлений с ответом по умолчанию для сохранения без подтверждения
#     for objWorkbook in objExcel.Workbooks:
#         strFileExtension = ".xlsx"
#         if objWorkbook.FileFormat == 52:
#             strFileExtension = ".xlsm"
#         objWorkbook.SaveAs(f"{strPath}\\{objWorkbook.Name}{strFileExtension}", FileFormat=objWorkbook.FileFormat, CreateBackup=0)
#         objWorkbook.Close(False)
#     objExcel.Quit()
#     objExcel = None
#     objInstancei.Terminate
#     sleep(1)


# S = "  Составил: ___________________________Е.В. Шукалова  "
# # xxx = textsost.find('_', 0, -1)
# xxx = S.find('_')
# print(f"xxx = {xxx}")
# '''Возвращает номер последнего вхождения или -1'''
# xxx = S.rfind('_')
# print(f"xxx = {xxx}")

# xxx = len(S)
# print(f"xxx = {xxx}")
# '''Удаление пробельных символов в начале и в конце строки'''
# xxx = S.strip()
# print(f"xxx = {xxx}")

# xxx = len(xxx)
# print(f"xxx = {xxx}")

# fail = r"C:\vxvproj\tnnc-Excel\CorrectReportApp\CorrectReport\Подписи\Аминев.jpg"

# from PIL import Image

# img = Image.open(fail)
# img = img.convert("RGBA")

# pixdata = img.load()

# width, height = img.size
# for y in range(height):
#     for x in range(width):
#         if pixdata[x, y] == (255, 255, 255, 255):
#             pixdata[x, y] = (255, 255, 255, 0)

# img.save(r"C:\vxvproj\tnnc-Excel\CorrectReportApp\CorrectReport\"img3.png", "PNG")


# from PIL import Image

# img = Image.open(fail)
# img = img.convert("RGBA")
# datas = img.getdata()

# newData = []
# for item in datas:
#     if item[0] == 255 and item[1] == 255 and item[2] == 255:
#         newData.append((255, 255, 255, 0))
#     else:
#         newData.append(item)

# img.putdata(newData)
# img.save("img2.png", "PNG")


'''Изменение размера изображения'''

# from PIL import Image
# image = Image.open('pena.png')
# resized_image = image.resize((320, 320))
# resized_image.save('resized.png')





# from PIL import Image

# img = Image.open(fail)
# img = img.convert("RGBA")
# datas = img.getdata()

# xxx = 222
# uuu = 0
# newData = []
# for item in datas:
#     if item[0] > xxx and item[1] > xxx and item[2] > xxx:
#         newData.append((item[0], item[1], item[2], 0))
#     else:
#         # newData.append(item)
#         # newData.append((item[0] - uuu, item[1] - uuu, item[2], 255))
#         newData.append((item[0] - uuu if item[0] - uuu > 0 else 0, item[1] - uuu if item[1] - uuu > 0 else 0, item[2], 255))

# img.putdata(newData)
# img.save("img3.png", "PNG")


# from PIL import Image

# img = Image.open(fail)
# img = img.convert("RGBA")
# datas = img.getdata()

# xxx = 15
# uuu = 0
# newData = []
# for item in datas:
#     if item[2] > xxx:
#         newData.append((item[0], item[1], item[2]))
#     else:
#         # newData.append(item)
#         # newData.append((item[0] - uuu, item[1] - uuu, item[2], 255))
#         newData.append((item[0], item[1], item[2]))

# img.putdata(newData)
# img.save("img3.png", "PNG")


# from HSV.hsv import rgb_to_hsv, hsv_to_rgb

# if __name__ == '__main__':
#     ONE_255 = 1.0 / 255.0
#     r, g, b = 25, 60, 128
#     print("\nOriginal RGB values (R:%s, G:%s, B:%s)\n" % (r, g, b))
    
#     h, s, v = rgb_to_hsv(r * ONE_255, g * ONE_255, b * ONE_255)
    
#     print("HSV values (H:%s, S:%s, V:%s)" % (h * 360.0, s * 100.0, v * 100.0))
#     h, s, v = (h * 360.0, s * 100.0, v * 100.0)
#     print("HSV (H:%s, S:%s, V:%s)" % (h, s, v))
    
#     r, g, b = hsv_to_rgb(h / 360, s / 100, v / 100)
#     print("Retrieved RGB values (R:%s, G:%s, B:%s)\n" % (r * 255.0, g * 255.0, b * 255.0))
#     r, g, b = (r * 255.0, g * 255.0, b * 255.0)
#     print("Retrieved RGB(R:%s, G:%s, B:%s)\n" % (r, g, b))
    


'''Работа с пикселями подписи'''
# from HSV.hsv import rgb_to_hsv, hsv_to_rgb
# from PIL import Image

# fail = r"C:\vxvproj\tnnc-Excel\CorrectReportApp\CorrectReport\В.И. Федорчак.jpg"
# img = Image.open(fail)
# img = img.convert("RGBA")
# datas = img.getdata()
# ONE_255 = 1.0 / 255.0
# xxx = 222
# newData = []

# for item in datas:
#     r, g, b = (item[0], item[1], item[2])
#     h, s, v = rgb_to_hsv(r * ONE_255, g * ONE_255, b * ONE_255)
#     h, s, v = (h * 360.0, s * 100.0, v * 100.0)

#     if r > xxx and g > xxx and b > xxx:
#         newData.append((0, 0, 0, 0))
#     else:
#         s = s + 30 if s + 30 < 100 else s
#         if h < 200 or h > 250:
#             newData.append((0, 0, 0, 0))
#         else:
#             r, g, b = hsv_to_rgb(h / 360, s / 100, v / 100)
#             r, g, b = (r * 255.0, g * 255.0, b * 255.0)
#             newData.append((int(r), int(g), int(b), 255))

# img.putdata(newData)
# img.save("img3.png", "PNG")




# from time import sleep
# import win32com.client
# Excel = win32com.client.Dispatch("Excel.Application")
# wb = Excel.ActiveWorkbook
# sheet = wb.ActiveSheet
# # sheet.Shapes(1).Duplicate.IncrementLeft = 200
# sheet.Shapes(1).ShapeRange.IncrementTop = 200

# '''Autograph'''
# import imageZeroFon
# directory = r"C:\Users\vvkhomutskiy\Desktop\Подписи"
# direct = os.listdir(directory)

# for filename in direct:
#     print(filename)
#     fff = os.path.join(directory, filename)
#     if os.path.isfile(fff) and ".jpg" in filename:
#         imageZeroFon.GO(directory + "\\" + filename)


# def qqq(aaa="888", bbb:tuple=(5.5, 5):
#     print(aaa + "555")
#     # bbb = int(bbb)
#     print(bbb + 5)

# qqq("eeff", 7)



# directMod = "C:/vxvproj/vxv_moduls/"
# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0], directMod)))
# if cmd_subfolder not in sys.path:
#     sys.path.insert(0, cmd_subfolder)

# sys.path.append(directMod)
# sys.path.insert(1, directMod)


# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1, directMod)

# from directMod import VBAExcel
# directMod = "C:\\vxvproj\\vxv_moduls\\VBAExcel.py"
# from directMod import VBAExcel



# print(sys.path)
# sys.path.append(directMod)
# sys.path.insert(1, directMod)
# inspect(sys.path, all=True)

# import VBAExcel

# wb, sheet = VBAExcel.Book()
# print(wb.Name)


# from rich import print
# from rich import inspect
# import sys
# # import vxvPatch

# # sys.path.insert(1, "C:\\vxvproj\\vxv_moduls\\")
# import VBAExcel
# wb, sheet = VBAExcel.Book()
# print(sys.path)
# print(wb.Name)




import subprocess

# process = subprocess.Popen("notepad.exe")
# code = process.wait()
# fff = process.returncode
# print(fff)

# fff = subprocess.CompletedProcess(args='ls', returncode=222)
# print(fff)

# print(code)

# print(process.stdout)

# outs, errs = process.communicate('555', timeout=15)
# print(outs, errs)



# result = subprocess.run('notepad.exe')
# result.returncode=5
# print(result)
# print(result.returncode)

# process = subprocess.Popen("notepad.exe")
# print(process)
# code = process.wait()
# process.returncode=777
# print(code)
# print(process.returncode)




# result = subprocess.run('notepad.exe', stderr=subprocess.PIPE)
# result = subprocess.run( __name__)
# print(subprocess.PIPE)
# # result.returncode=5
# print(result)
# # print(result.returncode)
# print(result.stderr)
# print(subprocess.PIPE)



# import win32com.client

# def ExcelInstances():
#     '''Поиск всех процессов EXCEL.EXE'''
#     objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
#     objSWbemServices = objWMIService.ConnectServer(".", "root\cimv2")
#     colExcelInstances = objSWbemServices.ExecQuery(
#         f"SELECT * FROM Win32_Process WHERE Name = 'prostoTest.py'")
#     return colExcelInstances

# colExcelInstances = ExcelInstances()
# print(colExcelInstances)
# print(subprocess(colExcelInstances.returncode))

# result = subprocess.run('EXCEL.EXE')
# for objInstancei in colExcelInstances:
#     print(objInstancei.subprocess.returncode)




# if __name__ == "__main__":
#     # start()

#     sys.exit(app.exec_())

# fff = subprocess.getoutput('ls /bin/ls', encoding='utf-8')

# sts = os.system("mycmd" + " myarg")
# pipe = os.popen(cmd, 'w')


# import subprocess
 
# args = ["ping", "www.yahoo.com"]
# process = subprocess.Popen(args, stdout=subprocess.PIPE, encoding='utf-8')
# data = process.communicate()
# print(data)

# import multiprocessing
# data = multiprocessing.current_process()
# print(data)

# import subprocess

# result = subprocess.run(data)
# result.returncode




# result = subprocess.run('notepad.exe')
# result.returncode=5
# print(result)
# print(result.returncode)


# import subprocess

# def process_exists(process_name):
#     call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
#     # use buildin check_output right away
#     output = str(subprocess.check_output(call))
#     # check in last line for process name
#     last_line = output.strip().split('\r\n')[-1]
#     # because Fail message could be translated
#     return last_line.lower().startswith(process_name.lower())


# fff = process_exists('prostoTest.py')

# print(fff)

# input('Ждем... Enter')


# import sys
# # import exit_X
# # exit_X.GO()

# import subprocess

# '''Запускаем python - файл и получаем код возврата
# exit_X.py содержит sys.exit(2)'''
# code = subprocess.call(["python.exe", "exit_X.py"])
# code.returncode=5
# print(code)

# process = subprocess.Popen(["python.exe", "exit_X.py"])
# print(process)


# print(fff)

# sys.exit(print(exit.fff))

# if __name__ == '__main__':
#   sys.exit(1)


# result = subprocess.run('exit.py')
# # result = subprocess.run('notepad.exe')
# print(result)
# # result.returncode=5
# print(result.returncode)


# def openTypeMTR():
#     '''открытие файла как при двойном клике'''
#     os.startfile('python exit.py')


import sys
import subprocess

'''Запускаем python - файл и получаем код возврата
exit_X.py содержит sys.exit(2)'''
code = subprocess.call(["python.exe", "exit_X.py"])
print(code)

'''Отправляем команду в терминал и получаем код выхода'''
import os
command = r"python C:\Users\vvkhomutskiy\Documents\vxv\code\test\exit_X.py"
res = os.system(command)
print("Выполнено в PY: ", res)