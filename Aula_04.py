Aula 4 ---
                           programa

print('Digite 3 numeros')

continua = 's'

while (continua == 's'):
    print('Digite o 1º numero')
    a = int(input())
    print('Digite o 2º numero')
    b = int(input())
    print('Digite o 3º numero')
    c = int(input())
    if a > b:
        if a > c:
            print( str(a) + ' é o maior número')
    elif b > c :
        print( str(b) + ' é o maior número')
    else:
        print( str(c) + ' é o maior número')
    print('Digite S para continuar ou N para sair')
    continua = input().lower()
    if (continua != 's'):
        if (continua != 'n'):
            print ('Eu disse pra digitar N!')
            print ('vou fechar só de raiva!')
print('Fim do programa !!!')

            resultado

Digite 3 numeros
Digite o 1º numero
5
Digite o 2º numero
6
Digite o 3º numero
8
8 é o maior número
Digite S para continuar ou N para sair
s
Digite o 1º numero
5
Digite o 2º numero
6
Digite o 3º numero
8
8 é o maior número
Digite S para continuar ou N para sair
h
Eu disse pra digitar N!
vou fechar só de raiva!
Fim do programa !!