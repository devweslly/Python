soma_nota       = 0.0
contador_nota   = 0

for i in range(1, 4):
    nota            = float( input(f'informe a nota {i}: ') )
    soma_nota       = soma_nota + nota
    contador_nota   = contador_nota + 1

media = soma_nota/contador_nota

print(f'Média é: {media}')