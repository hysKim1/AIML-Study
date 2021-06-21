#2562    최댓값
arr=[]
for i in range(9):
    arr.append(int(input()))
print(str(max(arr))+'\n'+str(arr.index(max(arr))+1))