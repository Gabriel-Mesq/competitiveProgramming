#Resolução !!!Three-Pointer!!!:

n, target = map(int, input().split())
valores = list(map(int, input().split()))

#enumerate retorna uma tupla contendo um índice e o valor correspondente em cada iteração. 
valores_indexados = [(valor, i) for i, valor in enumerate(valores)]
valores_indexados.sort()

# Inicia os ponteiros
i = 0
j = 1
k = n - 1

for i in range(n - 2):

    #Evitar repetições reduntantes
    if i > 0 and valores_indexados[i][0] == valores_indexados[i-1][0]:
            continue

    j = i + 1
    k = n - 1

    while j < k:

        #[0] para acessar o primeiro elemento da tupla.
        soma = valores_indexados[i][0] + valores_indexados[j][0] + valores_indexados[k][0]
        
        if soma == target:
            print(valores_indexados[i][1] + 1, valores_indexados[j][1] + 1, valores_indexados[k][1] + 1)
            break

        elif soma < target:

            # Ignora elementos iguais ou redundantes
            while j < k and valores_indexados[j][0] == valores_indexados[j+1][0]:
                j += 1
            j += 1
        
        else:
        
            # Ignora elementos iguais ou redundantes
            while j < k and valores_indexados[k][0] == valores_indexados[k-1][0]:
                k -= 1
            k -= 1
        
else:
    print("IMPOSSIBLE")
