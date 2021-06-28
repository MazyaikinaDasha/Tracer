from GEO.Geometry import Geometry
from GEO.Material import Material
from GEO.Vector import Vector


class Plane(Geometry):
    def __init__(self, pos, normal, material=Material()):
        # Это бесконечная плоскость
        super().__init__(material)
        self.type = "Plane"
        self.pos = pos
        self.normal = normal
        self.epsilon = 0.0001

    def getIntersection(self, ray, closestHit, result):
        if ray.dir.dot(self.normal) == 0:
            # лучу разрешается ударяться о заднюю сторону плоскости, но не параллельно
            return False

        t = (self.pos - ray.origin).dot(self.normal) / (ray.dir.dot(self.normal))

        if t < 0 or t >= closestHit:
            return False

        hitPos = ray.origin + ray.dir * t
        hitNormal = self.normal

        result.clear()
        result.extend([t, hitPos, hitNormal, self.objectId])

        return True
