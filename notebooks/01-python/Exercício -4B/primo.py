def primo(num):
    tentativa = False
    for c in range(2, num):
        if num%c == 0:
            print(f'O número {num} não é primo')
            tentativa = True
            break
    if tentativa == False:
        print(f'O numero {num} é primo') 
    


        