'''
EXERCÍCIOS: ESTRUTURA DE DADOS
1. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
faça um programa que:
a) imprima o maior elemento
b) imprima o menor elemento
c) imprima os números pares
d) imprima o número de ocorrências do primeiro elemento da lista
e) imprima a média dos elementos
f) imprima a soma dos elementos de valor negativo
'''

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
maior = max(lista)
menor = min(lista)
pares = []
cont_primeiro = 0
total = 0
total_negativos = 0
for i in lista:
    if (i % 2 == 0):
        pares.append(i)
    if (i == lista[0]):
        cont_primeiro += 1
    total += i
    if (i < 0):
        total_negativos += i
media = total / len(lista)
print('Maior elemento: {}'.format(maior))
print('Menor elemento: {}'.format(menor))
print('Números pares: {}'.format(pares))
print('Ocorrências do primeiro: {}'.format(cont_primeiro))
print('Média dos elementos: {:.2f}'.format(media))
print('Soma dos valores negativos: {}'.format(total_negativos))

'''
2. Faça um programa que leia dados do usuário (nome, sobrenome, idade)
adicione em uma lista e
imprima seus elementos na tela.
'''

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
lista = [nome, sobrenome, idade]
for i in lista:
    print(i)

'''
3. Faça um programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = []
quantidade = 4
for x in range(quantidade):
    notas.append(int(input('Nota {}: '.format(x+1))))
media = sum(notas) / len(notas)
print('NOTAS:')
x = 1
while x <= quantidade:
    print('Nota {}: {}'.format(x, notas[x-1]))
    x += 1

'''
4. Faça um programa utilizando um dict que leia dados de entrada do usuário.
O usuário deve entrar
com os dados de uma pessoa como nome, idade e cidade onde mora (fique livre
para acrescentar
outros). Após isso, você deve imprimir os dados como o exemplo abaixo:
nome: João
idade: 20
cidade: São Paulo

5. (Opcional) Utilize o exercício anterior e adicione a pessoa em uma lista.
Pergunte ao usuário se ele
deseja adicionar uma nova pessoa. Após adicionar dados de algumas pessoas,
você deve imprimir
todos os dados de cada pessoa de forma organizada.
'''

pessoa = {'nome': '', 'idade': '', 'cidade': ''}
lista_pessoas = []
resposta = 's'
while resposta == 's':
    for i in pessoa:
        pessoa[i] = input('Qual {}: '.format(i))
    for j in pessoa:
        print('{}: {}'.format(i, pessoa[j]))
    lista_pessoas.append(pessoa)
    resposta = input('Deseja adicionar mais pessoas sim(s) ou não(n): ')
print('Pessoas:')
print('--------\n')
for x in lista_pessoas:
    for y in x:
        print('{}: {}'.format(y, x[y]))
    print('\n')
