class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_Data(self):
        return self.data

    def get_Next(self):
        return self.next

    def set_Data(self, new_data):
        self.data = new_data

    def set_Next(self, new_next):
        self.next = new_next