def equilateral(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    if a == b == c:
        return True
    else:
        return False
def isosceles(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    if (a == b or b == c or a == c):
        return True
    else:
        return False

def scalene(sides):
    a, b, c = sides
    if a == 0 or b == 0 or c == 0:
        return False
    if a + b < c or b + c < a or a + c < b:
        return False
    if a !=b and a !=c and b !=c:
        return True
    else:
        return False