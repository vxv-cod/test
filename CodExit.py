
import sys
import subprocess
import os

'''Запускаем python - файл и получаем код возврата
exit_X.py содержит sys.exit(2)'''
code = subprocess.call(["python.exe", "exit_X.py"])
print(code)

'''Отправляем команду в терминал и получаем код выхода как return от команды'''
command = r"python exit_X.py"
res = os.system(command)
print("Выполнено в PY: ", res)

