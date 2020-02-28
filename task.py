def firstrun():
    return "success"


def calcDate(d1, d2):
    numDays = d2 - d1
    return numDays


def getList(list):
    if len(list) == 0 or len(list) == 1:
        # print("List less than 2 objects.")
        return None

    else:
        newList = []
        newList.append(list[0])
        newList.append(list[len(list) - 1])
        return newList


def getArea(radius):
    if(radius >= 0):
        area = 3.14159 * radius * radius
        return area

    else:
        return None
