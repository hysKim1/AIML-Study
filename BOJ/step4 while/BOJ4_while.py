#10952번 (A+B -5)
a,b = map(int, input().split())
while (a!=0 and b!=0):
    print(a+b)
    a, b=map(int,input().split())


#10951번 (A+B -4)
while True:
    try:
        a,b = map(int,input().split())
        print(a+b)
    except:
        break


#1110번-1 (더하기 사이클)
i = 0
a = int(input())
k=a
while 1:
  b = a//10+a%10
  c=a%10*10+b%10
  a=c
  i += 1
  if(a==k):
    break
print(i)