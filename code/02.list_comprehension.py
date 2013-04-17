[ord(x) for x in 'banana']

---

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]

---

days = range(1, 31)
hours = [day * 24 for day in days]
minutes = [hour * 60 for hour in hours]
table = zip(days, hours, minutes)

---

def divisors_of(n):
    l = []
    n = abs(int(n))
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l
l1 = divisors_of(200)


vs.


def divisors_of_lc(n):
    return [i for i in range(1, n + 1) if n % i == 0]
l2 = divisors_of_lc(200)

---

M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row2 = M[1]
row2_inv = row2[::-1]

INTERATIVO: Como posso obter a diagonal principal?

col2 = [row[1] for row in M]



diag = [M[i][i] for i in range(0, len(M))]

---

# EXEMPLO DE CONJUNTO
# QUEM SABE O QUE FAZ ESSE CODIGO?
import os
{os.path.splitext(filename)[1] for filename in os.listdir('.')}

# QUEM SABE O QUE FAZ ESSE CODIGO?
{filename: os.path.getsize(filename) for filename in os.listdir('.')}