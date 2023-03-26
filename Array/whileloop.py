from array import*
val=array('i',[5,7,9,4,3])
newArr=array(val.typecode, (a*a for a in val))
i=0
while i <len(newArr):
 print(newArr[i])
 i+=1