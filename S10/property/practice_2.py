
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Use the setter to validate the radius
 
    @property
    def area(self):
        return 3.14 * (self._redius ** 2)
    
    @property
    def radius(self):
        return self._redius
    
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._redius = value
        else:
            raise ValueError(" Radius must be positive ")
        



#Ex
circle = Circle(5)  # Pass a valid positive radius
print(circle.area)


