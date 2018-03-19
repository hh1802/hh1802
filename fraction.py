from math import gcd


class Fraction(object):

    def __init__(self, num, den):
        if den == 0:
            raise ValueError('分母不能为0')
        self._num = num
        self._den = den
        # self.normalize()
        # self.simplify()

    @property
    def num(self):
        return self._num

    @property
    def den(self):
        return self._den

    def add(self, other):
        return Fraction(self._num * other.den + self._den * other.num,
                        self._den * other.den).simplify().normalize()

    def sub(self, other):
        return Fraction(self._num * other.den - self._den * other.num,
                        self._den * other.den).simplify().normalize()

    def mul(self, other):
        return Fraction(self._num * other.num, self._den * other.den)\
            .simplify().normalize()

    def div(self, other):
        return Fraction(self._num * other.den, self._den * other.num)\
            .simplify().normalize()

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)

    def __truediv__(self, other):
        return self.div(other)

    def simplify(self):
        if self._num != 0 and self._den != 1:
            factor = gcd(abs(self._num), abs(self._den))
            if factor > 1:
                self._num //= factor
                self._den //= factor
        return self

    def normalize(self):
        if self._den < 0:
            self._num = -self._num
            self._den = -self._den
        return self

    def __str__(self):
        if self._num == 0:
            return '0'
        elif self._den == 1:
            return str(self._num)
        else:
            return '%d/%d' % (self._num, self._den)


def main():
    f1 = Fraction(3, -6)
    f2 = Fraction(3, 4)
    print(f1)
    print(f2)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    print((f1 - f2) * f2)


if __name__ == '__main__':
    main()
