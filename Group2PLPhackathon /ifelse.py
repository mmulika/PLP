import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input("enter number:"))
    if(n % 2)==0 and (n % 2) in range(2,5):
        print("Not Weird")
    elif(n % 2)== 0 and (n % 2)in range(6,20):
        print("Weird")
        
    elif(n % 2)== 0 and(n % 2)>20:
        print("Not Wierd") 
    else:
        print("Weird")