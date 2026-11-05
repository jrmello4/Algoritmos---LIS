def minimo(lis):
    if not lis:
        return 0

    n = len(lis)
    passos = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if lis[i] > lis[j]:
                if passos[j] + 1 > passos[i]:
                    passos[i] = max(passos[i], passos[j] + 1)
    
    return max(passos)

print(minimo([10, 22, 9, 33, 21, 50, 41, 60]))
