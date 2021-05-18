#algorytm generujący wszystkie podzbiory zbioru {1, . . . , n} w porządku minimalnych zmian (Graya), wykorzystujący wagi Hamminga
def gray(n):
    A = [0] * n
    B = []

    print(B)

    while True:
        B = []
        sum = 0

        for i in A:
            sum += i

        if sum % 2 == 0:
            A[-1] = 1 - A[-1]

        else:
            i = n
            while i > 0:
                i -= 1
                if A[i] == 1:
                    A[i - 1] = 1 - A[i - 1]
                    break

            if i == 0:
                break

        for i in range(len(A)):
            if A[i] == 1:
                B.append(i + 1)

        print(B)

gray(3)

#algorytm obliczający rangę podzbioru T w uporządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1, . . . , n}

def grey_rank(n, T):
    r = 0
    b = 0

    for i in range(n - 1, -1, -1):
        if n - i in T:
            b = 1 - b
        if b == 1:
            r += pow(2, i)

    return r

print(grey_rank(4, [1, 3]))

#algorytm wyznaczający podzbiór T o zadanej pozycji r w uporządkowaniu minimalnych zmian (Graya) podzbiorów zbioru {1, . . . , n}

def gray_unrank(n, r):
    T = []
    c = 0

    for i in range(n - 1, -1, -1):
        b = r // pow(2, i)
        if b != c:
            T.append(n - i)

        c = b
        r = r - b * pow(2, i)

    return T

print(gray_unrank(4, 12))
