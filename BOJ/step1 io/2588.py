#1. 입출력과 사칙연산

# 2588. 곱셈
a= int(input())
b= int(input())

print((a*(b%10)))
print((a*int(b/10%10)))
print((a*int(b/100%10)))
print(a*b)