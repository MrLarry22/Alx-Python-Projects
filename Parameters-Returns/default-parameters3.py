#pre-define a value for a parameter. If the user doesn’t give one, the default is used.
def calculate_area(length,width=5):
    return length * width

print(calculate_area(10))      # Uses default width = 5 → Output: 50
print(calculate_area(10, 2))   # Overrides default → Output: 20
