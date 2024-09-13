number_of_students = int(input())
lst = []
top_scorers = []
top_score = 0
while number_of_students > 0:
    score = [n for n in input("Enter the student name and grade").split(" ")]
    lst.append(score)
    number_of_students -= 1

for x in lst:
    if int(x[1]) >= top_score:
        top_score = int(x[1])

for x in lst:
    if int(x[1]) == top_score: 
        top_scorers.append(x[0])
print(top_scorers)



