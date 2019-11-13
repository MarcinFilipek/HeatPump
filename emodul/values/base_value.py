class BaseValue:
    def __init__(self, data):
        self.data = data.split(',')

    def get_id(self):
        return int(self.data[0])

    def get_id_parent(self):
        return int(self.data[1])

    def get_type(self):
        return int(self.data[2])

    def get_visibility(self):
        return int(self.data[3])
