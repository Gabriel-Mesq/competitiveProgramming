#Problema para strings de multiplas linhas 

texto = str(input())

for _ in range (texto.count("")):
    texto = texto.replace("\"", "``", 1)
    texto = texto.replace("\"", "''", 1)

print(texto)
