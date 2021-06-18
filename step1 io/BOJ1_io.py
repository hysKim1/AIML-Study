#1. 입출력과 사칙연산
#2557 Hello World
print("Hello World!")

# 10718 We love kriii
print('강한친구 대한육군')
print('강한친구 대한육군')

#10171 고양이  #역슬래쉬 \\
print("\\    /\\")
print(" )  ( ')")
print('''(  /  )''')
print(''' \\(__)|''')

#10172 개
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\\__|")

#1000 A+B
a,b = input().split()
print(int(a)+int(b))

# 1001. A - B
a,b = map(int, input().split())
print(a-b)

# 10998. A*B
a,b = map(int, input().split())
print(a*b)


# 1008. A/B
a,b = map(int, input().split())
print(a/b)


# 10869. 사칙연산
a,b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, sep='\n')


# 10430. 나머지
A,B,C = map(int, input().split())
print( (A+B) %C )
print(( (A%C) + (B%C) )%C)
print( (A*B) % C)
print(( (A%C) * (B%C) )%C)



# 2588. 곱셈
a= int(input())
b= int(input())

print((a*(b%10)))
print((a*int(b/10%10)))
print((a*int(b/100%10)))
print(a*b)