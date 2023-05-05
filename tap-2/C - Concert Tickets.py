#Código funciona, mas não passa todos os casos de teste

aux = input().split()
n_tickets = int(aux[0])
n_customers = int(aux[1])

tickets_price = list(map(int, input().split()))
customers_price = list(map(int, input().split()))

tickets_price.sort(reverse=True)
customers_price.sort()

customers = 0
fail = 0

while customers < n_customers:
        
        for _ in range (len(tickets_price)):

            if tickets_price[_] <= customers_price[customers]:
                print(tickets_price[_])
                tickets_price.remove(tickets_price[_])
                customers += 1
                break
        else:
            customers += 1
            fail += 1

print("-1\n" * fail, end="")