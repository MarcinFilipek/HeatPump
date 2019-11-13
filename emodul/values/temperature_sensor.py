from emodul.values.base_value import BaseValue


class TemperatureSensor(BaseValue):
    def __init__(self, data):
        super().__init__(data)

    def is_broken(self):
        return int(self.data[4])

    def id_text(self):
        return int(self.data[5])

    def value(self):
        return int(self.data[6])

    def battery(self):
        return int(self.data[7])

    def signal(self):
        return int(self.data[8])

    def statistic(self):
        return int(self.data[9])
