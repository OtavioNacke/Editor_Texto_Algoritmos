texto = input()

cursor = 0
while True:
    comando = input().split() #divide o input no comando e no argumento

    if comando[0] == 'F': #quebra tudo
        break
    
    if comando[0] == 'E':
        n = int(comando[1]) #pega apenas o argumento, o número e converte pra int
        cursor -= n         #move o cursor para a esquerda a partir da posição atual do cursor
        if cursor < 0:      #se o cursor for menor que 0, ele vai pro início
            cursor = 0
        
    elif comando[0] == 'D':
        n = int(comando[1]) 
        cursor += n         
        if cursor > len(texto): #se o cursor for maior que o comprimento do texto, ele vai pro final
            cursor = len(texto)
    
    elif comando[0] == 'i':
        char = comando[1]       #pega o argumento, que é o caractere
        texto = texto[:cursor] + char + texto[cursor:]   #aq ele pega o texto antes do cursor [:cursor], coloca o char e depois pega o texto depois do cursor [cursor:]

        cursor += 1             #pra ele andar um pra direita depois de colocar o char

    elif comando[0] == 'I':
        palavra = comando[1] #pega a palavra
        if cursor != 0:
            texto = texto[:cursor] + ' ' + palavra + texto[cursor:]  #coloca a palavra com a mesma ideia do de cima, mas coloca um espaço antes
            cursor += len(palavra) + 1    #aq, é pra andar o cursor até o final da palavra. tem o +1 pq tem o espaço
        else:
            texto = palavra + texto  #se o cursor for 0, estiver no inicio, n precisa colocar espaço antes. (eu n sei se a gente coloca espaço depois, faz sentido, mas n ta no enunciado)
            cursor += len(palavra)
    
    elif comando[0] == 'x':
        caracteres = list(texto) #transforma o texto em uma lista de caracteres
        caracteres.pop(cursor) #remove o caractere onde o cursor esta em cima
        texto = "".join(caracteres) #transforma a lista em string de volta
        



print(texto)



