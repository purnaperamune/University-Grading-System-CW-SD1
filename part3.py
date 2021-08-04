## I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
## Any code taken from other sources is referenced within my code solution.

## Student ID: IIT Registration Number : 20200548 
##             UoW Registration Number: 18302417/1     
  
## Date: 30/04/2021


credit=[0,20,40,60,80,100,120]

progress="Progress \nThank you for using e-grading system!"
num_progress=0   #number of students who got the result as progress

trailer="Progress (module trailer) \nThank you for using e-grading system!"
num_trailer=0    #number of students who got the result as progress(module trailer)

retriever="Do not Progress – module retriever \nThank you for using e-grading system!"
num_retriever=0  #number of students who got the result as module retriever

excluded="Exclude \nThank you for using e-grading system!"
num_excluded=0   #number of students who got the result as exclude


while True:
    try:
        while True:
            studentPass=int(input("Please enter the number of credits at pass?"))
            if not(studentPass in credit):
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

        if total!=120:
            print("Total incorrect! Try again from the beginning.")
        elif studentPass==120 and studentDefer==0 and studentFail==0: 
            print(progress)
            num_progress+=1  #updating the value of students who got progress as the result
        elif studentPass==100 and studentDefer==20 and studentFail==0:
            print(trailer)
            num_trailer+=1  #updating the value of students who got progress(module trailer) as the result
        elif studentPass==100 and studentDefer==0 and studentFail==20:
            print(trailer)
            num_trailer+=1
        elif studentPass==80 and studentDefer==40 and studentFail==0:
            print(retriever)
            num_retriever+=1 #updating the value of students who got module retriever as the result
        elif studentPass==80 and studentDefer==20 and studentFail==20:
            print(retriever)
            num_retriever+=1
        elif studentPass==80 and studentDefer==0 and studentFail==40:
            print(retriever)
            num_retriever+=1
        elif studentPass==60 and studentDefer==60 and studentFail==0:
            print(retriever)
            num_retriever+=1
        elif studentPass==60 and studentDefer==40 and studentFail==20:
            print(retriever)
            num_retriever+=1
        elif studentPass==60 and studentDefer==20 and studentFail==40:
            print(retriever)
            num_retriever+=1
        elif studentPass==60 and studentDefer==0 and studentFail==60: 
            print(retriever)
            num_retriever+=1
        elif studentPass==40 and studentDefer==80 and studentFail==0: 
            print(retriever)
            num_retriever+=1
        elif studentPass==40 and studentDefer==60 and studentFail==20:
            print(retriever)
            num_retriever+=1
        elif studentPass==40 and studentDefer==40 and studentFail==40: 
            print(retriever)
            num_retriever+=1
        elif studentPass==40 and studentDefer==20 and studentFail==60: 
            print(retriever)
            num_retriever+=1
        elif studentPass==40 and studentDefer==0 and studentFail==80: 
            print(excluded)
            num_excluded+=1 ##updating the value of students who got exclude as the result
        elif studentPass==20 and studentDefer==100 and studentFail==0: 
            print(retriever)
            num_retriever+=1
        elif studentPass==20 and studentDefer==80 and studentFail==20: 
            print(retriever)
            num_retriever+=1
        elif studentPass==20 and studentDefer==60 and studentFail==40: 
            print(retriever)
            num_retriever+=1
        elif studentPass==20 and studentDefer==40 and studentFail==60: 
            print(retriever)
            num_retriever+=1
        elif studentPass==20 and studentDefer==20 and studentFail==80: 
            print(excluded)
            num_excluded+=1
        elif studentPass==20 and studentDefer==0 and studentFail==100:
            print(excluded)
            num_excluded+=1
        elif studentPass==0 and studentDefer==120 and studentFail==0: 
            print(retriever)
            num_retriever+=1
        elif studentPass==0 and studentDefer==100 and studentFail==20: 
            print(retriever)
            num_retriever+=1
        elif studentPass==0 and studentDefer==80 and studentFail==40: 
            print(retriever)
            num_retriever+=1
        elif studentPass==0 and studentDefer==60 and studentFail==60: 
            print(retriever)
            num_retriever+=1
        elif studentPass==0 and studentDefer==40 and studentFail==80: 
            print(excluded)
            num_excluded+=1
        elif studentPass==0 and studentDefer==20 and studentFail==100:
            print(excluded)
            num_excluded+=1
        elif studentPass==0 and studentDefer==0 and studentFail==120: 
            print(excluded)
            num_excluded+=1

    

    user=input("Do you want to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:") #checking whether there is another student to enter results
    if user=='q':
        break
    elif user=='y':
        continue

print("")
print("Histogram of academic scores of students.")
print("----------------------------------------")

print("Progress",f'{num_progress:>28}',":",end="")
for x in range(num_progress):
    print('*',end="")
print("")

print("Progress (module trailer)",f'{num_trailer:>11}',":",end="")
for y in range(num_trailer):
    print('*',end="")
print("")

print("Do not Progress – module retriever",f'{num_retriever:>2}',":",end="")
for m in range(num_retriever):
    print('*',end="")
print("")

print("Exclude",f'{num_excluded:>29}',":",end="")
for n in range(num_excluded):
    print('*',end="")
print("")

tot_num=num_progress+num_trailer+num_retriever+num_excluded
print()
print(tot_num,"outcomes in total.") #total number of students who entered marks







        
