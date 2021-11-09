# Calculadora GBP com operações básicas

# Contador para definir um fim no processo
i = 0

# Ciclo para o funcionamento da calculadora
while i == 0:
    var1 = int(input(' '))
    operador = input(' ')
    var2 = int(input(' '))
    resultado = ''
    if operador == '+':
        resultado = var1 + var2
        print('Resultado = {}'.format(resultado))
    elif operador == '-':
        resultado = var1 - var2
        print('Resultado = {}'.format(resultado))
    elif operador == '/':
        resultado = var1/var2
        print('Resultado = {:.2}'.format(resultado))
    elif operador == 'x' or '*':
        resultado = var1 * var2
        print('Resultado = {}'.format(resultado))
    else:
        print('Digite um operador válido! (+, -, *, /)')
    decisao = input('Deseja fazer mais alguma operação? s/n ')
    if decisao == 's':
        continue
    else:
        i += 1
print('Obrigado por utilizar a calculadora GustavoBP!')


#end