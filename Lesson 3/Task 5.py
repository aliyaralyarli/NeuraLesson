numbers = [1, 2, 2, 3, 3, 3]

saylar={}

for eded in numbers:
    if eded in saylar:
        saylar[eded]+=1
    else:
        saylar[eded]=1
print(saylar)