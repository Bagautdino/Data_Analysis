import json

file = open("pokemon_full.json")
pokemon_str = file.read()
json_object = json.loads(pokemon_str)
print(f"1. Общая длина файла равна: {len(pokemon_str)}")

punctuations = '''‘’“”«»?‐…‒–—―⟨ ⟩''’!()-[]{};:'"\,<>./#$%^&*_~␠␢␣@©'''

str_without_punc = ""
for i in pokemon_str:
    if i not in punctuations:
        str_without_punc += i
new_string = str_without_punc.replace("\n", "")
print(f"2. Общая длина без пробелов и знаков препинания: {len(new_string)}")

max_desc = 0
max_amount = 0
poke_name = ""
res_ability = ""
for pokemon in json_object:
    desc = pokemon["description"]
    for ability_str in pokemon["abilities"]:
        if len(ability_str.split()) > max_amount:
            max_amount = len(ability_str.split())
            res_ability = ability_str
    if len(desc) > max_desc:
        max_desc = len(desc)
        poke_name = pokemon["name"]
print(f"3. Покемон {poke_name} с самым длинным описанием {max_desc} символов")
print(f"4. Самое большое количество слов: {res_ability}")
file.close()