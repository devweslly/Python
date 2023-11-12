# Função sem parâmetros

# Criando uma função
def saudacao():
    print('Olá, seja bem vinde =)')

# Chamando a função
saudacao()

nome = 'Weslly'
curso = 'Python'

# Criando função com parâmetro
def saudacao(nome, curso):
    print(f'Seja bem vinde, {nome}')
    print(f'Aproveite o curso de {curso}')

# Chamando a função com parâmetro
saudacao(nome, curso)

# Criando função com parâmetro default
def saudacao(nome = 'Juca', curso = 'C#'):
    print(f'Seja bem vinde, {nome}')
    print(f'Aproveite o curso de {curso}')

# Chamando a função com parâmetro default
saudacao()

# Funções com retorno
def Soma(num1, num2):
    return num1 + num2

resultado = Soma(3, 4)

print(f'A soma é: {resultado}')