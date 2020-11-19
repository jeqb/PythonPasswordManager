import json

class Settings(dict):
    def __init__(self):
        self.encryption_salt = None
        self.database_file_path = None
    
    def export_settings_to_json(self, file_name):

        output = self.__dict__

        with open(file_name, 'w') as fp:
            json.dump(output, fp)

    def load_json_settings(self, file_name):
        with open(file_name) as json_file:
            data = json.load(json_file)

            self.__dict__ = data