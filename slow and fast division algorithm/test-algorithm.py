import unittest
from src.slow.restoring_division import restoring_division
from src.slow.non_restoring_division import non_restoring_division
from src.fast.srt_division import srt_division
from src.fast.newton_raphson_division import newton_raphson_division

class TestDivisionAlgorithms(unittest.TestCase):
    def test_restoring_division(self):
        self.assertEqual(restoring_division(25, 3), (8, 1))
    
    def test_non_restoring_division(self):
        self.assertEqual(non_restoring_division(25, 3), (8, 1))

    def test_srt_division(self):
        self.assertEqual(srt_division(25, 3), (8, 1))

    def test_newton_raphson_division(self):
        self.assertEqual(newton_raphson_division(25, 3), (8, 1))

if __name__ == '__main__':
    unittest.main()
