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