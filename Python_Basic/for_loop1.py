limit=int(input("Enter the limit:"));
for i in range(limit,0,-1):
    for j in range(0,i):
        print(j,end=' ')
    print("\n")
