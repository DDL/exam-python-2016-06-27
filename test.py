from third import count_letter_in_string
import unittest

class TestCount_letter_in_string(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(count_letter_in_string('', 'a'), 0)
    def test_not_string_int(self):
        self.assertEqual(count_letter_in_string(1, 'a'), 0)
    def test_not_string_float(self):
        self.assertEqual(count_letter_in_string(1.1, 'a'), 0)
    def test_not_string_list(self):
        self.assertEqual(count_letter_in_string([0,1,2,3,4,5,6,7,8,9], 'a'), 0)
    def test_not_string_dict(self):
        self.assertEqual(count_letter_in_string({0,1,2,3,4,5,6,7,8,9}, 'a'), 0)
    def test_not_string_tuple(self):
        self.assertEqual(count_letter_in_string((0,1,2,3,4,5,6,7,8,9), 'a'), 0)
    def test_empty_letter(self):
        self.assertEqual(count_letter_in_string('Hello', ''), 0)
    def test_not_letter_int(self):
        self.assertEqual(count_letter_in_string('Hello', 1), 0)
    def test_not_letter_float(self):
        self.assertEqual(count_letter_in_string('a', 1.1), 0)
    def test_not_letter_list(self):
        self.assertEqual(count_letter_in_string('Hello', [0,1,2,3,4,5,6,7,8,9]), 0)
    def test_not_letter_dict(self):
        self.assertEqual(count_letter_in_string('Hello', {0,1,2,3,4,5,6,7,8,9}), 0)
    def test_not_letter_tuple(self):
        self.assertEqual(count_letter_in_string('Hello', (0,1,2,3,4,5,6,7,8,9)), 0)
    def test_not_letter_not_one_letter(self):
        self.assertEqual(count_letter_in_string('Hello', 'aa'), 0)
    def test_all_letter_same(self):
        self.assertEqual(count_letter_in_string('aaaaaa', 'a'), 6)
    def test_all_same_upper_letter(self):
        self.assertEqual(count_letter_in_string('AAAAAA', 'a'), 0)
    def test_all_letter_same_upper_and_lower(self):
        self.assertEqual(count_letter_in_string('AaAaAa', 'a'), 3)


if __name__ == '__main__':
    unittest.main()
