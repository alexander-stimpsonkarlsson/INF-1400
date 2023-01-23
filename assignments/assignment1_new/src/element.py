
class Element:
    """ Class represents a row, column or box. Has reference 
        to 9 square objects """
    def __init__(self, type): 
        self.my_squares = []
        self.my_type = type
    
    def add_square(self, square):
        self.my_squares.append(square)

    def has_value(self, value): 
        for square in self.my_squares: 
            if value == square.my_number: 
                return True
        return False

