class Temperature:
    def __init__(self, centigrade):
        self.centigrade = centigrade

    @property
    def fahrenheit(self):
        return (self.centigrade * 1.8) + 32
    

# Example:
temp = Temperature(25)
print(f"Temperature in Celsius: {temp.centigrade}")
print(f"Temperature in Fahrenheit: {temp.fahrenheit}")


