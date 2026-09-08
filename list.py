#list => when order matters
score=[8,9,10,11]
score.append(12)
score[1]=20
print(score[1:3]) # 1 to 2
score.remove(10)

#didct=key oreder pair ,unordered,no duplicates
stud={"name":"s","age":20,}
print(stud["name"])
for key ,value in stud.items():
    print(key,"->",value)