n = int(input('enter no of edges: '))
print("enter the adjacency matrix")
matrix = []
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            matrix[i][j] = 999

print('\ninput matrix')
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end='  ')
    print()

near = [-1]*n
edges = []
for i in range(n-1):
    edges.append([0,0])
minCost = 1e9
cost = 0
k = 0
l = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] < minCost:
            k = i
            l = j
            minCost = matrix[i][j]

cost+=matrix[k][l]
for i in range(n):
    if matrix[i][l]<matrix[i][k]:
        near[i] = l
    else:
        near[i]=k
    
near[k] = 0
near[l] = 0
minCost = 1e9
edges[0][0] = k
edges[0][1] = l

for i in range(1,n-1):
    index = 0
    for j in range(n):
        if near[j]!=0 and matrix[j][near[j]] < minCost:
            index = j
            minCost = matrix[j][near[j]]
    
    cost += matrix[index][near[index]]
    edges[i][0] = index
    edges[i][1] = near[index]
    near[index] = 0

    for k in range(n):
        if near[k]!=0 and matrix[k][index]<matrix[k][near[k]]:
            near[k] = index

    minCost = 1e9

print('the edges')
for i in range(n-1):
    print('({},{})'.format(edges[i][0]+1,edges[i][1]+1))

print('cost:',cost)
