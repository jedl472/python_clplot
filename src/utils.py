import math

def distance(pointa, pointb):
    return math.sqrt(abs(((pointb[0]-pointa[0])**2)+((pointb[1]-pointa[1])**2)))


def angle_from_origin(pointa, origin): #úhel v pozitivním směru (ve stupnich)
    angle = 0
    if pointa[0]-origin[0] == 0:
        angle = 90
    else:
        angle = math.degrees(math.atan((pointa[1]-origin[1])/(pointa[0]-origin[0])))

    if pointa[0]-origin[0] >= 0 and pointa[1]-origin[1] >= 0: #kvadranty jed. kružnice, aby to fungovalo pro všechny hodnoty ok 
        return angle
    elif pointa[0]-origin[0] < 0 and pointa[1]-origin[1] >= 0:
        return angle+180
    elif pointa[0]-origin[0] <= 0 and pointa[1]-origin[1] < 0:
        return angle+180
    elif pointa[0]-origin[0] > 0 and pointa[1]-origin[1] < 0:
        return angle +360