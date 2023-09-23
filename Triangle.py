# -*- coding: utf-8 -*-

def classifyTheTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'

    BEWARE: there may be a bug or two in this code
    """
    # require that the input values be >= 0 and <= 200
    if not all(map(lambda side: isinstance(side, int) and 0 < side <= 200, (a, b, c))):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if any(map(lambda sides: sides[0] + sides[1] <= sides[2], ((a, b, c), (b, c, a), (c, a, b)))):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if a == b == c:
        return 'Equilateral'
    elif any(map(lambda sides: sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2],
                 ((a, b, c), (b, c, a), (c, a, b)))):
        return 'Isosceles'
    elif any(map(lambda sides: sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2],
                 ((a, b, c), (b, c, a), (c, a, b)))):
        if any(map(lambda sides: sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2,
                   ((a, b, c), (b, c, a), (c, a, b)))):
            return 'Right'
        else:
            return 'Scalene'
    else:
        return 'NotATriangle'
