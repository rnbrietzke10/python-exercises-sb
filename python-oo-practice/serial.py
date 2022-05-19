"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """
        Sets start to user input start 
        serial_num keeps track of current serial number
            - set to start - 1 to allow so first serial number is the same as the start serial number 

         """
        self.start = start
        self.serial_num  = start -1
    def __repr__(self):
        return f'SerialGenerator start={self.start} next={self.serial_num+2} '
    def generate(self):
        """
        Sets new serial number when generate is called.
        """
        self.serial_num += 1
        return self.serial_num

    def reset(self):
        """
        Sets serial_num back to it's original value.
        """
        self.serial_num = self.start - 1

