def firstrun():
    return "success"


def getArea(radius):
    if(radius >= 0):
        area = 3.14159 * radius * radius
        return area

    else:
        return None
