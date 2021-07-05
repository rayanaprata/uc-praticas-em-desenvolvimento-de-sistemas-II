
# Example:

num1 = 10
num2 = 3
div = num1 / num2

print(f'printing without formatting: {div}')
print('printing using 2 float places using format function: {:.2f}'.format(div))
print(f'printing using 5 float places without using the format function: {div:.5f}')

name = "rayana prata neves"
print(f'{name:s}')

print('Upper: ' + name.upper())
print('Lower: ' + name.lower())
print('Title: ' + name.title())

print(f'{name:^20}')

print(name[1]) # a
print(name[3:6]) #ana
print(name[:6]) # rayana
print(name[7:]) # prata neves

print(name[:-1]) # rayana prata neve
print(name[:]) # rayana prata neves
