A = input()

for i in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    A = A.replace(i, '0')

print(len(A))
