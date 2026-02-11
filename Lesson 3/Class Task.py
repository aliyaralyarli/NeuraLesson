telebe={
    "age":"18",
    "name":"Aliyar",
    "ixtisas":["IT","DEVELOPER"]
}

yeni_list=[]

for i in telebe.items():
    if "IT" in telebe["ixtisas"]:
        yeni_list.append(i)

print(yeni_list)