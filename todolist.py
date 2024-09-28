todos = ["Pferd", "Hase"]

for _ in range(1000):
    newitem = input("Welches Item brauchst du noch?")
    todos.append(newitem)
    print("Meine Einkaufsliste hat diese Zutaten: ")

    for todo in todos:
        print(f"-  {todo}")

print ("Programm Ende")