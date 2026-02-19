scores = {"Ali": 85, "Nigar": 92, "Tural": 78}

highest_score=scores["Ali"]
highest_stud=[]

for key,value in scores.items():
    if value > highest_score:
        highest_stud.append((key,value))
print(highest_stud)