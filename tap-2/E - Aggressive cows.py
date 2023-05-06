def agressive_cows(stalls, cows):
    
    stalls.sort()
    low = 0
    high = stalls[-1] - stalls[0]

    while low <= high:
        
        mid = (low + high) // 2
        prev_cow = stalls[0]
        count = 1

        for i in range(1, len(stalls)):
            if stalls[i] - prev_cow >= mid:
                count += 1
                prev_cow = stalls[i]

                if count == cows:
                    break

        if count == cows:
            low = mid + 1
            result = mid

        else:
            high = mid - 1

    return result

t = int(input())

for i in range(t):

    n, c = map(int, input().split())
    stalls = [int(input()) for j in range(n)]

    print(agressive_cows(stalls, c))
