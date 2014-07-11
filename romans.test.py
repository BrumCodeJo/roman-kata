import unittest
from romans import Romans as R

class TestRomans(unittest.TestCase):

    def test_i(self):
        self.assertEqual(1, int(R("I")))

    def test_v(self):
        self.assertEqual(5, int(R("V")))

    def test_x(self):
        self.assertEqual(10, int(R("X")))

    def test_l(self):
        self.assertEqual(50, int(R("L")))

    def test_c(self):
        self.assertEqual(100, int(R("C")))

    def test_d(self):
        self.assertEqual(500, int(R("D")))

    def test_m(self):
        self.assertEqual(1000, int(R("M")))

    def test_ii(self):
        self.assertEqual(2, int(R("II")))

    def test_iv(self):
        self.assertEqual(4, int(R("IV")))

    def test_xlix(self):
        self.assertEqual(49, int(R("XLIX")))

    def test_mmm(self):
        self.assertEqual(3000, int(R("MMM")))

    def test_1(self):
        self.assertEqual("I", str(R(1)))

    def test_2(self):
        self.assertEqual("II", str(R(2)))

    def test_3000(self):
        self.assertEqual("MMM", str(R(3000)))

    def test_9(self):
        self.assertEqual("IX", str(R(9)))

    def test_49(self):
        self.assertEqual("XLIX", str(R(49)))

    def test_400(self):
        self.assertEqual("CD", str(R(400)))

    def test_900(self):
        self.assertEqual("CM", str(R(900)))

    def test_999(self):
        self.assertEqual("CMXCIX", str(R(999)))

if __name__ == '__main__':
    unittest.main()
