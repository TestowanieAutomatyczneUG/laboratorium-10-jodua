from Note import Note
from unittest import TestCase
from assertpy import assert_that


class TestNote(TestCase):
    def test_create_note_correct_data_instance(self):
        note = Note("Note Name", 5.0)
        assert_that(note).is_instance_of(Note)

    def test_create_note_correct_data_name_property(self):
        note = Note("Note1", 3.14)
        assert_that(note.name).is_equal_to("Note1")

    def test_create_note_correct_data_note_property(self):
        note = Note("Note1", 2.13)
        assert_that(note.note).is_close_to(2.13, 0.001)

    def test_create_note_invalid_name_type(self):
        assert_that(Note).raises(TypeError).when_called_with(3.45, 4.0)

    def test_create_note_invalid_note_type(self):
        assert_that(Note).raises(TypeError).when_called_with("Note2", "4.0")

    def test_create_note_invalid_types(self):
        assert_that(Note).raises(TypeError).when_called_with(1, 1)

    def test_create_note_empty_name(self):
        assert_that(Note).raises(ValueError).when_called_with("", 4.0)

    def test_create_note_value_less_than_2(self):
        assert_that(Note).raises(
            ValueError).when_called_with("Test Note", 0.12)

    def test_create_note_value_greater_than_6(self):
        assert_that(Note).raises(ValueError).when_called_with(
            "Test Note", 99999999999999999999999.1)
