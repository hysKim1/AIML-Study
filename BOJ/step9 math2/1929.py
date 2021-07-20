#1929 소수 구하기
#1 short ver.
M,N=map(int,input().split())
*s,=range(N+1)

for i in s[2:]:
    if s[i]:
        s[2*i::i]=[0]*(N//i-1)
        if(i>=M):print(i)
#2            
n1, n2= map(int, input().split())
li = [1]*(n2+1)
for i in range(2, int((n2+1)**0.5) + 1):
    if li[i] == 1:
        for j in range(i+i, n2+1, i):
            li[j] = 0
for i in range(n1, n2+1):
    if li[i] == 1 and i > 1:
        print(i)
