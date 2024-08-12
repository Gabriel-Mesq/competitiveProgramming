#Pega a média do tempo
#Divisão inteira tempo atual // tempo para produção  ---> Soma os resultados
#Se for igual ou maior, usar como novo máximo
#Se menor, incrementar o tempo mínimo

n, target = map(int, input().split())
maquinas = list(map(int, input().split()))

min, max = 0, target * max(maquinas) 

while min < max:

    tempo = (min + max) // 2

    #Alternativa de uma linha para somatório do loop de for explícito
    produto = sum(tempo // maquina for maquina in maquinas)
    
    if produto  >= target:
        max = tempo
    else:
        min = tempo + 1

print(int(min))
