class Sunday():
    
    def __init__(self,name,contribution) :
        self.name =name
        self.contributiom =contribution
        
    def offering(self):
        print (self.contributiom)
s = Sunday("mike",3000)
s.offering()