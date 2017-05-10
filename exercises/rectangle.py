class Rectangle:
    # Construct a rectangle object 
    def __init__(self, width = 1, height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

