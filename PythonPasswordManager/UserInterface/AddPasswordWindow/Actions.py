from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

import traceback

def cancel(parent_widget):
    """
    Closes the window
    """
    parent_widget.parent_widget.edit_password_mode = False
    parent_widget.close()


def add_password(parent_widget):
    """
    Get the password data from the AddPasswordWindow,
    then add it to the database. This can also update
    a password.
    """
    # assemble the data object
    password_data = {
        'Website': parent_widget.website_entry.text(),
        'Username': parent_widget.username_entry.text(),
        'Email': parent_widget.email_entry.text(),
        'Password': parent_widget.password_entry.text(),
        'Category': parent_widget.category_entry.text(),
        'Note': parent_widget.note_entry.text()
    }

    # check the validity of the data
    try:
        validate_password_data(password_data)
    except Exception as e:
        message = str(e)
        QMessageBox.information(parent_widget, "Missing Info", message)
        return

    # send it off to the database
    try:
        if parent_widget.parent_widget.edit_password_mode:
            # update an existing password
            password_data['Id'] = parent_widget.active_password_id
            parent_widget.api.update_password(**password_data)
        else:
            # create password entry in database
            parent_widget.api.add_password(**password_data)

        # update the table in the main window
        parent_widget.parent_widget.tab_changed()

        # make sure not in edit mode
        parent_widget.parent_widget.edit_password_mode = False

        # close the AddPasswordWindow
        parent_widget.close()
    except Exception as e:
        traceback_string = traceback.format_exc()
        e_message = str(e)

        message = f"An error has occurred.\nMessage is: \
            {e_message}\nTraceback is: {traceback_string}"

        QMessageBox.information(parent_widget, "Error has occurred", message)


def validate_password_data(password_dict):
    """
    Check to ensure that all the required data is present in order
    to create a password entry
    """

    if password_dict['Password'] == '':
        raise Exception('Password is required.')
    elif password_dict['Email'] == '' and password_dict['Username'] == '':
        raise Exception('Email or Username is required.')
    elif password_dict['Category'] == '':
        raise Exception("Category is required.")


def get_selected_password_data(parent_widget):
    """
    Look at the password table. See if a row is selected. if yes,
    grab that data and return it. else return None values.
    """
    main_window = parent_widget.parent_widget

    active_row = main_window.password_table.currentRow()

    if active_row >= 0:
        row_values = {
            'Id': main_window.password_table.item(active_row, 0).text(),
            'Website': main_window.password_table.item(active_row, 1).text(),
            'Username': main_window.password_table.item(active_row, 2).text(),
            'Email': main_window.password_table.item(active_row, 3).text(),
            'Password': main_window.password_table.item(active_row, 4).text(),
            'Category': main_window.password_table.item(active_row, 5).text(),
            'Note': main_window.password_table.item(active_row, 6).text(),
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


def populate_password_fields(parent_widget, data):
    """
    Given a data dictionary, populate the fields on the AddPasswordWindow form
    with the data.
    """

    id = data['Id']
    website = data['Website']
    username = data['Username']
    email = data['Email']
    password = data['Password']
    category = data['Category']
    note = data['Note']

    parent_widget.website_entry.setText(website)
    parent_widget.username_entry.setText(username)
    parent_widget.email_entry.setText(email)
    parent_widget.password_entry.setText(password)
    parent_widget.category_entry.setText(category)
    parent_widget.note_entry.setText(note)

    # need to store this somewhere for use with the db
    parent_widget.active_password_id = id