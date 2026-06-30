texto = input()

cursor = 0
while True:
    comando = input().split() #divide o input no comando e no argumento

    if comando[0] == 'F': #quebra o loop se o comando for F
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
        texto = texto[:cursor] + char + texto[cursor:]   #aqui ele pega o texto antes do cursor [:cursor], coloca o char e depois pega o texto depois do cursor [cursor:]

        cursor += 1             #para andar o cursor para a direita, pois ele acabou de adicionar um caractere, então o cursor precisa ir para a posição seguinte

    elif comando[0] == 'I':
        palavra = comando[1] #pega a palavra
        if cursor != 0:
            texto = texto[:cursor] + ' ' + palavra + texto[cursor:]  #coloca a palavra com a mesma ideia do de cima, mas coloca um espaço antes
            cursor += len(palavra) + 1    #aqui, é pra andar o cursor até o final da palavra. tem o +1 pq tem o espaço
        else:
            texto = palavra + texto  #se o cursor for 0, estiver no inicio, não precisa colocar espaço antes.
            cursor += len(palavra)
    
    elif comando[0] == 'x':
        if cursor < len(texto): #se o cursor estiver no final do texto, não faz nada
            caracteres = list(texto) #transforma o texto em uma lista de caracteres
            caracteres.pop(cursor) #remove o caractere depois do cursor
            texto = "".join(caracteres) #transforma a lista em string de volta
    

    elif comando[0] == 'X':

        if cursor < len(texto) and texto[cursor] not in " .,": #não estar em um espaço, ponto ou vírgula

            inicio = cursor #começar a contar do cursor
            fim = cursor    #começar a contar do cursor

            
            while inicio > 0 and texto[inicio-1] not in " .,": #achar inicio da palavra, inicio > 0 pois não pode ir pra posição -1
                inicio -= 1    #vai voltando até achar um espaço, ponto ou vírgula

            
            while fim < len(texto) and texto[fim] not in " .,": #achar fim da palavra, fim < len(texto) pois não pode ir pro final
                fim += 1   #vai andando até achar um espaço, ponto ou vírgula

            if inicio > 0 and texto[inicio-1] == " ": #remover o espaço antes da palavra
                inicio -= 1 

            texto = texto[:inicio] + texto[fim:] #remover a palavra do texto, pegando o texto antes do inicio e depois do fim da palavra
            cursor = inicio #posicionar antes da proxima palavra



print(texto)



