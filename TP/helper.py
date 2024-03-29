## Module de geometrie 2D
##

import math


class Helper(object):
#2
    def getAngledPoint(angle, longueur, cx, cy):
        x = (math.cos(angle) * longueur) + cx
        y = (math.sin(angle) * longueur) + cy
        return (x, y)

    getAngledPoint = staticmethod(getAngledPoint)
# 1
    def calcAngle(x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        angle = (math.atan2(dy, dx))
        return angle

    calcAngle = staticmethod(calcAngle)
#3
    def calcDistance(x1, y1, x2, y2):
        dx = abs(x2 - x1) ** 2
        dy = abs(y2 - y1) ** 2
        distance = math.sqrt(dx + dy)
        return distance

    calcDistance = staticmethod(calcDistance)
