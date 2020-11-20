import json

class Settings(dict):
    def __init__(self):
        self.encryption_salt = None
        self.database_file_path = None
        self.valid = False
    

    def export_settings_to_json(self, file_name):
        """
        export settings to password_manager_settings.json
        """
        output = self.__dict__

        with open(file_name, 'w') as fp:
            json.dump(output, fp)


    def load_json_settings(self, file_name):
        """
        load password_manager_settings.json
        """
        with open(file_name) as json_file:
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