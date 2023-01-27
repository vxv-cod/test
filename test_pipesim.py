    
import threading
import win32com.client
from time import sleep
from rich import print
from rich import inspect

# '''
# regsvr32.exe "C:\Program Files (x86)\Schlumberger\PIPESIM\Programs\Net32COM.dll"
# '''

# from pythoncom import VT_ARRAY, VT_R8, VT_DISPATCH
# from pythoncom import CoInitializeEx as pythoncomCoInitializeEx

# pythoncomCoInitializeEx(0)
# acad = win32com.client.Dispatch.__annotations__
# print(acad)
# print(dir(acad))
# print(acad)
# inspect(acad, all=True)


# pythoncomCoInitializeEx(0)
# acad = win32com.client.CLSIDToClass
# print(dir(acad))
# inspect(acad, all=True)


# from win32com.client import combrowse

# def thread(my_func):
#     def wrapper():
#         threading.Thread(target=my_func, daemon=True).start()
#     return wrapper

# # @thread
# def FunctionName():
#     combrowse.main()
#     sleep(10)


# FunctionName()

# fff = win32com.client.constants
# acad = win32com.client.Dispatch("PipeSim files.Application")
# inspect(acad, all=True)

# fff = dir(win32com.client.Dispatch)

# from win32com.client import combrowse
# combrowse.main()
# input('ffffff',)


# fff = win32com.client.Dispatch("_BJADB")
# fff = win32com.client.Dispatch.GetTypeInfoCount()
# print(fff)
# fff = dir(win32com.client.Dispatch.__class__)
# print(fff)

# import pkg_resources.py31compat



# from sixgill.pipesim import model

# import clr
# import os

# print(dir(clr))
# # OpenLink()

# def SendText():
#     '''Поместим библиотеку “TNNC_SQL_transferer.dll” и "tnnc_oapr_stat.ini" в папку с проектом:'''
#     '''Укажем путь до нашего .dll файла:'''
#     pathDLL = r"C:\Users\vvkhomutskiy\Documents\vxv\code\test\Net32COM.dll"

#     '''Чтобы подгрузить нужную нам библиотеку необходимо прописать следующий код:'''
#     clr.AddReference(pathDLL)

#     '''После чего можно импортировать модуль и всё, что в нем содержится.'''

    # import Net32COM

#     # try:
#     #     '''Отправляем тескт названия программы'''
#     #     TNNC_SQL_transferer.TNNC_SQL().SendStatMessage(text)
#     #     print(f'Оправка записи на SQL: "{text}"')
#     # except:
#     #     print('Ошибка оправки записи на SQL')

#     # NetBranchObj = dir(Net32COM)
#     # print(NetBranchObj)


# SendText()    

# import win32com
# fff = win32com.client.Dispatch("NET32COM.INetModel")

# KompasAPI5 = win32com.client.gencache.EnsureModule('{835242AB-BF43-4674-8D57-B9540D0EFB82}', 0, 1, 0)
# import clr
# pathDLL = os.getcwd() + "\\TNNC_SQL_transferer.DLL"
# clr.AddReference(pathDLL)


# import pyfas
# inspect(pyfas, all=True)

# import pyfas as fa

# tpl = fa.Tpl(r"C:\Users\vvkhomutskiy\Desktop\PIPSIM\Net32COM.dll")

# from win32com.client import Dispatch
# o = Dispatch("NET32COM.INetModel")



# # from __future__ import with_statement
# import pythoncom
# import pywintypes
# import win32com
# import win32com.client
# import win32api
# import re
 
# # fso = win32com.client.Dispatch("Scripting.FileSystemObject")
# # Net32COMLib = win32com.client.gencache.EnsureModule('{835242AB-BF43-4674-8D57-B9540D0EFB82}', 0, 1, 0)
# model = win32com.client.Dispatch("Net32COM.INetModel")
# # model.OpenModel(fso.GetAbsolutePathName("..\\PIP\\E300_flash_BIPs\\GTN.bpn"))




 
#!/bin/python
# -*- coding: utf-8 -*-
 
# from __future__ import with_statement
import pythoncom
import pywintypes
import win32com
import win32com.client
import win32api
import re
 
# fso = win32com.client.Dispatch("Scripting.FileSystemObject")
# Net32COMLib = win32com.client.gencache.EnsureModule('{095B5403-3172-11D4-A949-0080C802A6A1}', 0, 1, 0)
# model = win32com.client.Dispatch("Net32COM.INetModel")
# model.OpenModel(fso.GetAbsolutePathName("..\\PIP\\E300_flash_BIPs\\GTN.bpn"))
 
# (arr, num) = model.GetNameList(7)
# well = model.GetSingleBranchModel(arr[0])
# profile = well.ObjectProperties("NKT")
# unknown = profile._oleobj_.QueryInterface(pythoncom.IID_IUnknown)
# unknown = win32com.client.CastTo('disp', "Net32COM.TubingObj")
# tubing = win32com.client.CastTo(well.ObjectProperties("NKT")._oleobj_.QueryInterface(pythoncom.IID_IDispatch), "Net32COM.Tubing")

import os
# PATCHx = r"C:\Program Files\Schlumberger\PIPESIM2013.1.1\Programs\Net32COM.dll"
# PATCHx = r"C:\Program Files (x86)\Schlumberger\PIPESIM\Programs\Net32COM.dll"
# os.system(f'regsvr32.exe "{PATCHx}"')
# regsvr32 "C:\Program Files (x86)\Schlumberger\PIPESIM\Programs\Net32COM.dll"


import win32com

# inspect(win32com.client, all=True)
pipsim = win32com.client.Dispatch("Net32COM.INetModel")
pipsim.OpenModel(r"5555555555555.bpn")
# fff = dir(pipsim)
# fff = pipsim.GetCountObjectsInProfile(0)
# print(fff)
# fff = pipsim.GetNameList(0)[0]

# fff = pipsim.GetNameList(2)[0]
# fff = pipsim.GetNameList(6)

# pipsim.SetBoundaryFluidrate('Flowline_19', 1, "88888888888888", 'STB/d')
# fff = pipsim.SetBoundaryFluidrate(9, 1, 1, "sm3/d")
# print(fff)


# pipsim.SaveModel('5555555555555.bpn')
# pipsim = win32com.client.Dispatch("Net32COM.INetModel")
# pipsim.OpenModel(r"5555555555555.bpn")
# fff = pipsim
# # count_source

# # fff = pipsim.SetBoundaryFluidrate
# # print(dir(pipsim))

# from rich import print
# from rich import inspect

# # print(fff)
# # inspect(fff, all=True)


# objname_source, count_source = pipsim.GetNameList(2)
# objname_sink, count_sink = pipsim.GetNameList(3)

# # print(fff)
# print(objname_source, count_source)
# print(objname_sink, count_sink)

# Units = win32com.client.Dispatch("UnitsCOM.IUnitSystem")
# Units.ConvertAny("PRESSURE", 1, Units, "sm3/d")
# # Units = pipsim.IUnitSystem
# print(Units)

# for i in range(1, 1000):
#     try:
#         # fff = pipsim.GetNameList(i)[0]
#         fff = pipsim.GetNameList(i)
#         if fff[0] != None:
#             print(f"----- {i} -----")
#             print(fff)
#     except:
#         pass

# pipsim.SaveModel

# win32com.client.Dispatch("PNSREADER.PNSCom")
# win32com.client.Dispatch("NET32COM.ISingleBranchModel")








