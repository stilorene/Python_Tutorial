animals = ["Affe", "Pferd", "Panda", 4, 8.8]

for werte in animals:
    if isinstance(werte, str):
        print(f"Auf meinem Bauernhof lebt ein {werte}")

for werte in animals:
    if isinstance(werte, int):
        print(werte)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet.find('z'))
