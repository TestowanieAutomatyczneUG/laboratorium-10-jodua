from unittest import TestCase
from unittest.mock import patch
from assertpy import assert_that
from src.Note import Note
from src.NotesService import NotesService
from src.NotesStorage import NotesStorage


class TestNotesService(TestCase):
    def setUp(self) -> None:
        self.ns = NotesService()

    @patch.object(NotesStorage, 'add')
    def test_add_note_is_instance(self, mock_ns_add) -> None:
        note = Note("Note1", 3.5)
        mock_ns_add.return_value = note
        assert_that(self.ns.add(note)).is_instance_of(Note)

    @patch.object(NotesStorage, 'add')
    def test_add_note_is_equal_object(self, mock_ns_add) -> None:
        note = Note("Note1", 2.5)
        mock_ns_add.return_value = note
        assert_that(self.ns.add(note)).is_equal_to(note)

    @patch.object(NotesStorage, 'clear')
    def test_clear_notes(self, mock_ns_clear) -> None:
        mock_ns_clear.return_value = True
        assert_that(self.ns.clear()).is_true

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_average_of(self, mock_ns_getAllNotesOf) -> None:
        mock_ns_getAllNotesOf.return_value = [
            Note("sth", 3.0), Note("sth", 4.0), Note("sth", 2.0)]
        assert_that(self.ns.averageOf('sth')).is_equal_to(3.0)

    @patch.object(NotesStorage, 'getAllNotesOf')
    def test_clear_average_of_empty(self, mock_ns_getAllNotesOf) -> None:
        mock_ns_getAllNotesOf.return_value = []
        assert_that(self.ns.averageOf('sth')).is_equal_to(0)
