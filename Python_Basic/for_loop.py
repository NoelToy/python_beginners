limit=int(input("Enter the limit:"))
#limit2=int(input("Enter the limit:"))
for i in range(0,limit):
    for j in range(0,i):
        print(j,end=' ')
    print('\n')