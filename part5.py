## I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
## Any code taken from other sources is referenced within my code solution.

## Student ID: IIT Registration Number : 20200548 
##             UoW Registration Number: 18302417/1     
  
## Date: 30/04/2021

scores=[[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]] #storing results in a list. you can input more results in this list and check for their outputs too.

progress="Progress"   #using variables to store outcomes related to the result
trailer="Progress (module trailer)"
retriever="Do not Progress – module retriever"
excluded="Exclude"

num_progress=0
num_trailer=0
num_retriever=0
num_excluded=0

for x in scores:
    if x==[120,0,0]:
        print(progress)
        num_progress+=1
    elif x==[100,20,0]:
        print(trailer)
        num_trailer+=1
    elif x==[100,0,20]:
        print(trailer)
        num_trailer+=1
    elif x==[80,40,0]:
        print(retriever)
        num_retriever+=1 
    elif x==[80,20,20]:
        print(retriever)
        num_retriever+=1
    elif x==[80,0,40]:
        print(retriever)
        num_retriever+=1
    elif x==[60,60,0]:
        print(retriever)
        num_retriever+=1
    elif x==[60,40,20]:
        print(retriever)
        num_retriever+=1
    elif x==[60,20,40]:
        print(retriever)
        num_retriever+=1
    elif x==[60,0,60]: 
        print(retriever)
        num_retriever+=1
    elif x==[40,80,0]: 
        print(retriever)
        num_retriever+=1
    elif x==[40,60,20]:
        print(retriever)
        num_retriever+=1
    elif x==[40,40,40]: 
        print(retriever)
        num_retriever+=1
    elif x==[40,20,60]: 
        print(retriever)
        num_retriever+=1
    elif x==[40,0,80]: 
        print(excluded)
        num_excluded+=1 
    elif x==[20,100,0]: 
        print(retriever)
        num_retriever+=1
    elif x==[20,80,20]: 
        print(retriever)
        num_retriever+=1
    elif x==[20,60,40]: 
        print(retriever)
        num_retriever+=1
    elif x==[20 ,40,60]: 
        print(retriever)
        num_retriever+=1
    elif x==[20 ,20,80]: 
        print(excluded)
        num_excluded+=1
    elif x==[20,0,100]:
        print(excluded)
        num_excluded+=1
    elif x==[0 ,120,0]: 
        print(retriever)
        num_retriever+=1
    elif x==[0,100,20]: 
        print(retriever)
        num_retriever+=1
    elif x==[0,80,40]: 
        print(retriever)
        num_retriever+=1
    elif x==[0 ,60 ,60]: 
        print(retriever)
        num_retriever+=1
    elif x==[0,40,80]: 
        print(excluded)
        num_excluded+=1
    elif x==[0 ,20,100]:
        print(excluded)
        num_excluded+=1
    elif x==[0,0 ,120]: 
        print(excluded)
        num_excluded+=1

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
print(tot_num,"outcomes in total.")
