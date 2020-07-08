import math

def point_in_polygon(*points)-> bool:
    check_point = points[0:2]
    points = points[2:]
    coordinate_x = []
    coordinate_y = []
    polygon_square = 0.0
    check_square = 0.0
    for i in range(len(points)):
        if (i % 2 == 0):
            coordinate_x.append(points[i])
        else:
            coordinate_y.append(points[i])
    polygon_square = find_square(coordinate_x, coordinate_y)
    aX = []
    bY = []
    aX.append(check_point[0])
    bY.append(check_point[1])
    for i in range(len(coordinate_x)):
        aX.append(coordinate_x[i])
        bY.append(coordinate_y[i])
        if(len(aX) == 3 and len(bY) == 3):
            lol = find_square(aX, bY)
            check_square += lol
            aX.pop(1)
            bY.pop(1)
    aX.append(coordinate_x[0])
    bY.append(coordinate_y[0])
    check_square += find_square(aX,bY)
    result = polygon_square == check_square
    return result
def find_square(coordinate_x, coordinate_y):
    square = 0.0
    first_coef = 0.0
    second_coef = 0.0
    for i in range(len(coordinate_x)):
        if (i != (len(coordinate_x))-1):
            first_coef += coordinate_x[i]*coordinate_y[i+1]
            second_coef += coordinate_y[i]*coordinate_x[i+1]
        else:
            first_coef += coordinate_x[i] * coordinate_y[0]
            second_coef += coordinate_y[i] * coordinate_x[0]
        square = math.fabs(first_coef - second_coef) / 2
    return(square)
#point_in_polygon(0, 0, -5, -10, 0, 1, 1, 1, 1, 0)

