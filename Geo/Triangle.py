from GEO.Plane import Plane
from GEO.Vector import Vector
from GEO.Material import Material


class Triangle(Plane):
    def __init__(self, p0, p1, p2, material=Material()):
        # Определяем 3 вершины треугольника в порядке против часовой стрелки!
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.normal = (self.p1 - self.p0).cross(self.p2 - self.p0).normalized()
        self.pos = self.p0

        super().__init__(self.pos, self.normal)
        self.material = material
        self.type = "Triangle"

    def getIntersection(self, ray, closestHit, result):
        if Plane.getIntersection(self, ray, closestHit, result):
            if result[1] == self.p0 or result[1] == self.p1 or result[1] == self.p2:
                return True
            # 1. пересекает ли луч плоскость треугольника
            # 2. находится ли точка попадания внутри треугольника
            cross00 = (self.p1 - self.p0).cross(result[1] - self.p0)
            cross01 = (self.p2 - self.p1).cross(result[1] - self.p1)
            cross02 = (self.p0 - self.p2).cross(result[1] - self.p2)
            crossList = [cross00, cross01, cross02]
            dotList = []

            testCnt = 0
            for eachCross in crossList:
                if eachCross.length() == 0:
                    # Если точка попадания находится на одном из ребер, произведение равно нулю
                    testCnt += 1
                else:
                    if eachCross.normalized().dot(self.normal) > 0:
                        testCnt += 1

            if testCnt == 3:
                return True
            else:
                result.clear()
                return False

        else:
            result.clear() # Необходимо очистить список результатов, если возвращено значение false.
            # Результат будет возвращен в любом случае
            return False
