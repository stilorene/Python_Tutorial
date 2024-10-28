

def add_expense(expenses, amount, category):
    expenses.append({'expense': amount, 'category': category}) #hier ist das sogenannte Dictionary

def print_expenses(expenses): 
    for expense in expenses:   
        print(f'Amount: {expense['expense']}, Category: {expense['category']}')

def total_expense(expenses):
    return sum(map(lambda expense: expense['expense'], expenses))  

def filter_expense():
    pass

expenses = [] # Kurz erklärt: das ist die Leere Liste mit dem Dictionary die wir bei der Auswahl der Zahlen und 
                
            # und darauffolgenden Aufruf der Funktion immer wieder als Argument mitsenden. 
while True:
    print('\nExpense Tracker')
    print('1. Add an expense')
    print('2. List all expenses')
    print('3. Show total expenses')
    print('4. Filter expenses by category')
    print('5. Exit')


    choice = input('Enter your choice: ')

    if choice == '1':
        amount = float(input('What amount u spent: '))
        category = input('And in which category: ')
        add_expense(expenses, amount, category)

    elif choice == '2':
        print('This are all ur expenses: ')
        print_expenses(expenses)
        
    elif choice == '3':
        total_expense(expenses)
        print('Total Ausgabe Junge: ', total_expense(expenses))