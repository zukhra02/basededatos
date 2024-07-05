class NumberSequence:
    def __init__(self, start_number):
        self.start_number = start_number
        self.number_list = [start_number + i for i in range(10)]

    def get_list(self):
        return self.number_list

    def get_number_by_position(self, position):
        if 0 <= position < len(self.number_list):
            return self.number_list[position]
        else:
            raise IndexError("The position is out of the list's range")


sequence = NumberSequence(5)
# Shows the list of the next 10 numbers
print(sequence.get_list()) 
# Shows the number at position 3 
print(sequence.get_number_by_position(3))  