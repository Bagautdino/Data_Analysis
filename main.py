import json
from json_file import json_str

#Загружаем json file
data = json.loads(json_str)

print("1. Общая длина файла равна: {",len(json_str),"}")

#Задаём знаки препинания которые хотим убрать
punctuations = '''‘’“”«»?‐…‒–—―⟨ ⟩''’!()-[]{};:'"\,<>./#$%^&*_~␠␢␣@©'''

#Будет формироваться новая строка
new_string = ''
for i in json_str:
    if i not in punctuations:
        new_string+=i
#Убираем переходы на новую строку
new_string= new_string.replace("\n","")
print("2. Общая длина без пробелов и знаков препинания {", len(new_string),"}")


#Находим покемона с самым длинным описанием
most_d = 0
pokemon = ''
for item in data:
    description = (item['description'])
    if len(description) > most_d:
        most_d = len(description)
        pokemon = item['name']
print(f"3. Покемон {pokemon} с самым длинным описанием {most_d} символов")

#Найдем самое длинное название умений
most_a = 0
most_ability = ''
for abilities in data:
    ability = (abilities['abilities'])
    if (len(str.split(''.join(ability)))) > most_a:
        most_a = len(str.split(''.join(ability)))
        most_ability = ''.join(ability)
print(f"4. Самое большое количество умений {most_a}: {most_ability}")
