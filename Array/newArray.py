from array import*
val=array('i',[7,8,9,8,6,6])
newArr=array(val.typecode, (a for a in val))
for e in newArr:
    print(e)