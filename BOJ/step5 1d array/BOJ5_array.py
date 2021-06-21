#10818   최소, 최대
N = int(input())
arr = list(map(int, input().split()))
print(min(arr), max(arr))

#2562    최댓값
arr=[]
for i in range(0):
    arr.append(int(input()))
    
print(str(max(arr))+'\n'+str(arr.index(max(arr))+1))

#2577   숫자의 개수
A = int(input())
B = int(input())
C = int(input())

num_list = list(str(A * B * C))

for i in range(10):
    print(num_list.count(str(i)))

#3052   나머지
arr=[]
for i in range(10):
    n=int(input())%42
    if n not in arr:
        arr.append(n)
print(len(arr))

#1546   평균
N=int(input())
arr=list(map(int, input().split()))
M=max(arr)
for j in range(N):
    arr[j]=arr[j]*100/M
print( sum(arr)/N)

#8958   OX퀴즈
for _ in range(int(input())):
    cnt,ans=0,0
    for j in input():
        cnt = cnt +1 if j=='O' else 0
        ans +=cnt
    print(ans)

#4344   평균은 넘겠지
for _ in range(int(input())):
    arr=list(map(int,input().split()))
    n=arr[0]
    grade_arr=arr[1:]
    avg = sum(grade_arr)/n
    cnt=0
    for grade in grade_arr:
        if grade > avg:
            cnt +=1
    print('%.3f' %(cnt/n*100)+'%')