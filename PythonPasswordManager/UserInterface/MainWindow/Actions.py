import traceback

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from ..AddNoteWindow import AddNoteWindow
from ..AddPasswordWindow import AddPasswordWindow


def select_password(parent_widget):
    parent_widget.edit_password_mode = True
    create_password(parent_widget)


def get_passwords(parent_widget):
    # clear table
    for i in reversed(range(parent_widget.password_table.rowCount())):
        parent_widget.password_table.removeRow(i)

    # call the database api
    password_entries = parent_widget.api.get_passwords()

    populate_password_table(parent_widget, password_entries)


def get_password_by_id(parent_widget):
    # TODO: flesh out method
    pass


def create_password(parent_widget):
    """
    Creates the AddPasswordWindow on the screen. This window
    then handles the adding of the note to the database.
    """
    api = parent_widget.api
    parent_widget.new_password = AddPasswordWindow(parent_widget, api)
    parent_widget.new_password.exec_()


def update_password(parent_widget):
    # TODO: flesh out method
    pass


def delete_password(parent_widget):
    """
    Delete the password entry that is hilighted in the table.
    """
    # check that the password tab is active. if not, ignore.
    IsPasswordTabActive = parent_widget.tabs.currentWidget() == parent_widget.password_tab

    if not IsPasswordTabActive:
        return

    api = parent_widget.api

    password_data = get_selected_password_data(parent_widget)

    if password_data['Id'] == None:
        QMessageBox.information(parent_widget, "Error", "Must select a password to delete")
        return

    message_respnse = QMessageBox.question(parent_widget, "Are you sure?", "Are you sure you want to delete this Password?",
        QMessageBox.No | QMessageBox.Yes, QMessageBox.No)

    if message_respnse == QMessageBox.No:
        return
    else:
        try:
            # delete the password
            api.delete_password(**password_data)

            # update the table in the main window
            parent_widget.tab_changed()
        except Exception as e:
            traceback_string = traceback.format_exc()
            e_message = str(e)

            message = f"An error has occurred.\nMessage is: \
                {e_message}\nTraceback is: {traceback_string}"

            QMessageBox.information(parent_widget, "Error has occurred", message)
            

def get_selected_password_data(parent_widget):
    """
    Look at the note table. See if a row is selected. if yes,
    grab that data and return it. else return None values.
    """
    active_row = parent_widget.password_table.currentRow()

    if active_row >= 0:
        row_values = {
            'Id': parent_widget.password_table.item(active_row, 0).text(),
            'Website': parent_widget.password_table.item(active_row, 1).text(),
            'Username': parent_widget.password_table.item(active_row, 2).text(),
            'Email': parent_widget.password_table.item(active_row, 3).text(),
            'Password': parent_widget.password_table.item(active_row, 4).text(),
            'Category': parent_widget.password_table.item(active_row, 5).text(),
            'Note': parent_widget.password_table.item(active_row, 6).text(),
        }

        return row_values
    else:
        return {
            'Id': None,
            'Website': None,
            'Username': None,
            'Email': None,
            'Password': None,
            'Category': None,
            'Note': None,
        }


def select_note(parent_widget):
    parent_widget.edit_note_mode = True
    create_note(parent_widget)

def get_notes(parent_widget):
    # call the database api
    search_results = parent_widget.api.get_notes()

    populate_note_table(parent_widget, search_results)


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

    populate_note_table(parent_widget, search_results)


