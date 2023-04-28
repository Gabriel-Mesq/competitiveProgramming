sequence = input()

count = 1
max_count = 1

for i in range(1, len(sequence)):
    if sequence[i] == sequence[i-1]:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 1

print(max_count)
