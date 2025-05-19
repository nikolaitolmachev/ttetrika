import unittest

from solution import appearance


class MyTestCase(unittest.TestCase):
    def test_full_overlap(self):
        intervals = {
            'lesson': [0, 200],
            'pupil': [100, 150],
            'tutor': [100, 150]
        }
        self.assertEqual(appearance(intervals), 50)

    def test_no_overlap(self):
        intervals = {
            'lesson': [0, 2000],
            'pupil': [0, 1000],
            'tutor': [1000, 2000]
        }
        self.assertEqual(appearance(intervals), 0)

    def test_basic_case(self):
        intervals = {
            'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        }
        self.assertEqual(appearance(intervals), 3117)


if __name__ == '__main__':
    unittest.main()
