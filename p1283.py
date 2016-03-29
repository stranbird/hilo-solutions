import unittest


class Test(unittest.TestCase):
    def test_1(self):
        lst = [1, 2, 4, 3, 5]
        self.assertListEqual([1, 2, 4], decrypt(lst))

    def test_2(self):
        lst = [2, 1, 4, 3, 5]
        self.assertListEqual([2, 1, 4], decrypt(lst))

    def test_3(self):
        lst = [1, 2, 3, 4, 5]
        self.assertListEqual([1], decrypt(lst))

    def test_4(self):
        lst = [5, 4, 3, 2, 1]
        self.assertListEqual([5, 4, 3, 2], decrypt(lst))

    def test_5(self):
        lst = [1]
        self.assertListEqual([1], decrypt(lst))


def decrypt(lst):
    next_num = float('inf')
    for num in reversed(lst):
        if num < next_num and len(lst) > 1:
            next_num = lst.pop()
        else:
            break

    return lst
