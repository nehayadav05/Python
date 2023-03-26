from array import*
val=array('i',[4,6,3,5,2])
newArr=array(val.typecode, (a*a for a in val))
for j in newArr:
    print(j)