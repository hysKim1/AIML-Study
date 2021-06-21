#8958   OX퀴즈
for _ in range(int(input())):
    cnt,ans=0,0
    for j in input():
        cnt = cnt +1 if j=='O' else 0
        ans +=cnt
    print(ans)