#Exercício 2-B
import random
num = random.randint(1,100)
escolha = int(input('Escolha o número: '))
while escolha != num:
    if num > escolha:
        print('O número escolhido é menor do que o número secreto!')
    else:
        print('O número escolhido é maior do que o número secreto!')
    escolha = int(input('Escolha o número: '))
print(f'Você acertou!! O número secreto é {num}')