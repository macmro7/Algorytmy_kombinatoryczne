#algorytm wyznaczający następnik k-elementowego podzbioru T zbioru{1, . . . , n}
def podzbior_nast(T, k, n):
    print(T)
    U = T
    while True:
        i = k
        while i >= 1 and T[i - 1] == n - k + i:  # i - 1, bo od 0
            i -= 1
        if i == 0:
            return T
        else:
            T[i - 1] += 1
            for j in range(i, k): #i = i + 1
                T[j] = T[j - 1] + 1
            print(T)

podzbior_nast([1, 2, 7, 8], 4, 8)

#algorytm obliczający rangę k-elementowego podzbioru T zbioru{1, . . . , n} w uporządkowaniu leksykograficznym podzbiorów k-elementowych
def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i

    return number

def newton(n, k):
    number = factorial(n) / (factorial(k) * factorial(n - k))
    return number


def podzbior_rank(T, k, n):
    r = 0
    for i in range(1, k):
        if T[i - 1] + 1 <= T[i] - 1:
            for j in range(T[i - 1] + 1, T[i]): #T[i] - 1
                r += newton(n - j, k - i - 1)

    return int(r)

print(podzbior_rank([1, 2, 3], 3, 5))

#algorytm wyznaczający podzbiór T o randze r w uporządkowaniu leksykograficznym k-elementowych podzbiorów zbioru{1, . . . , n}

def podzbior_unrank(r, k, n):
    T = []
    x = 1
    for i in range(1, k + 1):
        while newton(n - x, k - i) <= r:
            r = r - newton(n - x, k - i)
            x += 1
        T.append(x)
        x += 1

    return T

print(podzbior_unrank(8, 3, 5))
