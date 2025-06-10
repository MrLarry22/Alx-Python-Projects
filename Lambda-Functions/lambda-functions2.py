#Use with sorted()
students=[("Alice", 90),("Bob", 80),("Clara",95)]
#sort by marks
#
sorted_students=sorted(students,key=lambda x:x[1])
print(sorted_students)