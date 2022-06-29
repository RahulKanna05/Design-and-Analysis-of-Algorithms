def knapsack():
    global cap,totalProfit
    for i in range(n):
        if weights[i]<cap:
            totalProfit += profits[i]
            cap -= weights[i]
            ratios[i]=1.0
        else:
            break
    
    if i<n:
        ratios[i] = cap/weights[i]
        totalProfit += profits[i]*ratios[i]

    print('weights and their ratios')
    for i in range(n):
        print('{}->{}'.format(weights[i],ratios[i]))
    
    print('total profits',totalProfit)


n = int(input('enter no of objects: '))
print("enter weigths")
weights = [int(i) for i in input().split()]
print('enter profits')
profits = [int(i) for i in input().split()]
cap = int(input('enter capacity: '))

ratios = [0.0]*n
for i in range(n):
    ratios[i] = profits[i]/weights[i]

for i in range(n):
    for j in range(n-i-1):
        if ratios[j] < ratios[j+1]:
            ratios[j],ratios[j+1] = ratios[j+1],ratios[j]
            profits[j],profits[j+1] = profits[j+1],profits[j]
            weights[j],weights[j+1] = weights[j+1],weights[j]

totalProfit = 0
knapsack()
