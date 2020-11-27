from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from ..AddNoteWindow import AddNoteWindow


def populate_password_table(root_widget):
    # TODO: flesh out method
    pass


def select_password(root_widget):
    # TODO: flesh out method
    pass


def get_passwords(root_widget):
    # TODO: flesh out method.
    pass


def get_password_by_id(root_widget):
    # TODO: flesh out method
    pass


def create_password(root_widget):
    # TODO: flesh out method
    pass


def update_password(root_widget):
    # TODO: flesh out method
    pass


def delete_password(root_widget):
    # TODO: flesh out method
    pass


def populate_note_table(root_widget):
    # TODO: flesh out method
    pass


def select_note(root_widget):
    # TODO: flesh out method
    pass


def get_notes(root_widget):
    # clear table
    for i in reversed(range(root_widget.note_table.rowCount())):
        root_widget.note_table.removeRow(i)

    # call the database api
    notes = root_widget.api.get_notes()

    # populate table
    for note in notes:
        id = str(note.Id)
        content = str(note.Content)
        row_number = root_widget.note_table.rowCount()
        root_widget.note_table.insertRow(row_number)
        root_widget.note_table.setItem(row_number, 0, QTableWidgetItem(id))
        root_widget.note_table.setItem(row_number, 1, QTableWidgetItem(content))


def get_note_by_id(root_widget):
    # TODO: flesh out method
    pass


def create_note(root_widget):
    """
    Creates the AddNoteWindow on the screen. This window
    then handles the adding of the note to the database.
    """
    api = root_widget.api
    root_widget.new_note = AddNoteWindow(api)


def update_note(root_widget):
    # TODO: flesh out method
    pass


def delete_note(root_widget):
    # TODO: flesh out method
    pass