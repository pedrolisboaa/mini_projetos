from calculadora import soma

print(soma(10, 20))
print(soma(-10, 20))
print(soma(-10.5, 20))
print(soma(3.3, 4.8))
try:
    print(soma(1, 'p'))
except AssertionError as e:
    print(f'Conta invalida {e}')

