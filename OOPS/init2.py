class system:
    
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def confi(self):
        print("Config is ",self.cpu,self.ram)
        
comp1=system('i5',16)
comp2=system('Ryzen3',6)

comp1.confi()
comp2.confi()