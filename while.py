# Estrutura sem contador

numero_sorteado = 15

numero_escolhido = int( input('Escolha um número entre 1 e 20: ') )

while numero_escolhido != numero_sorteado:
    print('Errou! Tente novamente')
    numero_escolhido = int( input('Escolha um número entre 1 e 20: ') )

print('Você acertou!')

# Estrutura com contador

contador = 0

while contador < 5:
    print(contador)
    contador = contador + 1