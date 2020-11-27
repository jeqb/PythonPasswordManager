from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import traceback

def cancel(parent_widget):
    """
    Closes the window
    """
    parent_widget.close()

def add_note(parent_widget):
    try:
        # create the note in the database
        api = parent_widget.api
        note_content = parent_widget.note_entry.text()
        parent_widget.api.add_note(note_content)

        # update the table in the main window
        parent_widget.parent_widget.tab_changed()
        
        # close the AddNoteWindow
        parent_widget.close()
    except Exception as e:
        traceback_string = traceback.format_exc()
        e_message = str(e)

        message = f"An error has occurred.\nMessage is: \
            {e_message}\nTraceback is: {traceback_string}"

        QMessageBox.information(parent_widget, "Error has occurred", message)