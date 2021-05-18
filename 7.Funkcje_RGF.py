#algorytm generujący funkcję RGF odpowiadającą zadanemu podziałowi zbioru
def rgf(n, k, B):
    F = []
    for j in range(1, n + 1):
        F.append(0)

    j = 1
    nr = 1

    for i in range(1, k + 1):
        while F[j - 1] != 0:
            j += 1
        h = 1
        while j not in B[h - 1]:
            h += 1
        for g in B[h - 1]:
            F[g - 1] = nr
        nr += 1

    return F

print(rgf(10, 4, [[3,6,7], [1,2], [5,8,9], [4,10]]))

#algorytm generujący podział zbioru{1, . . . , n} odpowiadający zadanej funkcji RGF
def rgf(n, F):
    max_nr = max(F)
    nr = 1
    B = []
    for i in range(max_nr):
        B.append([])

    for i in F:
        B[i - 1].append(nr)
        nr += 1

    return B

print(rgf(10, [1,1,2,3,4,2,2,4,4,3]))

