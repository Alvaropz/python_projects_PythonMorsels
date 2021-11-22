from math import sqrt
from decimal import Decimal
import cmath

def is_perfect_square(n, *, complex=False):
    if complex:
        root = cmath.sqrt(n)
        return root.real.is_integer() and root.imag.is_integer()
    if not (isinstance(n, int) or isinstance(n, float) or isinstance(n, Decimal)):
        raise TypeError
    if n < 0:
        return False
    if isinstance(n, float):
        if n % sqrt(n) == 0:
            return True
        return False
    if n % Decimal(n).sqrt() == 0:
        return True
    return False

