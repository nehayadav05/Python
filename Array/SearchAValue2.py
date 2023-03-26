from array import*
arr=array('i',[])
n=int(input("Enter the length of the array: "))
for i in range(n):
    x=int(input("Enter the next value:"))
    arr.append(x)
print(arr)
val=int(input("Enter the number to be searched: "))
print(arr.index(val))    