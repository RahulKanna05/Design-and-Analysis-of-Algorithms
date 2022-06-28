def findMin(a,b)->int:
    if a<=b:
        return a
    else:
        return b

def allpairs()->None:
    for k in range(n):
        for i in range(n):
            if i!=k:
                for j in range(n):
                    if i!=j:
                        matrix[i][j] = findMin(matrix[i][j],matrix[i][k]+matrix[k][j])

matrix = []
n = int(input('enter the size: '))
print('enter the adjacency matrix')
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

for i in range(n):
    for j in range(n):
        if i!=j and matrix[i][j]==0:
            matrix[i][j]=int(1e9)

print('input matrix')
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end='    ')
    print()

allpairs()
print()
print('all pairs matrix')
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end='    ')
    print()
