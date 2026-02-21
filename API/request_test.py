# Импорт библиотеки requests
import requests
# Запрос GET (Отправка только URL без параметров)
response = requests.get("http://api.open-notify.org/astros.json")
# Вывод кода
print(response.status_code)
# Вывод ответа, полученного от сервера API
print(response.json())


# Импорт библиотеки json
import json
def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
# Запрос GET (Отправка только URL без параметров)
response = requests.get("http://api.open-notify.org/astros.json")
# Вывод ответа, через пользовательскую функцию jprint
jprint(response.json())



# Запрос GET (Отправка только URL без параметров)
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# Вывод ответа, через пользовательскую функцию jprint
print("response:\n{}\n\n".format(response))
print("response.url:\n{}\n\n".format(response.url))                 #Посмотреть формат URL (с параметрами)
print("response.headers:\n{}\n\n".format(response.headers))         #Header of the request
print("response.status_code:\n{}\n\n".format(response.status_code)) #Получить код ответа
print("response.text:\n{}\n\n".format(response.text))               #Text Output
print("response.encoding:\n{}\n\n".format(response.encoding))       #Узнать, какую кодировку использует Requests
print("response.content:\n{}\n\n".format(response.content))         #В бинарном виде
# print("response.json():\n{}\n\n".format(response.json()))           #JSON Output

import pandas as pd

page_number = 0
search_str = "qlik"
area_str = "1"
# Адрес api метода для запроса get
url = 'https://api.hh.ru/vacancies'
param = {
    "text": search_str,
    "area": area_str,
    "page": page_number
}
# Отправляем get request (запрос GET)
response = requests.get(url, param)
data = response.json()
# Создаем пустой dict (словать данных)
dict_data = {}
dict_number = 0
# Количество страниц
for i in range(0, data['pages']):
    param_cycle = {
        "text": search_str,
        "area": area_str,
        "page": i
    }
    response_cycle = requests.get(url, param_cycle)
    print("ЗАПРОС №" + str(i))
    result = dict(response_cycle.json())
    result = result['items']
    # Парсим исходный list формата Json в dictionary (словарь данных)
    for y in range(0, len(result) - 1):
        dict_data[dict_number] = {
            'id': result[y]['id'],
            'premium': result[y]['premium'],
            'name': result[y]['name'],
            'department': result[y]['department'],
            'has_test': result[y]['has_test'],
            'area_name': result[y]['area']['name'],
            'salary': result[y]['salary'],
            'type_name': result[y]['type']['name'],
            'snippet_requirement': result[y]['snippet']['requirement']
        }
        dict_number = dict_number + 1

    print("==================================")
print(dict_data[0])

import xml.etree.ElementTree as et

v_date = '16.04.2020'
# Адрес api метода для запроса get
url = 'https://www.cbr.ru/scripts/XML_daily.asp'
params = {
    'date_req': v_date
}
# Отправляем get request (запрос GET)
response = requests.get(url, params)
tree = et.ElementTree(et.fromstring(response.text))
root = tree.getroot()
df_cols = ["date", "numcode", "charcode", "nominal", "name", "value"]
rows = []
for node in root:
    s_numcode = node.find("NumCode").text if node is not None else None
    s_charcode = node.find("CharCode").text if node is not None else None
    s_nominal = node.find("Nominal").text if node is not None else None
    s_name = node.find("Name").text if node is not None else None
    s_value = node.find("Value").text if node is not None else None

    rows.append({"date": v_date, "numcode": s_numcode,
                 "charcode": s_charcode, "nominal": s_nominal,
                 "name": s_name, "value": s_value})
df = pd.DataFrame(rows, columns=df_cols)
print(df.head())

