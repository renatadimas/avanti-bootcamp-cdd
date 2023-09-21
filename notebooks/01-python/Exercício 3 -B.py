#Exercício 3-B
animais = ('cavalo', 'macaco', 'cachorro', 'gato', 'tigre', 'urso')
escolha = str(input('Digite o nome de um animal: ')).lower()
acertou = False
for n in animais:
    if n == escolha:
        print(f'O animal {escolha} está presente na tupla')
        acertou = True
if acertou == False:
    print(f'O animal {escolha} não está presente na tupla')
