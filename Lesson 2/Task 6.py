import random

gizli_reqem=random.randint(1,10)

cehd_sayi=3

while cehd_sayi>0:
    texmin_edilen_reqem=int(input("Gizli reqemi daxil edin: "))
    if texmin_edilen_reqem>gizli_reqem:
        print("Daha Kicik reqem daxil edin: ")
        cehd_sayi=cehd_sayi-1
        if cehd_sayi==0:
            print("Cehd sayiniz bitmisdir")
            break
    elif texmin_edilen_reqem<gizli_reqem:
        print("Daha boyuk reqem daxil edin: ")
        cehd_sayi=cehd_sayi-1
        if cehd_sayi==0:
            print("Cehd sayiniz bitmisdir")
            break

    else:
        print(f"{texmin_edilen_reqem} duz tapdiniz")
        break
