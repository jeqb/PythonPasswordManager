import traceback

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
    parent_widget.edit_note_mode = True
    create_note(parent_widget)

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


def search_note_by_content(parent_widget):
    """
    Powers the Search button on the right side of the Notes Tab.
    Given a text entered in the note_search_entry, search the Content
    column of the note table using a wildcard.

    Callout: This may need to be async for performance in the future.
    """
    # do the wildcard search
    api = parent_widget.api
    search_text = parent_widget.note_search_entry.text()
    search_results = api.search_note_by_content(search_text)

    # clear table
    for i in reversed(range(parent_widget.note_table.rowCount())):
        parent_widget.note_table.removeRow(i)

    # populate table
    for note in search_results:
        id = str(note.Id)
        content = str(note.Content)
        row_number = parent_widget.note_table.rowCount()
        parent_widget.note_table.insertRow(row_number)
        parent_widget.note_table.setItem(row_number, 0, QTableWidgetItem(id))
        parent_widget.note_table.setItem(row_number, 1, QTableWidgetItem(content))


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
    """
    Delete the note entry that is hilighted in the table.
    """
    api = parent_widget.api

    note_data = get_selected_note_data(parent_widget)

    if note_data['Id'] == None:
        QMessageBox.information(parent_widget, "Error", "Must select a note to delete")
    else:
        try:
            # delete the note
            api.delete_note(**note_data)

            # update the table in the main window
            parent_widget.tab_changed()
        except Exception as e:
            traceback_string = traceback.format_exc()
            e_message = str(e)

            message = f"An error has occurred.\nMessage is: \
                {e_message}\nTraceback is: {traceback_string}"

            QMessageBox.information(parent_widget, "Error has occurred", message)


def get_selected_note_data(parent_widget):
    """
    Look at the note table. See if a row is selected. if yes,
    grab that data and return it. else return None values.
    """
    active_row = parent_widget.note_table.currentRow()

    if active_row >= 0:
        row_values = {
            'Id': parent_widget.note_table.item(active_row, 0).text(),
            'Content': parent_widget.note_table.item(active_row, 1).text(),
        }

        return row_values
    else:
        return {
            'Id': None,
            'Content': None
        }


def check_if_blank(parent_widget):
    """
    This checks if the note_search_entry object is blank when
    the text in it changes. If it is indeed blank, that means nothing
    is being searched for and therefore, the table needs to be repopulated in
    case they searched for something and it reduced the table results.
    """
    content = parent_widget.note_search_entry.text()
    
    if content == "":
        # the field has been emptied, therefore, repopulate the table.
        get_notes(parent_widget)