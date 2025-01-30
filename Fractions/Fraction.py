class Fraction(object):

    def __init__(self, numerator=0, denominator=1):
        if not isinstance(numerator, int) or not isinstance(denominator, int) or denominator == 0:
            raise ZeroDivisionError("Invalid input")
        
        gcd_value = Fraction.gcd(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd_value * (-1 if denominator < 0 else 1)
        self.denominator = abs(denominator) // gcd_value
        pass

    def gcd(a, b):
        low = min(a, b)
        while low > 0:
            if (a % low == 0 and b % low == 0):
                return low
            low -= 1

    def get_numerator(self):
        return self.numerator
        pass

    def get_denominator(self):
        return self.denominator
        pass

    def get_fraction(self):
        #TODO
        pass