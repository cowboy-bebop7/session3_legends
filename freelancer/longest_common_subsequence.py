def lcs(u,v):
    for r in range(len(u)+1):
        lcs[r][len(v)+1]=0
    for c in range(len(v)+1):
        lcs[len(v)+1][c]=0
    return m
u="abc"
v="dfg"
m=[0 for i in range(len(u))
        for j in range(len(v))]
print(lcs(u,v))