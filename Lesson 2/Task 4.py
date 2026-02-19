limit=int(input("Enter limit: "))
cem=0

for i in range(1,limit+1):
    if i%2==0:
        cem=cem+i

print(cem)