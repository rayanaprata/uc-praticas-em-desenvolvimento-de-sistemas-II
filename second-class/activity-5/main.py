# Implementar uma calculadora simples utilizando todos os conceitos estudados.

# – Menu se deseja sair ou continuar
# – Operador informado pelo usuário
# – Verificação de valor numérico e se está vazio
# – Formatação de saídas

def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    num1 = int(input('Please enter the first number: '))
    num2 = int(input('Please enter the second number: '))

    if operation == '+':
        res = num1 + num2
        print(f'{num1} + {num2} = {res}')

    elif operation == '-':
        res = num1 - num2
        print(f'{num1} - {num2} = {res}')

    elif operation == '*':
        res = num1 * num2
        print(f'{num1} * {num2} = {res}')

    elif operation == '/':
        print('{} / {} = '.format(num1, num2))
        print(num1 / num2)

    else:
        print('You have not typed a valid operator, please run the program again.')

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