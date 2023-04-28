cores = [int(i) for i in input().split()]
rep = set()
ct = 0 

for cor in cores:
    if cores.count(cor) > 1 and cor not in rep:
        ct += cores.count(cor) - 1
        rep.add(cor)

print(ct)     
