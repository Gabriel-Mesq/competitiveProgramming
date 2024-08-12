n_cities, n_towers = map(int, input().split())
cord_cities = list(map(int, input().split()))
cord_towers = list(map(int, input().split()))
distancias = []

for i in range(n_cities):
    
    min_dist = max(abs(cord_cities[0] - cord_towers[-1]), abs((cord_cities[-1] - cord_towers[0])))
    for j in range(n_towers):
        dist = abs(cord_cities[i] - cord_towers[j])
        if dist < min_dist:
            min_dist = dist
    
    #Vetor contendo para cada cidade, a distância para torre mais proxima
    distancias.append(min_dist)

print(max(distancias))