def robber(arr,n,x):

    sum = 0
    for i in range(0,n,x):
        sum = sum + arr[i]
    return sum

arr = [2,7,9,3,1]
n = len(arr)
x = 2
print(robber(arr,n,x))