##10871	X보다 작은 수
N,X=map(int,input().split())
A=list(input().split())
print(" ".join([i for i in A if int(i)<X]))