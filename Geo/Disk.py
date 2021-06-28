from GEO.Plane import Plane
from GEO.Vector import Vector
from GEO.Material import Material


class Disk(Plane):
    def __init__(self, pos, radius, normal, material=Material()):
        self.pos = pos
        self.radius = radius
        self.normal = normal

        super().__init__(self.pos, self.normal)
        self.material = material
        self.type = "Disk"

    def getIntersection(self, ray, closestHit, result):
        if Plane.getIntersection(self, ray, closestHit, result):
            # находится ли эта точка в радиусе
            distToCenter = (result[1] - self.pos).length()

            if distToCenter <= self.radius:
                return True
            else:
                result.clear()
                return False
        else:
            result.clear()
            return False
