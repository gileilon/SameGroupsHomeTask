import unittest
from sameGroupsFinder import find_same_groups


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        file_path = r'Groups.txt'
        same_groups = find_same_groups(file_path)
        vals = set([tuple(ls) for ls in same_groups.values()])
        expected = {('A10',), ('A5', 'A32'), ('A7',), ('A1', 'A2', 'A6')}  # this is set
        self.assertEqual(vals, expected)

    def test_2(self):
        file_path = r'Groups_tests\Groups_2.txt'
        same_groups = find_same_groups(file_path)
        vals = set([tuple(ls) for ls in same_groups.values()])
        expected = {('A1',), ('A2',), ('A3',), ('A4',)}  # this is set
        self.assertEqual(vals, expected)

    def test_3(self):
        file_path = r'Groups_tests\Groups_3.txt'
        same_groups = find_same_groups(file_path)
        vals = set([tuple(ls) for ls in same_groups.values()])
        expected = {('A1',), ('A2',), ('A3',), ('A4',)}  # this is set
        self.assertEqual(vals, expected)

    def test_4(self):
        file_path = r'Groups_tests\Groups_4.txt'
        same_groups = find_same_groups(file_path)
        vals = set([tuple(ls) for ls in same_groups.values()])
        expected = {('A1', 'A2',), ('A3', 'A4',)}  # this is set
        self.assertEqual(vals, expected)

    def test_5(self):
        file_path = r'Groups_tests\Groups_5.txt'
        same_groups = find_same_groups(file_path)
        vals = set([tuple(ls) for ls in same_groups.values()])
        expected = set()  # this is set
        self.assertEqual(vals, expected)

    def test_6(self):
        file_path = r'Groups_tests\Groups_6.txt'
        same_groups = find_same_groups(file_path)
        vals = set([tuple(ls) for ls in same_groups.values()])
        expected = {('A1', 'A2', 'A3', 'A4', 'A5', 'A6',)}  # this is set
        self.assertEqual(vals, expected)

    def test_7(self):
        file_path = r'Groups_tests\Groups_7.txt'
        same_groups = find_same_groups(file_path)
        vals = set([tuple(ls) for ls in same_groups.values()])
        expected = {('A1', 'A2',), ('A4', 'A5',), ('A3',), ('A6',)}  # this is set
        self.assertEqual(vals, expected)

if __name__ == '__main__':
    unittest.main()
