# import os
# import sys
# import urllib3
# import requests
# from urllib.parse import urlparse
# from rich import print

# from rich import inspect
# inspect(color, all=True)

# import urllib.request
# import requests


print('--------------------------------')
# url = 'file:///' +  r"C:\Users\vvkhomutskiy\Desktop\TEST\333\27_111.html"
# url = 'http://tnnc-pir-app/test-api/view-projects'

# proxies = {
#     “http”: “https://пользователь:пароль@адрес_прокси:порт”,
#     “https”: “https://пользователь:пароль@адрес_прокси:порт”,
# }

# link = urllib.request.urlopen(url)


# print(url)
# lines = []
# for line in link.readlines():
#     # if line.find(b'<nobr>') != -1 or (line.find(b'<td colspan="6">') != -1 and b'<td colspan="6"><b></b></td>' not in line):
#     # if line.find(b'<nobr>') != -1 or line.find(b'rosneft.ru') != -1:
#     # if b'<nobr>' in line or b'rosneft.ru' in line:            
#         # lines.append(line)
#     lines.append(line)
#     # print(line)
# link.close()
# print(lines)


# '''Переводим bytes в str'''
# for i in range(len(lines)):
#     lines[i] = lines[i].decode('utf-8')

# print(lines)


# http = urllib3.PoolManager()
# url = 'https://haieronline.ru/?ysclid=l9gjlgte4z595040643.html'
# # url = r'"C:\Users\vvkhomutskiy\Desktop\TEST\444\last\last\27 PC MEMORY _ Отчет _ TNNC-WORKSTATION-MONITORING.html"'
# resp = http.request('GET', url)
# resp.data
# print(resp.status)
# resp.close()

'''http://tnnc-pir-app/test-api/view-projects'''

# 
# vvkhomutskiy@tnnc.rosneft.ru
# import requests

# url = 'http://tnnc-pir-app/test-api/view-projects'
# username = "rosneft\vvkhomutskiy"
# username = "rosneft\vvkhomutskiy"
# password = "Dkflbvbh444"
# response = requests.get(url, auth=(username, password))
# print(response.status_code)
# # print(response.json())

# print(response.headers['content-type'])

# import win32security
# username = "vvkhomutskiy"
# domain = "rosneft"
# password = "Dkflbvbh444"

# token = win32security.LogonUser(
#     username,
#     domain,
#     password,
#     win32security.LOGON32_LOGON_NETWORK,
#     win32security.LOGON32_PROVIDER_DEFAULT)
# authenticated = bool(token)


# print(authenticated)
# # print(token)

# url = 'http://tnnc-pir-app/test-api/view-projects'

# session = requests.Session()
# # domain = "rosneft"
# domain = "@tnnc.rosneft.ru"
# # user = "rosneft\\vvkhomutskiy"
# user = "@tnnc.rosneft.ru\\vvkhomutskiy"
# password = "Dkflbvbh444"
# session.auth = (user, password)

# from requests.auth import HTTPDigestAuth
# response = requests.get(url, auth=HTTPDigestAuth('user', 'password'))

# # # auth = session.post(url)
# # header = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
# # response = requests.get(url, headers=header)
# # # response = session.get('http://tnnc-pir-app/test-api/view-projects')


# # print(auth)
# print(token)
# print(response.status_code)



# user = "vvkhomutskiy"
# password = "Dkflbvbh444"
# # user = r"ROSNEFT\\" + os.getlogin()
# # user = os.getlogin() + '@tnnc.rosneft.ru'

# import requests
# from requests.auth import HTTPBasicAuth

# response = requests.get(url)

# if response.status_code == 401:    
#     response = requests.get(url, auth=HTTPBasicAuth(user, password).__call__)
#     s_auth = response.headers.get("www-authenticate", "")

# # if response.status_code != 200:
# #     # Definitely something's wrong

# print(user)
# print(response.status_code)
# print(response.headers)



# url = 'http://tnnc-pir-app/test-api/view-projects'

# import requests
# from requests_kerberos import HTTPKerberosAuth, REQUIRED
# kerberos_auth = HTTPKerberosAuth(mutual_authentication=REQUIRED, sanitize_mutual_error_response=False)
# r = requests.get(url, auth=kerberos_auth)



# from requests.auth import HTTPBasicAuth
# user = "rosneft/vvkhomutskiy"
# user = "vvkhomutskiy (10.28.177.117)"
# user = "vvkhomutskiy"
# password = "Dkflbvbh444"
# basic = HTTPBasicAuth(user, password)
# r = requests.get(url, auth=basic)

# # print(r.status_code)

# # r = requests.get(url, auth=(user, password))
# # print(r.status_code)

# from requests.auth import HTTPDigestAuth
# url = 'http://tnnc-pir-app/test-api/view-projects'
# r = requests.get(url, auth=HTTPDigestAuth(user, password))
# # r = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
# # print(r.status_code)

# user = __import__("os").getenv('username')
# print(user)
# user = os.getlogin()
# print(user)


# print(password)
# db_connect(server, user, password)

# r = requests.get(url)
# r = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
# print(r.status_code)
# print(r.text)
# from getpass import getpass
# print(getpass())
# r = requests.get(url, auth=(user, getpass()))
# print(r.status_code)

# session = requests.Session()
# session.auth = (user, password)
# auth = session.post('http://tnnc-pir-app')
# r = session.get('http://tnnc-pir-app/test-api/view-projects')
# print(r.status_code)


# import requests
# from requests_oauthlib import OAuth1

# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

