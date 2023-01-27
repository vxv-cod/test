import sys
import os
import requests
from requests_ntlm import HttpNtlmAuth
print(sys.prefix) # '''Виртуалка инфо'''

from rich import print
import urllib.request

def namestr(obj):
    '''Имя переменной в строку'''
    name = [i for i in globals() if globals()[i] is obj][0]
    # print(f'"len({name})" = {len(obj)}')
    # print(f'"type({name})" = {type(obj)}')
    print(f'"{name}" = {type(obj)} len = {len(obj)}')

    
domain = 'rosneft'
user = os.getlogin()
password = 'Dkflbvbh444'

def resp(url):
    response = requests.get(url,auth=HttpNtlmAuth(f'{domain}\\{user}', password))
    if response.status_code == 404:
        print("'Страница не существует!'")
        return
    if response.status_code == 401:
        print("'Ошибка авторизации пользователя!'")
        return
    response = response.json()
    return response



'''Таблица 3 Идентификация зданий и сооружений площадочных и линейных объектов'''
Id = '2246'
response = resp(f"http://tnnc-pir-app/test-explication-ns-api/kits/kit-build-items/{Id}")
# url = f"http://tnnc-pir-app/test-explication-ns-api/dictionaries/dictionary-items/"




print(response)

print(sys.prefix) # '''Виртуалка инфо'''









# print(dir(globals()))


# print(listdict[0])
# print(listdict[0]['Customer'])

# print(listdict[0]['Project']['Description'])

# print(listdict)

# url = "http://tnnc-pir-app/test-explication-ns-api/kits/kit-build-items/2246"
# response = requests.get(url,auth=HttpNtlmAuth(f'{domain}\\{user}', password)).json()
# print(response)




# url = 'http://tnnc-pir-app/test-explication-ns-api/system/object-types'
# response = requests.get(url,auth=HttpNtlmAuth(f'{domain}\\{user}', password)).json()
# print(response)



# url = "http://tnnc-pir-app/test-explication-ns-api/kits/kit-build-item/2248"
# response = requests.get(url,auth=HttpNtlmAuth(f'{domain}\\{user}', password)).json()
# print(response)
