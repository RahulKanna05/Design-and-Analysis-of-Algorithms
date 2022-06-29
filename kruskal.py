def findParent(i):
    while p[i]!=-1:
        i = p[i]
    return i

def union(a,b):
    p[a]=b


n = int(input('enter no of vertices: '))
matrix = []
print('enter the adjacency matrix')
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            matrix[i][j] = 999

p = [-1]*n
edgeCount = 1
minCost = 1e9
cost = 0
while edgeCount<n:
    v1 = 0
    v2 = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < minCost:
                v1 = i
                v2 = j
                minCost = matrix[i][j]

    u = findParent(v1)
    v = findParent(v2)

    if u!=v:
        union(u,v)
        cost += matrix[v1][v2]
        edgeCount+=1
        print('({},{})={}'.format(v1,v2,matrix[v1][v2]))

    matrix[v1][v2]=999
    matrix[v2][v1]=999
    minCost = 1e9

print('total cost:',cost)