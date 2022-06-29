def dijkstra():
    flag = [0]*n
    for i in range(n):
        dist[i] = matrix[v][i]
    
    for i in range(1,n):
        minCost = 1e9
        u=0
        for j in range(n):
            if not flag[j] and dist[j] < minCost:
                minCost = dist[j]
                u = j
                
        flag[u] = 1
        for k in range(n):
            if not flag[k] and (dist[u]+matrix[u][k]<dist[k]):
                dist[k] = dist[u]+matrix[u][k] 
    


n = int(input("enter no of nodes: "))
print('enter the adjacency matrix')
matrix=[]
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

for i in range(n):
    for j in range(n):
        if matrix[i][j]==0:
            matrix[i][j] = 999

v = int(input('enter the source vertex: '))
dist = [0]*n
dijkstra()
print('shortest paths from')
for i in range(n):
    if v!=i:
        print('({},{})={}'.format(v,i,dist[i]))