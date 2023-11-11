# Listas (aceita diferente tipo de dados)
notas   = [7.9 , 9.7 , 8.2]
pessoa  = ['Weslly' , 32 , True]

# Criando lista vazia
lista = []
lista = list()

# Criando lista de listas
lista_de_Listas = [notas , pessoa , lista , [1 , 2 , 3]]

# Indexação (acessando elemento da lista)
tamanho_lista = len(notas)

for indice in range(tamanho_lista):
    print(notas[indice])

print('-----------------------')

# (indices negativos)
print(notas[-1]) # acessa o último elemento 
print(notas[-2]) # acessa o antepenúltimo elemento

print('-----------------------')

lista = [10 , 12 , 23 , 42 , 53 , 67 , 77 , 85 , 99 , 140]

for elemento in lista:
    print(elemento)

print('-----------------------')

# Slices (fatiamento de uma lista)
print(lista[0:3]) # obtendo os elementos do intervalo de indices 0 até 2
print(lista[3:7])
print(lista[3:])
print(lista[0:10:2])

# adicionando um elemento no final da lista
lista.append(160)

# escolhendo a posição onde o elemento inserido (e empurra todos os elementos para frente)
lista.insert(3 , 200)

# juntando duas listas (colocando os elementos da segunda lista no final da primeira)
lista.extend(notas)

# removendo elemento (caso não especificar a posição é removido o último elemento)
lista.pop() # remove ultimo elemento
lista.pop(0) # remove elemento do indice especificado

# o remove você informa qual valor remover
lista.remove(200)

# Contando a quantidade de vezes que um valor aparece na lista
print('Quantidade de 2 na lista: ', lista.count(2))

# Informando o indice de um valor
print('Indice do valor 77: ', lista.index(77))

print('Lista depois da alterações: ', lista)

# Ordenando a lista
lista.sort()
print(lista)

# Somando os valores da lista
print(sum(lista))

# O valor max e min
print('Maior valor da lista', max(lista))
print('Menor valor da lista', min(lista))