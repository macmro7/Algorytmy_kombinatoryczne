#algorytm obliczający metodą programowania dynamicznego liczbę podziałów liczby n na k składników
def podzial(n, k):
    n += 1
    k += 1
    P = []
    for i in range(n):
        P.append([0] * n)

    P[0][0] = 1

    for i in range(1, n):
        P[i][0] = 0
    for i in range(1, n):
        for j in range(1, min(i, k) + 1):
            P[i][j] = P[i - 1][j - 1] + P[i - j][j]

    return(P[n - 1][k - 1])

#algorytm generujący podział sprzężony do zadanego podziału (a1, . . . , am) liczby n
def podzial_sp(a):
    b = []
    for i in range(a[0]):
        b.append(1)

    for j in range(1, len(a)):
        for i in range(a[j]):
            b[i] += 1

    return b

#algorytm generujący wszystkie podziały liczby n w postaci normalnej
a = [0] * 5
def podzial_3(n, b, m):
    if n == 0:
        print(a[:m])

    else:
        for i in range(1, min(b, n) + 1):
            a[m] = i
            podzial_3(n - i, i, m + 1)

#algorytm generujący wszystkie podziały liczby n na k składników
a = [0] * 20
def podzial_g(n, b, m):
    if n == 0:
        b_l = podzial_sp(a[:m])
        print(b_l)
    else:
        for i in range(1, min(b, n) + 1):
            a[m] = i
            podzial_g(n - i, i, m + 1)

def podzial_4(n, k):
    a[0] = k
    podzial_g(n - k, k, 1)

print("zadanie 1\n")
print(podzial(5, 2))

print("\nzadanie 2\n")
print(podzial_sp([4, 3, 2, 2, 1]))

print("\nzadanie 3\n")
podzial_3(6, 6, 0)

print("\nzadanie 4")
podzial_4(10, 5)