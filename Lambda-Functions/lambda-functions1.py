#short, unnamed function you can write in one line
#quick, simple function (usually for things like filtering, mapping, or sorting).

#Use with filter()
numbers=[1,2,3,4,5]
even= list(filter(lambda x: x%2==0,numbers))
print(even)