import json
import os
from pathlib import Path

class Settings(dict):
    """
    This class is to be instantiated on startup. It should correspond
    to a password_manager_settings.json file which contains all the needed
    properties to run the app.

    if the password_manager_settings.json file does not exist, it will get
    auto generated.
    """

    FILE_NAME = 'password_manager_settings.json'

    def __init__(self):
        # settings that live in password_manager_settings.json
        self.encryption_salt = None
        self.database_file_path = None
        self.valid = False

        # construct settings file path
        cwd = os.getcwd()
        cwd = Path(cwd)
        file_path = cwd / self.FILE_NAME

        # try to load the settings
        try:
            self.load_json_settings(file_path)
            self.is_valid()
        except FileNotFoundError:
            # create the file if it doesn't exist
            self.export_settings_to_json(file_path)
    

    def export_settings_to_json(self, file_path):
        """
        export settings to password_manager_settings.json
        """
        output = self.__dict__

        with open(file_path, 'w') as fp:
            json.dump(output, fp)


    def load_json_settings(self, file_path):
        """
        load password_manager_settings.json
        """
        with open(file_path) as json_file:
            data = json.load(json_file)

            self.__dict__ = data


    def is_valid(self):
        """
        a "valid" settings object has a salt and a database path.
        otherwise it's not.
        """
        for key, value in self.__dict__.items():
            if value is None:
                self.valid = False

                return self.valid

        self.valid = True

        return self.valid