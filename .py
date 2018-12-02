import random
import time


oraclelist = ["Yes","No",
              "Maybe","Never",
              "Try again","Oops",
              "I am tired"]


r= random.randint(0,6)


def oracle():
    input("Enter your question...> ")
    print(oraclelist[r])
    time.sleep(1)
    dieOracle()

def dieOracle():
    yn =input("Try again?...> ")
    if yn=="Yes" or yn=="Y":
        oracle()
    elif yn=="No"or yn=="N":
        print("See you soon")
        quit()
        
    else:
        while True:
            ny=input("Invalid input, Yes or No..> ")
            if ny=="Yes" or "Y":
                oracle()
            elif ny=="No"or "N":
                quit()
        
    
print("Welcome...")
time.sleep(1)
oracle()

time.sleep(1)

