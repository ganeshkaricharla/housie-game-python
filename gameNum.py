import random
import os

def pickNum():
    pickedNum=[]
    for i in range(1,91):
        a=input()
        if a == 'n' or a == 'N':    
            num=random.randint(1,90)
            while num in pickedNum:
                num=random.randint(1,90)
            os.system("cls")
            pickedNum.append(num)
            pickedNum.sort()
            print("{} . Number ==>  {}  ".format(i,num))
            if i%5 == 0:
                print(*pickedNum,end=" ")
        else:
            break



