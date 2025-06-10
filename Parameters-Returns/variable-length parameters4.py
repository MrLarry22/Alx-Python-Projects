#you allow the function to accept many arguments, not just one or two.
#*args → for many positional arguments
#**kwargs → for many keyword arguments
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3))       # Output: 6
print(add_all(10, 20, 30, 40))# Output: 100


