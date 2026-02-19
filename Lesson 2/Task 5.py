secret_key="secret123"
login=False

while login==False:
    sifre=input("Sifrenizi daxil edin: ")
    if sifre==secret_key:
        login=True
        break
print("Girisiniz ugurlu oldu")