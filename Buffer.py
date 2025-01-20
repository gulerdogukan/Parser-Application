class File:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            file = open(self.file_name, 'r', encoding='utf-8')
        except OSError:
            print("Something Wrong, Could Not Access The File!!!")

    def read_from_file(self):
        file = open(self.file_name, 'r', encoding='utf-8')
        inputs_token = file.readline()
        return inputs_token
