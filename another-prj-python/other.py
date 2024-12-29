import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"The roots are real and distinct: {root1} and {root2}"
    
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return f"The root is real and repeated: {root}"
    
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        return f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"

# Input coefficients a, b, and c
print("Solve the quadratic equation ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the quadratic equation
result = solve_quadratic(a, b, c)
print(result)
