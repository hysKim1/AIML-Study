#1546   평균
N=int(input())
arr=list(map(int, input().split()))
M=max(arr)
for j in range(N):
    arr[j]=arr[j]*100/M
print( sum(arr)/N)