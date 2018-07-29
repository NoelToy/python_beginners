party_member=[]
limit=int(input("Enter the number of members:"));

for i in range(0,limit):
    temp=input("Enter the name:")
    party_member.append(temp)
print(party_member)

index=int(input("Enter the index:"))
temp=input("Enter the name:")
party_member.insert(index,temp)
print(party_member)

party_member.remove("Noel")
print(party_member)

party_member.reverse()
print(party_member)

party_member.sort()
print(party_member)