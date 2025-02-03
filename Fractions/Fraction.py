class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if isinstance(numerator, str):
            try:
                numerator, denominator = map(int, numerator.strip().split("/"))
            except (AttributeError, ValueError):
                self.denominator = 0
                self.numerator = 1

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            self.numerator = 0
            self.denominator = 1
            return
        
        if denominator == 0:
            raise ZeroDivisionError("Invalid input")
        
        gcd_value = max(1, Fraction.gcd(abs(numerator), abs(denominator)))
        self.numerator = numerator // gcd_value * (-1 if denominator < 0 else 1)
        self.denominator = abs(denominator) // gcd_value
        

    def gcd(a, b):
        if a == 0 or b == 0:
            return 0
        while b != 0:
            a , b = b, a % b
        return a

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_fraction(self):
        if self.numerator == 0:
            return "0"
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else f"{self.numerator}"
        