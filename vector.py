#diagnose before testing. Thank.
class Vector:
    
    def __init__(self, x = 0.0, y = 0.0):
        self.x = x 
        self.y = y
    
    def _repr_(self):
        return "Vector ({}, {})". format(self.x, self.y)
    
    def __add__(self, other):                                   # add coordinates
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):                                   # substitute
        return self.__add__(-1 * other)
    
    def __rmul__(self, a: float):
        return Vector(a * self.x, a * self.y)
    
    def __mul__(self, a: float):                                # multiply
        return self.__rmul__(a)
    
    def __truediv__(self, a: float):                            # divide 
        return self.__rmul__(1.0 / a)
    
    def __neg__(self):
        self.x *= -1
        self.y *= -1
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self. __eq__(other)
    
    @staticmethod
    def test():
        z = Vector(x = 5, y = 5)
        x = Vector(x = 4, y = 4)
        print('z is {}'. format(z))
        print('x is {}'. format(x))
        print('z + v is {}'. format(z + x))
        print('z - x is {}'. format(z - x))
        print('a * u is {}'. format(3* x))
        print('-u * x is {}'. format(-1 * x))
