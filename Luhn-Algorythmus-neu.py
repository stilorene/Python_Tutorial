def cardinfo():
    card_number = '4111-1111-4555-1141'

    #coole Funktionen um Regeln eines Strings mithilfe des Dictionarys zu "übersetzen" also zu implementieren/ersetzen
    translate_cardnumber = str.maketrans({' ': '', '-': ''}) 
    translated_cardnumber = card_number.translate(translate_cardnumber)
    print(translated_cardnumber)

cardinfo()