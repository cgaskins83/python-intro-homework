list1 = ["Python", "Java", "Javascript", "SQL", "C", "Ruby"]
list2 = ["GO", "SQL", "Java", "PHP", "Python", "Swift"]

#convert list to set
set_list1 = set(list1)
set_list2 = set(list2)

#prints both list with no duplicates 
print(set_list1.union(set_list2))

#print languages in both lists
print(set_list1.intersection(set_list2))

#print differences in both lists
print(set_list1.difference(set_list2))