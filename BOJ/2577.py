#2577   숫자의 개수
arr=[]
prod=1

for i in range(3):
    prod *= int(input())
    
for j in range(10):
    arr.append(str(prod).count(str(j)))
    
for k in arr:
    print(k)