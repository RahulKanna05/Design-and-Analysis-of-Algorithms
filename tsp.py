def findMin(a,b):
    if a<b:
        return a
    else:
        return b

print('enter a 4x4 matrix')
matrix = []
for i in range(4):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

paths = [[0,1,2,3,0],[0,1,3,2,0],[0,2,1,3,0],[0,2,3,1,0],[0,3,1,2,0],[0,3,2,1,0]]
minCost = 1e9
spath = -1
for i in range(6):
    flag = 1
    cost = 0
    for j in range(4):
        if matrix[paths[i][j]][paths[i][j+1]]!=0:
            cost += matrix[paths[i][j]][paths[i][j+1]]
        else:
            flag=0
            break
    
    if flag == 1:
        minCost = findMin(cost,minCost)
        if minCost == cost:
            spath = i

print('shortest path:',paths[spath])
print('cost:',minCost)
    