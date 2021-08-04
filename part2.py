## I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
## Any code taken from other sources is referenced within my code solution.

## Student ID: IIT Registration Number : 20200548 
##             UoW Registration Number: 18302417/1     
  
## Date: 30/04/2021


progress="Progress \nNext student please!"
trailer="Progress (module trailer) \nNext student please!"
retriever="Do not Progress – module retriever \nNext student please!"
excluded="Exclude \nNext student please!"

credit=[0,20,40,60,80,100,120]  #creating a list to store valid credits

while True: #to get results of one after one repeatedly
    try:    #prevent entering something other than integer
        while True:
            studentPass=int(input("Please enter the number of credits at pass?"))
            if not(studentPass in credit):  #checking whether the input is a valid credit
                print("Out of range! Enter the credits at pass again.")
                continue
            else:
                break

        while True:
            studentDefer=int(input("Please enter the number of credits at defer?"))
            if not(studentDefer in credit):
                print("Out of range! Enter the credits at defer again.")
                continue
            else:
                break

        while True:
            studentFail=int(input("Please enter the number of credits at fail?"))
            if not(studentFail in credit):
                print("Out of range! Enter the credits at fail again.")
                continue
            else:
                break
            
    except ValueError:
        print("Integer Required! Try again from the beginning.")
        continue

    else:
        total=studentPass+studentDefer+studentFail

        if total!=120:  #checking whether the total is equal to 120
            print("Total incorrect! Try again from the beginning.")
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
