x = float(input('Digite um valor: '))
y = float(input('Digite outro valor: '))
option = ' '
print('-=' * 15)

while True:
    print('~~' * 15)
    option = int(input('''Qual operação deseja realizar?
    [1] SOMA
    [2] PRODUTO
    [3] DIFERENÇA
    [4] DIVISÃO
    [5] POTENCIAÇÃO
    [6] RADICIAÇÃO DOS DOIS VALORES
    [7] ESCOLHA NOVOS VALORES                  
    [0] SAIR DA CALCULADORA\n'''))
    print('~~' * 15)

    if option == 0:
        break

    elif option == 1:
        soma = x + y
        print(f'O resultado da soma entre {x} e {y} é {soma}.')
    
    elif option == 2:
        prod = x * y
        print(f'O produto entre {x} e {y} é {prod}.')
    
    elif option == 3:
        sub = x - y
        print(f'A diferença entre os valores é {sub}.')

    elif option == 4:
        try:
            div = x / y
            print(f'A divisão entre {x} e {y} é {div:.2f}.')
        except ZeroDivisionError:
            print('É impossível dividir por Zero.')

    elif option == 5:
        pot = x ** y
        print(f'{x} elevado a {y} é {pot}.')

    elif option == 6:
        if x >= 0 and y >= 0:
            r1 = x ** 0.5
            r2 = y ** 0.5
            print(f'A raiz quadrada de {x} é {r1:.2f}.')
            print(f'A raiz quadrada de {y} é {r2:.2f}.')
        else: 
            print('Não existe raiz quadrada negativa no conjunto dos números Reais.')

    elif option == 7:
        x = float(input('Digite um novo valor: '))
        y = float(input('Digite o outro novo valor: '))
    
    else:
        print('Opção Inválida... ')

print('Obrigado por utilizar nossa calculadora.')