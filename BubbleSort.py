import array


def bubblesort(arr):
 n=len(arr)

 for i in range(n):
    for j in range(0,n-j-1):
        if arr[j]>arr[j+1]:
            arr[j+1],arr[j]=arr[j],arr[j+1]

arr = [64, 34, 25, 12, 22, 11, 90]
  
bubblesort(arr)
  
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")           
        