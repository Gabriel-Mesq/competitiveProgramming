aux = input().split()
num_of_applicants = int(aux[0])
num_of_apartment = int(aux[1])
max_difference = int(aux[2])

desired_size = list(map(int, input().split()))
real_size = list(map(int, input().split()))

desired_size.sort()
real_size.sort()

n_aplicants = 0
n_apartment = 0
count = 0

while n_aplicants < num_of_applicants and n_apartment < num_of_apartment:

    if abs(desired_size[n_aplicants] - real_size[n_apartment]) <= max_difference:
        count += 1
        n_aplicants += 1
        n_apartment += 1
    elif desired_size[n_aplicants] < real_size[n_apartment]:
        n_aplicants += 1
    else:
        n_apartment += 1

print(count)
