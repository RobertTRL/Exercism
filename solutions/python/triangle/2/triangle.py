def equilateral(sides):
    a, b, c = sides
    if (a==0 or b==0 or c==0) or (a+b<c or b+c< a or c+a<b):
        return False
    else:
        return a == b == c
        
def isosceles(sides):
    a, b, c = sides
    if (a==0 or b==0 or c==0) or (a+b<c or b+c< a or c+a<b):
        return False
    else:
        return a==b or a==c or b==c
    
def scalene(sides):
    a, b, c = sides
    if (a==0 or b==0 or c==0) or (a+b<c or b+c< a or c+a<b):
        return False
    else:
        return a !=b and a !=c and b !=c