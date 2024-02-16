import yaml

class ConfigLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = None
        self.load_config()

    def load_config(self):
        with open(self.file_path, 'r') as file:
            self.config = yaml.safe_load(file)

    def get_config(self):
        return self.config



