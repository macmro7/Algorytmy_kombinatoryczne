#algorytm generujący następnik permutacji p zbioru{1, . . . , n}w porządku leksyko-graficznym
def perm_nast(p):
    n = len(p)
    iPos = False

    for i in range(n - 2, 0, -1):
        if p[i] < p[i + 1]:
            iPos = i
            break

    if not iPos:
        return "brak nastepnika"

    for j in range(n - 1, 0, -1):
        if p[j] > p[iPos]:
            jPos = j
            break

    p[iPos], p[jPos] = p[jPos], p[iPos]

    pTemp = p.copy()

    temp = n

    for i in range(iPos + 1, n):
        temp -= 1
        pTemp[i] = p[temp]


    return pTemp

print(perm_nast([3, 6, 2, 7, 5, 4, 1]))

#algorytm obliczający rangę permutacji p zbioru{1, . . . , n} w porządku leksykograficz-nym
def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def perm_rank(p):
    r = 0
    n = len(p)

    for j in range(n):
        r += (p[j] - 1) * factorial(n - j - 1)
        for i in range(j + 1, n):
            if p[i] > p[j]:
                p[i] = p[i] - 1

    return r

print(perm_rank([2, 4, 1, 3]))

#algorytm wyznaczający permutację p zbioru{1, . . . , n} o randze r w porządku leksy-kograficznym
def perm(n, r):
    p = []
    for i in range(n):
        p.append(0)

    p[n - 1] = 1

    for j in range(n - 1):
        d = int((r % factorial(j + 2)) / factorial(j + 1))

        r = r - d * factorial(j + 1)
        p[n - j - 2] = d + 1

        for i in range(n - j - 1, n):
            if p[i] >= d + 1:
                p[i] += 1

    return p

print(perm(4, 10))
