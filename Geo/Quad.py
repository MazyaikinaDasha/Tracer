from GEO.Triangle import Triangle
from GEO.Geometry import Geometry
from GEO.Material import Material


class Quad(Geometry):
    def __init__(self, p0, p1, p2, p3, material=Material()):
        # Quad - это 2 треугольника, определяемые в порядке против часовой стрелки
        self.triList = [Triangle(p0, p1, p2), Triangle(p0, p2, p3)]
        self.material = material
        self.type = "Quad"

    def getIntersection(self, ray, closestHit, result):
        for eachTri in self.triList:
            if eachTri.getIntersection(ray, closestHit, result):
                # Важно, переопределяем идентификатор объекта, в противном случае будет возвращен идентификатор
                # треугольника, равный 0
                result[3] = self.objectId
                return True

        return False
