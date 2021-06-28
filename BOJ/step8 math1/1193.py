n=int(intput())
i=1
while(n>0):
    n-=i
    i+=1
i-=1
n1=n+i
n2=i-n1+1
if i%2 ==1:
    print('{0}/{1}.format(n2,n1)')
else:
    print('{0}/{1}.format(n1,n2)')