# r = requests.get(url, auth=auth)
# print(auth)
# print(r.status_code)


# from requests_oauthlib import OAuth2
# import requests_oauthlib
# scope = [url]

# oauth = requests_oauthlib.OAuth2Session(user, redirect_uri=url,
#                           scope=scope)
# # print(oauth)

# import requests
# from requests_oauthlib import OAuth1

# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

# r = requests.get(url, auth=auth)
# print(r.status_code)


# import requests
# from requests_ntlm import HttpNtlmAuth

# session = requests.Session()
# # rosneft/vvkhomutskiy
# session.auth = HttpNtlmAuth('rosneft\\vvkhomutskiy', password)
# session.get(url)




# # r = requests.get(url, auth=('rosneft/vvkhomutskiy', 'Dkflbvbh444'))
# r = requests.get(url, auth=('rosneft/vvkhomutskiy', 'Dkflbvbh444'))

# fff = r.status_code
# print(fff)
# r.headers['content-type'] = 'application/json; charset=utf8'
# # print(r.headers['content-type'])
# # 'application/json; charset=utf8'

# r.encoding = 'utf-8'
# # print(r.encoding)
# print(r.text)

# import requests as req
# resp = req.get(url)
# print(resp.text)

# o = urlparse("http://tnnc-pir-app/test-api/view-projects"
#             "highlight=params#url-parsing")
# print(o)
# print(o.scheme)


# link = urllib.request.urlopen(url, 'vvkhomutskiy', 'Dkflbvbh444')

# o = urllib.request.AbstractBasicAuthHandler(password_mgr=None)
# print(o)

# url = 'https://haieronline.ru/?ysclid=l9i00pil7u574802265'


# url = 'https://haieronline.ru/personal/favorites/ovens/'

# # url = 'https://translate.yandex.ru/'
# url = url.replace('https', 'http')
# r = requests.get(url, auth=('vvkhomutskiy', 'Dkflbvbh444'))
# # headers = {'vvkhomutskiy': 'Dkflbvbh444'}
# # r = requests.get(url, headers=headers)
# # r.json()
# # r.raise_for_status()
# print(r.status_code)
# print('========== r.text ===========')
# r.encoding = 'utf-8'
# print(r.encoding)
# print(r.text)
# # print('========== r.content ===========')
# # print(r.content)

# # lines = r.content
# '''Переводим bytes в str'''
# for i in range(len(lines)):
#     lines[i] = lines[i].decode('utf-8')

# print(lines)








# r.close()



# import urllib
# print(urllib.__file__)




# import socket

# from ntlm_auth.ntlm import NtlmContext

username = 'User'
password = 'Password'
domain = 'Domain' # Can be blank if you are not in a domain
# workstation = socket.gethostname().upper()




# import requests
# from requests_ntlm import HttpNtlmAuth

# session = requests.Session()
# session.auth = HttpNtlmAuth(user,password)
# session.get(url)


# import requests
# from requests_ntlm import HttpNtlmAuth

# r = requests.get(url, auth=('vvkhomutskiy', 'Dkflbvbh444'))

# response = requests.get("http://tnnc-pir-app/test-api/view-projects",auth=HttpNtlmAuth('rosneft\\vvkhomutskiy','Dkflbvbh444'))
# response = requests.get("http://tnnc-pir-app/test-explication-ns-api/dictionaries/projects",auth=HttpNtlmAuth('rosneft\\vvkhomutskiy','Dkflbvbh444'))
# response = requests.get("http://tnnc-pir-app/test-explication-ns-api/system/users",auth=HttpNtlmAuth('rosneft\\vvkhomutskiy','Dkflbvbh444'))
# response = requests.get("http://tnnc-pir-app/test-explication-ns-api/system/users",auth=HttpNtlmAuth('rosneft\\vvkhomutskiy','Dkflbvbh444'))




import sys
import os
import requests
from requests_ntlm import HttpNtlmAuth
print(sys.prefix) # '''Виртуалка инфо'''
import venv



url = "http://tnnc-pir-app/test-api/view-projects"
# url = "http://tnnc-sapsan-app:5050"
# url = "http://tnnc-sapsan-app:5050/api/document/get"
domain = 'rosneft'
user = os.getlogin()
password = 'Dkflbvbh444'
response = requests.get(url,auth=HttpNtlmAuth(f'{domain}\\{user}', password))
print(response.status_code)
listdict = response.json()
print(len(listdict))

print(listdict)
# for key in listdict:
#     print(key)


# print(listdict['Total'])
# print(listdict['Data'])
# fff = listdict['Data']
# fff = len(fff)
# print(fff)

# print(f"type(listdict['Data'] = {type(listdict['Data'])}")
# print(f"len(listdict['Data'] = {len(listdict['Data'])}")
# print(f"listdict['Data'][0] = {listdict['Data'][0]}")

# print(listdict['Data'][100])
# print(listdict[1]['OiItem']['Title'])


# for i in listdict['Data']:
#     # print(i)
#     for r in i:
#         print(r)
#         if 'Обустройство' in  r:
#             # print(i)
#             i['Shifr']

#         # print(f"{i['Shifr']}")



# listdict = response.text
# print(listdict)
# print(listdict['Shifr'][1])




# for i in listdict:
#     # print(f"{i['Shifr']} - {i['Title']}")
#     print(listdict['Shifr'])


# print(listdict[0])
# print(len(listdict))
# print(response.status_code)


# \venv\Scripts\activate.bat"

print(venv.main) 

input()
print('=================================')