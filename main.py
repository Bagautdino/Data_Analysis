import json

file = open("pokemon_full.json")
pokemon_str = file.read()
json_object = json.loads(pokemon_str)
print(f"1. Общая длина файла равна: {len(pokemon_str)}")

punctuations = '''‘’“”«»?‐…‒–—―⟨ ⟩''’!()-[]{};:'"\,<>./#$%^&*_~␠␢␣@©'''

new_string = ''
for i in pokemon_str:
    if i not in punctuations:
        new_string += i
new_string = new_string.replace("\n", "")
print(f"2. Общая длина без пробелов и знаков препинания: {len(new_string)}")

max_desc = 0
max_amount = 0
poke_name = ""
res_ability = ""
for pokemon in json_object:
    desc = pokemon["description"]
    for ability_amount in pokemon["abilities"]:
        if len(ability_amount.split()) > max_amount:
            max_amount = len(ability_amount.split())
            res_ability = ability_amount
    if len(desc) > max_desc:
        max_desc = len(desc)
        poke_name = pokemon["name"]
print(f"3. Покемон {poke_name} с самым длинным описанием {max_desc} символов")
print(f"4. Самое большое количество умений: {res_ability}")
file.close()
