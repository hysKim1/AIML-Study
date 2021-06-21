#4344   평균은 넘겠지
for _ in range(int(input())):
    arr=list(map(int,input().split()))
    n=arr[0]
    grade_arr=arr[1:]
    avg = sum(grade_arr)/n
    cnt=0
    for grade in grade_arr:
        if grade > avg:
            cnt +=1
    print('%.3f' %(cnt/n*100)+'%')