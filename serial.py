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
        self.start = start
        self.increment = start

    def __repr__(self):
        """Show representation"""
        return f"<SerialGenerator start={self.start} next={self.increment}>"

    def generate(self):
        before_increment = self.increment
        self.increment += 1
        return before_increment

    def reset(self):
        self.increment = self.start

