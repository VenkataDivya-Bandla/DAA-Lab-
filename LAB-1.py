#LAB-1
#Leader Array
a=[16,17,4,3,5,2]

n=len(a)
max=a[-1]
for i in range(0,n-1):
    for j in range(i+1,n-1):
        if a[i]<a[j]:
            print(a[j])
        else:
            break
        
        
print(max)


#Sorting Array
def zigzag_sort(a):
    n = len(a)

    # Sort the input list in ascending order
    a.sort()

    # Swap adjacent elements starting from index 1
    for i in range(1, n - 1, 2):
        a[i], a[i + 1] = a[i + 1], a[i]

a = [4, 3, 7, 8, 6, 2, 1]
zigzag_sort(a)
print("Zigzag ordered array:", a)
