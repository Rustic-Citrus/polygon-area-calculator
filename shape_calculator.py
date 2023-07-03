class Rectangle:
    def __init__(self, width: int, height: int):
        """Initializes Rectangle object with width (int) and height (int)."""
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("width and height must be integers.")
        self.width = width
        self.height = height
        
    def __str__(self) -> str:
        """Returns a string representation of Rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, value: int):
        """Accepts an integer and sets the width attribute of the Rectangle 
        object to that integer."""
        if not isinstance(value, int):
            raise ValueError("width must be integer.")
        self.width = value

    def set_height(self, value: int):
        """Accepts an integer and sets the height attribute of the Rectangle 
        object to that integer."""
        if not isinstance(value, int):
            raise ValueError("height must be integer.")
        self.height = value

    def get_area(self) -> int:
        """Calculates the area of the Rectangle and returns an integer."""
        area = self.width * self.height
        return area

    def get_perimeter(self) -> int:
        """Calculates the perimeter of the Rectangle and returns an integer."""
        perimeter = self.width * 2 + self.height * 2
        return perimeter

    def get_diagonal(self) -> float:
        """Calculates the diagonal of the Rectangle and returns an integer."""
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal

    def get_picture(self) -> str:
        """Returns a string representation of the Rectangle using asterisk 
        characters. If either of the sides of the Rectangle is longer than 50, 
        returns a string with 'Too big for picture.'"""
        if (self.height > 50) or (self.width > 50):
            return "Too big for picture."
        else:
            picture = "".join(["*" * self.width + "\n" for n in range(self.height)])
            return picture

    def get_amount_inside(self, shape) -> int:
        """Accepts either a Rectangle or a Square object as an argument and 
        returns an integer representing the number of times the passed object 
        fits into the current instance."""
        amount_inside = int(self.get_area() / shape.get_area())
        return amount_inside

class Square(Rectangle):
    def __init__(self, side: int):
        """Initializes Square object with width (int) and height (int)."""
        if not isinstance(side, int):
            raise ValueError("side must be integer.")
        self.width = side
        self.height = side

    def __str__(self):
        """Returns a string representation of Square."""
        return f"Square(side={self.width})"

    def set_side(self, side: int):
        """Accepts an integer as an argument and sets the width and height 
        attributes to the value of the passed integer."""
        if not isinstance(side, int):
            raise ValueError("side must be integer.")
        self.width = side
        self.height = side

    def set_height(self, value):
        """Accepts an integer as an argument and sets the height attribute to 
        the value of the passed integer."""
        return self.set_side(value)
    
    def set_width(self, value):
        """Accepts an integer as an argument and sets the width attribute to 
        the value of the passed integer."""
        return self.set_side(value)

