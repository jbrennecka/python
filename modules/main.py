from math_operations import calculator, geometry

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10,4)
print("Subtraction result:", result)

result = geometry.area_circ(5)
print("area of circle:", result)

result = geometry.area_rect(4, 3)
print("area of rectangle:" , result)

result = geometry.area_tri(3, 2, 4)
print("area of triangle:", result)

result = geometry.area_tri(3, 2, 1)
print("area of triangle:", result)