class Students:
    school="DPS"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.school
    
s1=Students(76,65,90)       
s2=Students(89,79,78)

print(s1.avg())       
print(Students.info())       