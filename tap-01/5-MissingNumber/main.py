n = int(input())
listaIncompleta = [int(i) for i in input().split()]

set_completa = set(range(1, n+1))
set_incompleta = set(listaIncompleta)
missing_number = set_completa - set_incompleta
print(missing_number.pop())
