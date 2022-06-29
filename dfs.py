def dfs(v):
    global nodeCount
    visit[v] = 1
    for i in range(n):
        if matrix[v][i] and not visit[i]:
            print('{}->{}'.format(v,i))
            nodeCount+=1
            dfs(i)

n = int(input('enter no of nodes: '))
print('enter adjacency matrix')
matrix = []

for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)
nodeCount = 1
visit = [0]*n
dfs(0)

if nodeCount == n:
    print('grapgh is completed')
else:
    print('graph is not completed')