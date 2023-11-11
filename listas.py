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