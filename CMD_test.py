import os, sys

'''Команды можно записывать разделяя из знаком "&"'''
# Перейти в текущую папку
com_1 = r'cd %CD%'
com_2 = r'call %CD%\venv\Scripts\activate.bat'
com_3 = 'pause'
com_4 = r'%CD%'
os.system(f'{com_1} & {com_2} & {com_3} & echo Адресс: {com_4} & echo {sys.prefix}')
os.system('pause')

'''Запускаем файл PY'''
command = r"python exit_X.py"
os.system(command)