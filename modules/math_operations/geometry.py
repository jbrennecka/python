def area_rect(x, y):
    area = x * y
    return area
def area_tri(x, y, z):
    if x + y == z or y + z == x or x + z == y:
        return "cannot create, one side is equal to the sum of the other two"
    s = (x + y + z) / 2
    area = (s * (s - x) * (s - y) * (s - z)) ** 0.5
    return round(area, 3)
def area_circ(r):
    area = (r ** 2) * 3.14159
    return round(area, 3)