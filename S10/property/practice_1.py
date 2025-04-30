
class Circle:
    def __init__(self, radius):
        self._redius = radius
 
    @property
    def area(self):
        return 3.14 * (self._redius ** 2)
    


circle = Circle(2)
print(circle.area)
