f = open(r"C:\Users\Админ\Desktop\Python\Словари и json\filenameforlesson.json")
from json import load
a = load(f)
print(a['games'])
for i in a ["games"]:
    if "first person" in i ["genre"]:
        print(i["name"])
