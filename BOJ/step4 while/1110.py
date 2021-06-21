#1110번 (더하기 사이클)
cnt = 0
a = int(input())
chk=a

while True:
  b = a//10+a%10
  c=a%10*10+b%10
  a=c
  cnt += 1
   
  if(a==chk):
    break    
print(cnt)