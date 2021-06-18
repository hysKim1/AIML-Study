#2739	구구단
i=int(input())

for j in range(1,10):
    print(i, '*' ,j, '=', i*j)

#10950	A+B - 3
for _ in range(int(input())):
    print(sum(list(map(int,input().split()))))

#8398	합
total=0
for i in range(int(input())+1):
    total += i
print(total)

#15552   빠른 A+B
import sys
T = int(sys.stdin.readline())
for i in range(T):
    a, b = map(int,sys.stdin.readline().split())
    print(a+b)

#2741   N 찍기
for i in range(int(input())+1):
    print(i)

#2742   기찍 N
for i in range(int(input()),0,-1):
    print(i)

#11021 A+B-7
for i in range(int(input())):
    print("Case #{}:".format(i + 1), sum(map(int, input().split())))

##11022 A+B-8
for i in range(int(input())):
    a,b=map(int, input().split())
    print("Case #{}: {} + {} = {}".format(i + 1,a,b,a+b))

#2438  별찍기-1
for i in range(int(input())):
    print("' '{}*{}".format(int(input())-i,i+1))
#2439  별찍기-2
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(i))

##10871	X보다 작은 수
N,X=map(int,input().split())
A=list(input().split())
print(" ".join([i for i in A if int(i)<X]))