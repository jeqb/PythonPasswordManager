from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import traceback

def cancel(parent_widget):
    """
    Closes the window
    """
    parent_widget.parent_widget.edit_note_mode = False
    parent_widget.close()

def add_note(parent_widget):
    note_content = parent_widget.note_entry.text()

    if note_content == "":
        message = "There is no Note content to store"
        QMessageBox.information(parent_widget, "Missing Info", message)
    else:
        try:
            # create the note in the database
            api = parent_widget.api
            parent_widget.api.add_note(note_content)

            # update the table in the main window
            parent_widget.parent_widget.tab_changed()
            
            # make sure not in edit mode (paranoia)
            parent_widget.parent_widget.edit_note_mode = False

            # close the AddNoteWindow
            parent_widget.close()
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
    main_window = parent_widget.parent_widget

    active_row = main_window.note_table.currentRow()

    if active_row >= 0:
        row_values = {
            'Id': main_window.note_table.item(active_row, 0).text(),
            'Content': main_window.note_table.item(active_row, 1).text(),
        }

        return row_values
    else:
        return {
            'Id': None,
            'Content': None
        }


def populate_note_fields(parent_widget, data):
    """
    Given a data dictionary, populate the fields on the AddNoteWindow form
    with the data.
    """

    content = data['Content']

    parent_widget.note_entry.setText(content)