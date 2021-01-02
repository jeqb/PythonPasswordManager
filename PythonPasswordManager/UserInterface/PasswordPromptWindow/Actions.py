def submit(parent_widget):
    main_window = parent_widget.parent_widget
    password = parent_widget.password_field.text()
    main_window.password_submission = password

    parent_widget.close()


def cancel(parent_widget):
    parent_widget.close()