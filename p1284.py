import unittest
from collections import OrderedDict
from fractions import Fraction


def factorize(num):
    d = OrderedDict()
    i = 2
    while i <= num:
        if num % i == 0:
            d[i] = d.get(i, 0) + 1
            num /= i
        else:
            i += 1
    return d


def count_factors(factors):
    cnt = 1
    for num, idx in factors.items():
        cnt *= (idx + 1)

    return cnt


def p(n, m):
    n_factors = factorize(n)
    m_factors = factorize(m)

    n_factor_cnt = count_factors(n_factors)
    m_factor_cnt = count_factors(m_factors)

    # Every collision has the possibility = 1/u
    u = n_factor_cnt * m_factor_cnt

    # Counts the collisions
    v = 1
    for factor, n_idx in n_factors.items():
        if factor in m_factors:
            m_idx = m_factors[factor]
            v *= (min(n_idx, m_idx) + 1)

    f = Fraction(v, u)
    return [f.denominator, f.numerator]


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual([4, 1], p(3, 2))

    def test_2(self):
        self.assertEqual([6, 1], p(12, 6))

    def test_3(self):
        self.assertEqual([6, 1], p(6, 9))


if __name__ == '__main__':
    nums = [int(num) for num in raw_input().split()]
    for num in p(*nums):
        print num,
