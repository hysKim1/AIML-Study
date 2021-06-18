#1330	두 수 비교하기
a,b =map(int, input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')

#9498	시험성적
score =int(input())
if score >=90:
    print('A')
elif score >=80:
    print('B')
elif score >=70:
    print('C')
elif score >=60:
    print('D')
else :
    print('F')

#2753	윤년
year = int(input())

if year %4==0 and (year%100!=0| year %400==0) :
    print(1)
else:
    print(0)
#14681	사분면 고르기
x=int(input())
y=int(input())
if x>0 and y>0 :
    print(1)
elif x< 0 and y>0 :
     print(2)
elif x< 0 and y<0 :
     print(3)
else:
     print(4)

#	2884	알람 시계
hh,mm =map(int, input().split())

if mm<45:
    hh-=1
    mm+=15
    
    if hh <0:
        hh=23
else:
    mm-=45

print(hh,mm)