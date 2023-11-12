#LAB-2
#Triplet and their Sum
a=[12,3,4,1,6,9]
sum=24
n=len(a)
for i in range(n-2):
    j=n-1
    k=i+1
    if(a[i]+a[j]+a[k]==sum):
        print(a[i],a[j],a[k])
    


    #Sorting an Array
a=[0,0,1,2,0,1,2,2,1]
n=len(a)
for i in range(n):
    for j in range(i+1,n):
        if a[i]<=a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
a.reverse()
print(a)