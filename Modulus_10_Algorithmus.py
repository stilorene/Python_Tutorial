# genannt auch den dINGS Luhn-Algorythmus zur Validierung von Kreditkarten
def main():
    creditcard_number = '4111-1111-4555-1141'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_creditcard_number = creditcard_number.translate(card_translation)
    
    
    if  verify_card_number(translated_creditcard_number):
        print('VALID!')
    else:
        print('INVALID!')

    
   
   
#Funktion geht mit step = 2 durch die Ziffern durch (odd-ziffern), nimmt nochmal versetzt den gleichen Ansatz (even-Ziffern)
def verify_card_number(creditcard_number):
    sum_of_odd_digits = 0   
    creditcard_number_reversed = creditcard_number[::-1]
    odd_digits = creditcard_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit) # Summe der ungeraden Ziffern
    print(f'Summe der Odd Digits {sum_of_odd_digits}')    

    sum_of_even_digits = 0
    even_digits = creditcard_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number # Das dann die Zahl der ungeraden Ziffern
    total = sum_of_odd_digits + sum_of_even_digits
    

    print(f'Summer der even Digits: {sum_of_even_digits}')
    print(total)
    return total % 10 == 0

main()



