import math
from GEO.Geometry import Geometry
from GEO.Material import Material


class Sphere(Geometry):
    def __init__(self, pos, radius, material=Material()):
        super().__init__(material)
        self.pos = pos
        self.radius = radius
        self.epsilon = 0.0001

    def getIntersection(self, ray, closestHit, result):
        # testing delta ----- b^2 - 4ac >=0
        a = 1  # ray.dir.dot(ray.dir)
        b = 2 * ray.dir.dot(ray.origin - self.pos)
        c = (ray.origin - self.pos).sqr() - math.pow(self.radius, 2)

        delta = b * b - 4 * a * c

        if delta < 0:
            return False
        else:
            t0 = (-b + math.sqrt(delta)) / (2 * a)
            t1 = (-b - math.sqrt(delta)) / (2 * a)

            if t0 > 0 and t1 > 0:  # корень должен быть положительным, иначе он находится за источником луча
                t = min(t0, t1)  # Важно!! Берем самое близкое (самое маленькое) значение
                if t >= closestHit: return False  # находится ли этот t позади ближайшего t, обнаруженного до сих пор
            elif t0 > 0 and t1 <= 0:
                t = t0  # исочник внутри сферы
            elif t1 > 0 and t0 <= 0:
                t = t1  # источник внутри сферы
            else:
                return False

            hitPos = ray.origin + ray.dir * t
            hitNormal = (hitPos - self.pos).normalized()

            result.clear()
            result.extend([t, hitPos, hitNormal, self.objectId])
            return True
