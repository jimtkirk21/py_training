def equilateral(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a > 0 and a == b and b == c:
        return True
    else:
        return False
    
def isosceles(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if not (a + b > c and a + c > b and b + c > a):
        return False
    return a == b or b == c or a == c

def scalene(sides):
    if len(sides) != 3:
        return False
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a==b or b==c or a==c):
        return False
    if not (a + b > c and a + c > b and b + c > a):
        return False
    return a != b or b != c or a != c