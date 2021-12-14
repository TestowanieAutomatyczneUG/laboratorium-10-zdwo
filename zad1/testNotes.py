import unittest
from notes import Note


class TestNote(unittest.TestCase):
    def setUp(self):
        self.temp = Note('aaa', 2.1)

    def test_get_name(self):
        self.assertEqual(self.temp.get_name(), 'aaa')

    def test_get_note(self):
        self.assertEqual(self.temp.get_note(), 2.1)

    def test_set_name_none(self):
        with self.assertRaises(Exception):
            Note(None, 2.1)

    def test_note_lt_2(self):
        with self.assertRaises(Exception):
            Note('a', 1.13)

    def test_note_gt_6(self):
        with self.assertRaises(Exception):
            Note('a', 7.22)

    def test_note_str(self):
        with self.assertRaises(Exception):
            Note('a', '2')

    def test_note_tup(self):
        with self.assertRaises(Exception):
            Note('a', ())

    def test_note_arr(self):
        with self.assertRaises(Exception):
            Note('a', [])

    def test_note_dict(self):
        with self.assertRaises(Exception):
            Note('a', {})

    def test_note_bool(self):
        with self.assertRaises(Exception):
            Note('a', True)

    def test_name_int(self):
        with self.assertRaises(Exception):
            Note(1, 3.14)

    def test_name_fl(self):
        with self.assertRaises(Exception):
            Note(1.5, 3.14)

    def test_name_tup(self):
        with self.assertRaises(Exception):
            Note((), 3.14)

    def test_name_arr(self):
        with self.assertRaises(Exception):
            Note([], 3.14)

    def test_name_dict(self):
        with self.assertRaises(Exception):
            Note({}, 3.14)

    def test_name_bool(self):
        with self.assertRaises(Exception):
            Note(True, 3.14)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
