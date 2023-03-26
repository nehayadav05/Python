from array import*
ar=array('i',[])
n=int(input("Enter the length of an array: "))
for i in range(n):
    x=int(input("Enter the next value: "))
    ar.append(x)

print(ar)   

val=int(input("Enter the value to be searched: "))
k=0
for e in ar:
    if e==val:
        print(k)
        break
    k+=1 