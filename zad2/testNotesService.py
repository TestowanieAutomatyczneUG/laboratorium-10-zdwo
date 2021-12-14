import unittest
from unittest.mock import *
from notesService import NotesService
from notesStorage import NotesStorage
from zad1.notes import Note


class TestNotesService(unittest.TestCase):

    def setUp(self):
        self.service = NotesService()

    @patch.object(NotesStorage, 'add')
    def test_add(self, mock_method):
        note = Note('aaa', 3.11)
        mock_method.return_value = 'ok'
        self.assertEqual(self.service.add(note), 'ok')

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_avgOf(self, mock_method):
        mock_method.return_value = [2.3, 4.4, 2.21]
        self.assertAlmostEqual(self.service.averageOf('a'), 2.97)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_avgOf_empty(self, mock_method):
        mock_method.return_value = []
        self.assertEqual(self.service.averageOf('b'), 0)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_avgOf_one(self, mock_method):
        mock_method.return_value = [5.281]
        self.assertAlmostEqual(self.service.averageOf('c'), 5.281)

    @patch.object(NotesStorage, 'clear')
    def test_clear(self, mock_method):
        mock_method.return_value = 'ok'
        self.assertEqual(self.service.clear(), 'ok')



