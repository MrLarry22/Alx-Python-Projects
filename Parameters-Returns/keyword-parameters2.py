#specify which argument goes to which parameter by name, not order
def calculate_area(length,width):
    return length * width

print(calculate_area(width=5, length=10))  # Same result: 50
