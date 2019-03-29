'''
Strings

Saber métodos:
dir('string')

Saber o que método faz:
help('string'.método)

Aspas:
Simples
Duplas
Triplas - multilinha (ex. html)

Fatiamento:
x = '0123456789'
x[0:2] // 01
Primeiro índice ínicio e segundo até onde

-1 último
-2 penúltimo

x[:2] // 01
x[4:] // 456789
x[4:-1] // 45678
x[-4:-1] // 678
x[:] // 0123456789

texto = 'batatinha quando nasce'
texto[::2] // bttnaqad ac
Inteiro de dois em dois

texto[::-1]
Invertida


Novas Strings
texto = 'Alo mundo'
texto = '@' + texto[1:] // @lo mundo

Verificação parcial de strings
arquivo = 'prog.py'
arquivo.startswith('p') // True
arquivo.endswith('py') // True

resposta = "Sim"
resposta.lower() // sim
respota.upper() // SIM

resposta.lower() in 'sim não yes no' // True

x.find('palavra') // procura a primeira
x.find('palavra', 4) // procura depois do índice

x.replace('palavra', 'palavranova') // uma cópia com palavras trocadas (precisa refenciar à uma varável pois os valores originais permanecem)

x.split() // separa
x.split('/') // separa nas barras

'/'.join(x) // juntar


FOR

for i in range(5):
  print (i)

 
for letra in 'aeiou':
  print (letra)

for x in ['string', 10, 2.4]
  print(x)


Funções

def épar(x):
  return x%2 == 0


Random

import random

random.randint(1, 100) aleatório
random.choice([array]) aleatório
random.shuffle([array]) mistura

LIST
list('string') // transforma em lista/array


SORT
array.sort() // Coloca em ordem

CONJUNTOS
frutas = {'laranja', 'banana', 'abacaxi'}

a = set('abacate')
b = set('abacaxi')
a - b Diferença
a | b União
a & b Interseção
a ^ b Diferença simétrica

DICIONÁRIOS

pessoa.keys() - retorna as chaves
pessoa.values() - retorna os valores

Somente tipos de dados imutáveis podem ser usados como chaves, ou seja, nenhuma lista ou dicionário
pode ser usado.

Tuplas são permitidas então:
dic = {(1, 2, 3): 'valor'}

função dict:
a = dict(um=1, dois=2, três=3)
{'três': 3, 'dois': 2, 'um': 1}




'''