from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from ..AddNoteWindow import AddNoteWindow
from ..AddPasswordWindow import AddPasswordWindow


def populate_password_table(parent_widget):
    # TODO: flesh out method
    pass


def select_password(parent_widget):
    # TODO: flesh out method
    pass


def get_passwords(parent_widget):
    # TODO: flesh out method.
    pass


def get_password_by_id(parent_widget):
    # TODO: flesh out method
    pass


def create_password(parent_widget):
    """
    Creates the AddPasswordWindow on the screen. This window
    then handles the adding of the note to the database.
    """
    api = parent_widget.api
    parent_widget.new_note = AddPasswordWindow(api)


def update_password(parent_widget):
    # TODO: flesh out method
    pass


def delete_password(parent_widget):
    # TODO: flesh out method
    pass


def populate_note_table(parent_widget):
    # TODO: flesh out method
    pass


def select_note(parent_widget):
    active_row = parent_widget.note_table.currentRow()
    row_values = {
        'Id': parent_widget.note_table.item(active_row, 0).text(),
        'Content': parent_widget.note_table.item(active_row, 1).text(),
    }

    print('active_row ', active_row)
    print(row_values)


def get_notes(parent_widget):
    # clear table
    for i in reversed(range(parent_widget.note_table.rowCount())):
        parent_widget.note_table.removeRow(i)

    # call the database api
    notes = parent_widget.api.get_notes()

    # populate table
    for note in notes:
        id = str(note.Id)
        content = str(note.Content)
        row_number = parent_widget.note_table.rowCount()
        parent_widget.note_table.insertRow(row_number)
        parent_widget.note_table.setItem(row_number, 0, QTableWidgetItem(id))
        parent_widget.note_table.setItem(row_number, 1, QTableWidgetItem(content))


def get_note_by_id(parent_widget):
    # TODO: flesh out method
    pass


def create_note(parent_widget):
    """
    Creates the AddNoteWindow on the screen. This window
    then handles the adding of the note to the database.
    """
    api = parent_widget.api
    parent_widget.new_note = AddNoteWindow(parent_widget, api)
    parent_widget.new_note.exec_()


def update_note(parent_widget):
    # TODO: flesh out method
    pass


def delete_note(parent_widget):
    # TODO: flesh out method
    pass