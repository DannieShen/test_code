
import unittest
class MathOperations:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y


class TestMathOperations(unittest.TestCase):

    def setUp(self):
        # 在每个测试方法执行前创建一个 MathOperations 实例
        self.calc = MathOperations()

    def test_add(self):
        # 测试加法
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)

    def test_subtract(self):
        # 测试减法
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)


if __name__ == '__main__':
    unittest.main()

