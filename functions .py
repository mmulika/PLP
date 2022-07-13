# def sum(a,b):
#     sum =(a + b)
#     print(sum)
#     return(sum)
# sum(2,4)

# def add(a, b):
    
#     sum = (a + b)
#     print(sum)
#     return(sum)
    
# add(50,50)

def commission():
     salary = int(input("enter  employee salary :"))
     sales =int(input("enter employee monthly sales :"))
     commission =(sales * 10)/100
     net = (commission + salary)
     if net >=10000 and net <=20000:
         print("bossy")
     else:
       
         print("mtu basic")
        

         print(net,commission)
     return (net,commission)
commission()