qt_numeros, x = map(int, input().split())
nums = list(map(int, input().split()))

"""
Ideia inicial: Como tem dois loops, o código vai ter complexidade O(n^2). 

for i in range(qt_numeros):
    for j in range(i+1, qt_numeros):
        if nums[i] + nums[j] == x:
            print(i+1, j+1)
            exit()

print("IMPOSSIBLE")

Por isso, procurei sobre alternativas para o aninhamento de loops. 
E conheci a ideia de usar um dicionário para armazenar complementos.
Eis a segunda tentativa:
"""

dicionario_de_complementos = {}

for i in range(qt_numeros):
    
    complemento = x - nums[i]
    
    if complemento in dicionario_de_complementos:
        print(dicionario_de_complementos[complemento] + 1, i+1)
        exit()
    dicionario_de_complementos[nums[i]] = i

print("IMPOSSIBLE")

