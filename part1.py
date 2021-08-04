## I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
## Any code taken from other sources is referenced within my code solution.

## Student ID: IIT Registration Number : 20200548 
##             UoW Registration Number: 18302417/1     
  
## Date: 30/04/2021


progress="Progress"   #using variables to store outcomes related to the result
trailer="Progress (module trailer)"
retriever="Do not Progress – module retriever"
excluded="Exclude"


studentPass=int(input("Please enter the number of credits at pass?"))
studentDefer=int(input("Please enter the number of credits at defer?"))
studentFail=int(input("Please enter the number of credits at fail?"))

total=studentPass+studentDefer+studentFail

if total!=120 :    #checking if the total is equal to 120
    print("Total incorrect!")
elif studentPass==120 and studentDefer==0 and studentFail==0:
    print(progress)
elif studentPass==100 and studentDefer==20 and studentFail==0:
    print(trailer)
elif studentPass==100 and studentDefer==0 and studentFail==20:
    print(trailer)
elif studentPass==80 and studentDefer==40 and studentFail==0:
    print(retriever)
elif studentPass==80 and studentDefer==20 and studentFail==20:
    print(retriever)
elif studentPass==80 and studentDefer==0 and studentFail==40:
    print(retriever)
elif studentPass==60 and studentDefer==60 and studentFail==0:
    print(retriever)
elif studentPass==60 and studentDefer==40 and studentFail==20:
    print(retriever)
elif studentPass==60 and studentDefer==20 and studentFail==40:
    print(retriever)
elif studentPass==60 and studentDefer==0 and studentFail==60: 
    print(retriever)
elif studentPass==40 and studentDefer==80 and studentFail==0: 
    print(retriever)
elif studentPass==40 and studentDefer==60 and studentFail==20: 
    print(retriever)
elif studentPass==40 and studentDefer==40 and studentFail==40:
    print(retriever)
elif studentPass==40 and studentDefer==20 and studentFail==60:
    print(retriever)
elif studentPass==40 and studentDefer==0 and studentFail==80:
    print(excluded)
elif studentPass==20 and studentDefer==100 and studentFail==0:
    print(retriever)
elif studentPass==20 and studentDefer==80 and studentFail==20:
    print(retriever)
elif studentPass==20 and studentDefer==60 and studentFail==40:
    print(retriever)
elif studentPass==20 and studentDefer==40 and studentFail==60:
    print(retriever)
elif studentPass==20 and studentDefer==20 and studentFail==80:
    print(excluded)
elif studentPass==20 and studentDefer==0 and studentFail==100:
    print(excluded)
elif studentPass==0 and studentDefer==120 and studentFail==0:
    print(retriever)
elif studentPass==0 and studentDefer==100 and studentFail==20:
    print(retriever)
elif studentPass==0 and studentDefer==80 and studentFail==40:
    print(retriever)
elif studentPass==0 and studentDefer==60 and studentFail==60:
    print(retriever)
elif studentPass==0 and studentDefer==40 and studentFail==80:
    print(excluded)
elif studentPass==0 and studentDefer==20 and studentFail==100:
    print(excluded)
elif studentPass==0 and studentDefer==0 and studentFail==120:
    print(excluded)
