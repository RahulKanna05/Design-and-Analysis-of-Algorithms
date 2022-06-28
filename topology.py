def findInorder():
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += matrix[i][j]
        inorder.append(sum)

def topology():
    findInorder()
    topOrder = []
    temp = []
    for i in range(n):
        if inorder[i] == 0:
            temp.append(i)
    
    while temp:
        u = temp.pop()
        topOrder.append(u+1)
        for v in range(n):
            if matrix[u][v]:
                inorder[v]-=1
                if inorder[v]==0:
                    temp.append(v)

    print('topology order is ',end='')
    for i in topOrder:
        print(i,end=' ')


n = int(input('enter the size: '))
matrix = []
inorder = []
print("enter adjacency matrix")
for i in range(n):
    arr = [int(i) for i in input().split()]
    matrix.append(arr)

topology()