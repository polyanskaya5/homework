4.1
from random import randrange as rnd
A=[rnd( 10) for i in range(10)]
print(A)
del A[4]
print(A)
4.2
k=int(input('������� ����� ��������-> '))
del A[k-1]
print(A)
4.5
from random import randrange as rnd
A=[rnd(-10,5) for i in range(10)]
print(A)
M=A[0]
for x in A:
    if x>M:
        M=x
del A[M]
print(A)
