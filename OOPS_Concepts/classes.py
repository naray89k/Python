class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height


    def area(self):
        return self.width * self.height


    def perimeter(self):
        return 2 * (self.width + self.height)


    def __str__(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)


    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)


    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False


    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            return NotImplemented



if __name__ == "__main__":
    rectangle1 = Rectangle(10,10)
    rectangle2 = Rectangle(10,10)
    rectangle3 = Rectangle(15,10)
    print(rectangle1 == rectangle2)
    print(rectangle3 > rectangle2)
    print(rectangle1 > rectangle3)
#print(5 + 10)
