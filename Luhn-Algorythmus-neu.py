

def verify_card_number():
        reversed_card_number = translated_cardnumber[::-1]
        print(f'Umgekehrte Nummer: {reversed_card_number}')
        even_digits = reversed_card_number[::2]
        even_digits_int = int(''.join(even_digits))
        print(f'Die unveränderten jede 2. Ziffern versetzt {even_digits_int}')
        doubled_numbers = [int(x)*2 for x in reversed_card_number[1::2]]
        print(f'Jede zweite Ziffer verdoppelt{doubled_numbers}')
       
        doubled_numbers_int = 0

        for number in doubled_numbers:
            doubled_numbers_int = doubled_numbers_int * 10 + number
        
        if doubled_numbers_int >= 10:
                doubled_numbers_int = (doubled_numbers_int // 10) + (doubled_numbers_int % 10)

        print(f'Die Ziffern der verdoppelten Nummern verrechnet {doubled_numbers_int}')


        sum_of_digits = (doubled_numbers_int + even_digits_int) 
        return sum_of_digits % 10 == 0
            



card_number = '4111-1111-4555-1141'

#coole Funktionen um Regeln eines Strings mithilfe des Dictionarys zu "übersetzen" also zu implementieren/ersetzen
translate_cardnumber = str.maketrans({' ': '', '-': ''}) 
translated_cardnumber = card_number.translate(translate_cardnumber)
print(translated_cardnumber)


is_valid = verify_card_number()
print(f'Die Kartennummer ist {"gültig" if is_valid else "ungültig"}.')