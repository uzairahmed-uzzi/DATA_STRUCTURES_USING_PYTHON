arr=[4,6,8,2,0,3,65,1,9]
size=len(arr)
for x in range(size):
    curmin=arr[x]
    print(x)
    for y in range(1,size):
        print(y)
        if(arr[y]<curmin):
            [curmin,arr[y]]=[arr[y],curmin]

print(arr)