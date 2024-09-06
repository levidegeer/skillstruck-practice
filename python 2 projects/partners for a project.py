people = input()
people_lst = people.split()
people_lst.sort()
lst = []
for x in range(1,len(people_lst)//2+1):
    x = (people_lst[x-1], people_lst[-x])
    lst.append(x)
print(lst)