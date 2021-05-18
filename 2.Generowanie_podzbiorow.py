#algorytm obliczający pozycję podzbioru T⊂{1, . . . , n} w uporządkowaniu leksyko-graficznym
def podzbior_rank(n, T):
    s = 0
    for i in range(1, n + 1):
        if i in T:
            s += pow(2, (n - i))
    return s

print(podzbior_rank(5, [2, 3, 5]))

#algorytm wyznaczający podzbiór T o zadanej pozycji r w uporządkowaniu leksyko-graficznym

def reverse(T):
    R = []
    for i in T[::-1]:
        R.append(i)

    return R

def podzbior_unrank(n, r):
    T = []
    for i in range(n, 0, -1):
        if r % 2 == 1:
            T.append(i)
        r //= 2

    return reverse(T)

print(podzbior_unrank(5, 13))

#algorytm generujący w porządku leksykograficznym wszystkie ciągi długości n zbudowane z liczb od 1 do k

def ALG(x, i):
    if i == n - 1:
        print(x)

    else:
        for j in range(1, k + 1):
            x[i + 1] = j
            ALG(x, i + 1)

n = 4
k = 3
i = 0
x = [0] * n

ALG(x, i - 1)
