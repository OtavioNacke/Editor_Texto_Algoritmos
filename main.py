texto = 'Você sabia que sábia, sabia assobiar?'

#Declarar uma váriavel responsável pela ação
acao, sub_acao = input("Qual a ação desejada: ").split()

c = 0
while acao != 'F': 

    if acao == 'E':
        n = int(sub_acao)
        if sub_acao > len(texto):
            n = len(texto)
        c = n 
        print(texto[c])
    

    if acao == 'D':
        n = int(sub_acao)
        if n > len(texto) - c:
            n = len(texto) - c
        c = n
        print(texto[c])
        
    if acao == 'x':
        texto = texto.replace(texto[c] , '')
        print(texto)


    acao , sub_acao = input("Qual a ação desejada: ").split()
