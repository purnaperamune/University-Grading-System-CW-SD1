## I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
## Any code taken from other sources is referenced within my code solution.

## Student ID: IIT Registration Number : 20200548 
##             UoW Registration Number: 18302417/1     
  
## Date: 30/04/2021

credit=[0,20,40,60,80,100,120]

progress="Progress \nThank you for using e-grading system!"
num_progress=0

trailer="Progress (module trailer) \nThank you for using e-grading system!"
num_trailer=0

retriever="Do not Progress – module retriever \nThank you for using e-grading system!"
num_retriever=0

excluded="Exclude \nThank you for using e-grading system!"
num_excluded=0


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
            num_progress+=1
        elif studentPass==100 and studentDefer==20 and studentFail==0:
            print(trailer)
            num_trailer+=1
        elif studentPass==100 and studentDefer==0 and studentFail==20:
            print(trailer)
            num_trailer+=1
        elif studentPass==80 and studentDefer==40 and studentFail==0:
            print(retriever)
            num_retriever+=1
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
            num_excluded+=1
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

    

    user=input("Do you want to enter another set of data? \nEnter 'y' for yes or 'q' to quit and view results:")
    if user=='q':
        break
    elif user=='y':
        continue

print("")
print("Histogram of academic scores of students.")
print("----------------------------------------")

a=num_progress  #assiging the value in 'num_progress' to a new variable called 'a' to reduce the code related to the histogram
b=num_trailer
c=num_retriever
d=num_excluded

print(f'{"Progress":10}{"Trailer":10}{"Retriever":10}{"Exclude ":10}')
for x in range(10):
        if a>0:
            print(f'{"   *":10}',end="")
            a=a-1
            if b>0:
                print(f'{"   *":10}',end="")
                b=b-1
                if c>0:
                    print(f'{"   *":10}',end="")
                    c=c-1
                    if d>0:
                        print(f'{"   *":10}')
                        d=d-1
                        
                        
        else:
            print(f'{"":10}',end="")
            if b>0:
                print(f'{"   *":20}',end="")
                b=b-1
                if c>0:
                    print(f'{"   *":30}',end="")
                    c=c-1
                    if d>0:
                        print(f'{"   *":10}',end="")
                        d=d-1
            else:
                print(f'{"":20}')
                if c>0:
                    print(f'{"   *":30}',end="")
                    c=c-1
                    if d>0:
                        print(f'{"   *":10}',end="")
                        d=d-1
                else:
                 print(f'{"":30}')
                 if d>0:
                     print(f'{"   *":10}',end="")
                     d=d-1

                     
tot_num=num_progress+num_trailer+num_retriever+num_excluded
print(tot_num,"outcomes in total.")








        
                    

                
                
         
