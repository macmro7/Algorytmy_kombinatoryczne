#algorytm obliczający wartości liczb Stirlinga drugiego rodzaju
n = 4
k = 2

S = []
for i in range(n + 1):
    S.append([0] * (k + 1))

S[0][0] = 1

for i in range(1, n + 1):
    for j in range(k + 1):
        if i < j:
            S[i][j] = 0
        if j == 0 and i > 0:
            S[i][j] = 0
        else:
            S[i][j] = j * S[i - 1][j] + S[i - 1][j - 1]

print(S[n][k])

#algorytm obliczający wartości liczb Stirlinga pierwszego rodzaju
n = 6
k = 4

s = []
for i in range(n + 1):
    s.append([0] * (k + 1))

s[0][0] = 1

for i in range(1, n + 1):
    for j in range(k + 1):
        if i < j:
            s[i][j] = 0
        if j == 0 and i > 0:
            s[i][j] = 0
        else:
            s[i][j] = s[i - 1][j - 1] - (i - 1) * s[i - 1][j]

print(s[n][k])

#algorytm obliczający wartości liczb Bella

def factorial(n):
    number = 1
    for i in range(1, n + 1):
        number *= i

    return number

def newton(n, k):
    number = factorial(n) / (factorial(k) * factorial(n - k))

    return int(number)

def bella(n):

    B = []
    B.append(1)

    for i in range(1, n + 1):
        sum = 0
        for k in range(i):
            sum += newton(i - 1, k) * B[k]

        B.append(sum)

    return B[n]

print(bella(4))

