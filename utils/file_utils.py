

class FileUtil:
    def __init__(self, path):
        self.path = path

    def get_file_as_str(self):
        try:
            with open(self.path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            print("File {} not found".format(self.path))
            raise FileNotFoundError

    def get_file_as_lines(self):
        try:
            with open(self.path, 'r') as file:
                return file.readlines()
        except FileNotFoundError:
            print("File {} not found".format(self.path))
            raise FileNotFoundError