'''
Primeira ideia de solução (após descartar usar dois fors aninhados):

n, target = map(int, input().split())
valores = list(map(int, input().split()))

dicionario = {}

for _ in range(n):

    complemento = target - valores[_]

    if complemento in dicionario:
        #Print o index do complemento e index atual +1 (A resposta do exercicio começa os index em 1)
        print(dicionario[complemento] + 1, _ + 1)
        break

    else:
        dicionario[valores[_]] = _

else:
    print("IMPOSSIBLE")

'''

#Resolução Two-Pointer:
n, target = map(int, input().split())
valores = list(map(int, input().split()))

#enumerate retorna uma tupla contendo um índice e o valor correspondente em cada iteração. 
valores_indexados = [(valor, i) for i, valor in enumerate(valores)]
valores_indexados.sort()

# Inicia os ponteiros
i = 0
j = n - 1

while i < j:

    #[0] para acessar o primeiro elemento da tupla.
    soma = valores_indexados[i][0] + valores_indexados[j][0]
    
    if soma == target:
        print(valores_indexados[i][1] + 1, valores_indexados[j][1] + 1)
        break
    
    elif soma < target:
        i += 1
    
    else:
        j -= 1

else:
    print("IMPOSSIBLE")
