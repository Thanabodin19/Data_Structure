import json
class My_JSON:
    def __init__(self, file):
        self.js = file

    def write(self, data):
        with open(self.js, 'w') as write_it:
            json.dump(data, write_it, indent = 4)

    def read(self):
        with open(self.js, 'r') as read_it:
            data = json.load(read_it)
        return data

    def write_app(self, new_data):
        with open(self.js, 'r') as read_it:
            data = json.load(read_it)

        data.update(new_data)

        with open(self.js, 'w') as write_it:
            json.dump(data, write_it, indent = 4)

if __name__ == '__main__':
    path_json = 'example.json'

    h = My_JSON(path_json)
    h.write({
        'Class ID': "310-2101",
        'Subject': "Data Structure and Algorithms"

    })

    h.write_app({
        'Teacher': 'Krisada'
    })

    print(h.read())
