def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_a1 = int(input('Please enter the first number: '))
    number_b2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_a1, number_b2))
        print(number_a1 + number_b2)

    elif operation == '-':
        print('{} - {} = '.format(number_a1, number_b2))
        print(number_a1 - number_b2)

    elif operation == '*':
        print('{} * {} = '.format(number_a1, number_b2))
        print(number_a1 * number_b2)

    elif operation == '/':
        print('{} / {} = '.format(number_a1, number_b2))
        print(number_a1 / number_b2)

    else:
        print('You have not typed a valid operator, run the program again.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

calculate()
