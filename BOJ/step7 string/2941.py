#2941	크로아티아 알파벳
arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()
 
for c in arr:
    w = w.replace(c, '*')
print(len(w))