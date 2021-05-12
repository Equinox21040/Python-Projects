a = ["A","B","C","D","E","F"]
b = [[]]
l = []
def combi(a):
    b = [[]]
    l = []
    for i in range(len(a)):
        s = a[i]
        for j in range(len(b)):
           d = list(b[j])
           l.append(list(d))
           d.append(s)
           l.append(list(d))
        b = list(l)
        l.clear()
    return b
print(combi(a))
