def bfs(v):
    queue = []
    queue.append(v)
    visited[v]=1
    while queue:
        v = queue.pop(0)
        for i in range(n):
            if matrix[v][i] and not visited[i]:
                visited[i]=1
                queue.append(i)
        
        print(v,end=" ")



n = int(input('enter no of nodes: '))
print('enter adjacency matrix')
matrix = []
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

visited = [0]*n

v = int(input('enter the starting vertex: '))
bfs(v)