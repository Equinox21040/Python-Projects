
a = [1,1,0,1,1,1,1,0,0,1,0]

par = 0
for i in a:
    if i == 1:
        par = par + 1

if par % 2 == 1:
    a.insert(0,1)
else:
    a.insert(0,0)

for i in range(4):
    pos = 2**i
    a.insert(pos,0)


print(a)

buffer_list = []
buffer = []
for i in range(4):
    for j in range(4):
        position = 4*i + j
        buffer_list.append(a[position])
    buffer.append(list(buffer_list))
    buffer_list.clear()

a = buffer

print(a)

def parityc(arr,c1,c2):
    arr = list(arr)
    paric = 0
    for i in range(4):
        if arr[i][c1] == 1:
            paric = paric + 1
    for j in range(4):
        if arr[j][c2] == 1:
            paric = paric + 1
    return paric

def parityr(arr, r1, r2):
    arr = list(arr)
    parir = 0
    for i in range(4):
        if arr[r1][i] == 1:
            parir = parir + 1
    for j in range(4):
        if arr[r2][j] == 1:
            parir = parir + 1

    return parir

if parityc(arr=a , c1 = 2, c2 = 3) % 2 == 1:
    a[0][1] = 1

if parityc(arr = a, c1 = 1, c2 = 3) % 2 == 1:
    a[0][3] = 1

if parityr(arr = a , r1 = 2, r2 = 3) % 2 == 1:
    a[1][0] = 1

if parityr(arr=a,r1=1,r2=3) % 2 == 1:
    a[2][0] = 1

print(a)
