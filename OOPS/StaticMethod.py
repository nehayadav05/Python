class Student:
    school="DPS"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student class")
    
s1=Student(76,65,90)       
s2=Student(89,79,78)

print(s1.avg())       
print(Student.getSchool()) 

Student.info()

     