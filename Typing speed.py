from time import *
import random as r

def mistakes(str1,str2):
    error=0
    for i in range(len(str1)):
        try:
            if str1[i]!=str2[i]:
                error=error+1
        except:
            error=error+1
    return error

def speedcount(starttime,endtime,inputstr):
    deftime=round(endtime-starttime,2)
    speed=len(inputstr)/deftime
    return round(speed)

ch='yes'
while True:
    if ch=='yes':
        print()
        print("_______________________________")
        print("\n***** Check Typing Speed *****")
        print("_______________________________\n")
        strings=["A database management system is a collection of interrelated data","Java is currently one of the most influential programming languages",
                 "JS is easy, simple and very compatible with HTML CSS","Variable is a name of a memory location where the data is stored"]
        str=r.choice(strings)
        print("String = ",str)
        print()
        starttime=time()
        inputstr=input("Enter above string : ")
        endtime=time()
        print()
        print("Typing speed = ",speedcount(starttime,endtime,inputstr),"Words/Sec")
        print("Mistakes = ",mistakes(str,inputstr))

        ch=input("If you want to continue check enter 'yes' otherwise 'no' : ")
    elif ch=='no':
        print("\nThank You !!!")
        break;
    else:
        print("\nSorry !! please enter right choice.")
        ch = input("If you want to continue check enter 'yes' otherwise 'no' : ")