def Palindrome_Check(str):
    flag=True;
    str_len = len(str)
    str_len1 = -1 * str_len
    i=0;
    j=-1;
    while (i <= str_len and j>=str_len1):
        if(str[i]!=str[j]):
            flag=False
            break
        i+=1
        j+=-1
    return flag


str=input("Please enter a string:")
#print(len(str))
str_len=len(str)
'''for i in range(0,str_len):
    print(str[i])'''
flag=Palindrome_Check(str)
if(flag):
    print(str," is a palindrome")
else:
    print(str," is not palindrome")


