numbers = [10, 45, 3, 99, 23]

en_boyuk_reqem=numbers[0]

for i in range(1,len(numbers)):
    if numbers[i]>en_boyuk_reqem:
        en_boyuk_reqem=numbers[i]
print(f"Listdeki en boyuk reqem: {en_boyuk_reqem}")