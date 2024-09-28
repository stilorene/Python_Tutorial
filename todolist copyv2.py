todos = []
for _ in range(1000):
    print("Was wilst du tun")
    print("(1) Todos anzeigen")
    print("(2)  Todos hinzufügen")

    option = input("Bitte auswählen: ")

    if int(option) == 2:
        
        newitem = input("Welches Item brauchst du noch?")
        todos.append(newitem)
        print("Meine Einkaufsliste hat diese Zutaten: ")

    if int(option) == 1:
        for todo in todos:
            print(f"-  {todo}")

    print ("Programm Ende")