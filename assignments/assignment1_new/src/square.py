
class Square:
    """ Class represents single square and contains a number and reference 
        row, column and box it is part of"""
    def __init__(self, my_number, my_row, my_column, my_box): 
        self.my_number = my_number
        self.my_row = my_row
        self.my_column = my_column
        self.my_box = my_box
    
    # Returns True on legal, False on non legal
    def is_legal(self, number):
        if self.my_column.has_value(number) == False \
                and self.my_row.has_value(number) == False \
                and self.my_box.has_value(number) == False: 
            return True
        return False
    
    def set_number(self, number): 
        self.my_number = number
    
    def __str__(self):
        r = "|n:" + str(self.my_number) \
            + " r:" + str(self.my_row) \
            + " c:" + str(self.my_column) \
            + " b:" + str(self.my_box) + "|"
        return r

