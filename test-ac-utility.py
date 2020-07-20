import unittest
import ac_utility as ac

class TestAcUtility(unittest.TestCase):

    def test_quadratic_equation(self):
        roots = ac.get_roots(1, 2, 1)

        self.assertEqual(roots['x1'], -1.000000)
        self.assertEqual(roots['x2'], -1.000000)

if __name__ == '__main__':
    unittest.main()
