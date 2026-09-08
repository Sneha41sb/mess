nums = [1, 2, 3, 4, 5]
squares = [x*10 for x in nums]
print(squares)

nums=[1,2,3]
sq=[a**2 for a in nums]
print(sq)

nums=[1,2,3]
ans=[b*10 for b in nums if b>2]
print(ans)

passed_names = [student["name"] for student in students if student["marks"] > 60]