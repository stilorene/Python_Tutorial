absender = input ("Wer versendet den Brief?`" )


def generate_newsletter(absender):
    name = input ("Wer ist der Empfänger?`" )
    print(f"Hallo {name} hier kommt dein Wöchentlicher Newsletter")
    print("")
    print(f"Aktienkurse steigen")
    print("")
    print(f"Wohnungen werden Teurer")
    print(f"Grüße {absender}" )

    
for _ in range(3):
    generate_newsletter(absender)