def populate_note_table(parent_widget, note_array):
    """
    Gets an array of notes. Populates the note table with that array
    """
    # clear table
    for i in reversed(range(parent_widget.note_table.rowCount())):
        parent_widget.note_table.removeRow(i)

    # populate table
    for note in note_array:
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
    # check that the password tab is active. if not, ignore.
    IsNoteTabActive = parent_widget.tabs.currentWidget() == parent_widget.note_tab

    if not IsNoteTabActive:
        return

    api = parent_widget.api

    note_data = get_selected_note_data(parent_widget)

    if note_data['Id'] == None:
        QMessageBox.information(parent_widget, "Error", "Must select a note to delete")
        return

    message_respnse = QMessageBox.question(parent_widget, "Are you sure?", "Are you sure you want to delete this Note?",
        QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
    
    if message_respnse == QMessageBox.No:
        return
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


def is_password_field_blank(parent_widget):
    """
    Does the same thing as above
    """
    content = parent_widget.password_search_entry.text()
    category = get_radio_category(parent_widget)

    if content == "" and category is None:
        # repopulate the table with no filters
        get_passwords(parent_widget)
    elif content == "" and category is not None:
        # repopulate table with the category filter
        clicked_category_button(parent_widget)
    else:
        # the search field is not empty.
        return


def clear_radio_buttons(parent_widget):
    """
    Clears all readio buttons, and unfilters Password Table -> just refresh
    """
    # https://stackoverflow.com/a/1732385
    radio_buttons = [
        parent_widget.general_radiobutton,
        parent_widget.email_radiobutton,
        parent_widget.financial_radiobutton,
        parent_widget.shopping_radiobutton,
        parent_widget.social_radiobutton
    ]

    for button in radio_buttons:
        button.setAutoExclusive(False)

    for button in radio_buttons:
        button.setChecked(False)

    for button in radio_buttons:
        button.setAutoExclusive(True)

    # repopulate table
    if parent_widget.password_search_entry.text() is None or \
        parent_widget.password_search_entry.text() == '':
        get_passwords(parent_widget)

    else:
        search_passwords_by_website(parent_widget)


def search_passwords_by_website(parent_widget):
    """
    Powers the "Search" button in the Password tab.
    Callout:
        this will search the current table values for data - meaning
        if they have filtered by category, it will search for a website within
        the currently selected category. If no category is selected,
        it will just search by the website
    """
    website_string = parent_widget.password_search_entry.text()

    # can't search by empty string
    if website_string == '': return

    # determine if any radio buttons are selected.
    # this could be written better
    category = get_radio_category(parent_widget)

    # search for the data
    if category is None:
        password_entries = parent_widget.api.search_password_by_website(website_string)
    else:
        password_entries = parent_widget.api.search_password_by_website_and_category(
            website_string, category)

    populate_password_table(parent_widget, password_entries)


def clicked_category_button(parent_widget):
    """
    If a password category gets clicked, figure out which one,
    see if there's text in the website search. Then apply the necessary
    filters.
    """
    # grab search data
    category = get_radio_category(parent_widget)
    website_string = parent_widget.password_search_entry.text()

    if website_string is None or website_string == '':
        # search by category only.
        password_entries = parent_widget.api.search_password_by_category(category)
    else:
        # search by website and category
        password_entries = parent_widget.api.search_password_by_website_and_category(
            website_string, category)

    populate_password_table(parent_widget, password_entries)


def get_radio_category(parent_widget):
    """
    Figure out which radio button on the Password
    tab is checked.
    """
    if parent_widget.general_radiobutton.isChecked():
        return 'General'
    elif parent_widget.email_radiobutton.isChecked():
        return 'Email'
    elif parent_widget.financial_radiobutton.isChecked():
        return 'Financial'
    elif parent_widget.shopping_radiobutton.isChecked():
        return 'Shopping'
    elif parent_widget.social_radiobutton.isChecked():
        return 'Social'
    else:
        return None


def populate_password_table(parent_widget, password_entries):
    """
    Given the results from the database, populate the password
    table with it.
    """

    # clear table
    for i in reversed(range(parent_widget.password_table.rowCount())):
        parent_widget.password_table.removeRow(i)

    # populate table
    for entry in password_entries:
        # get individual column values
        id = str(entry.Id)
        website = str(entry.Website)
        username = str(entry.Username)
        email = str(entry.Email)
        password = str(entry.Password)
        category = str(entry.Category)
        note = str(entry.Note)

        row_number = parent_widget.password_table.rowCount()
        
        # add the data to the row
        parent_widget.password_table.insertRow(row_number)
        parent_widget.password_table.setItem(row_number, 0, QTableWidgetItem(id))
        parent_widget.password_table.setItem(row_number, 1, QTableWidgetItem(website))
        parent_widget.password_table.setItem(row_number, 2, QTableWidgetItem(username))
        parent_widget.password_table.setItem(row_number, 3, QTableWidgetItem(email))
        parent_widget.password_table.setItem(row_number, 4, QTableWidgetItem(password))
        parent_widget.password_table.setItem(row_number, 5, QTableWidgetItem(category))
        parent_widget.password_table.setItem(row_number, 6, QTableWidgetItem(note))