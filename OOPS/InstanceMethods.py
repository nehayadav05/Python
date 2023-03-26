class average:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
 
s1=average(90,87,65)      
s2=average(94,84,85)

print(s1.avg())      