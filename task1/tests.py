import unittest

from solution import strict


class MyTestCase(unittest.TestCase):
    def test_correct_types_1(self):
        @strict
        def func(a: int, b: str, c: float):
            return f'{a}, {b}, {c}'

        self.assertEqual(func(10, 'test', 3.14), '10, test, 3.14')

    def test_correct_types_2(self):
        @strict
        def func(a: int, b: str):
            return f"{a}, {b}"

        self.assertEqual(func(b='test', a=10), '10, test')

    def test_incorrect_types(self):
        @strict
        def func(a: int, b: str, c: float):
            return f"{a}, {b}, {c}"

        with self.assertRaises(TypeError):
            func(1, 2, 3.14)


if __name__ == '__main__':
    unittest.main()
