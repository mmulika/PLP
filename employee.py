class Employee():
    #update
    def __init__(self, name, age,income):
     self.name = name
     self.age = age
     self.income =income
    def  details(self):
        print(self.name)
        print(self.age)
        print(self.income)
    
    def benefits(self):
        commission =(self.income * 10)/100
        return (commission)
employee1 =Employee('boss',10,1000)

print(employee1.details())
print(employee1.benefits())