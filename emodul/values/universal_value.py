from emodul.values.base_value import BaseValue


class UniversalValue(BaseValue):
    def __init__(self, data):
        super().__init__(data)

    def status(self):
        return int(self.data[4])

    def id_icon(self):
        return int(self.data[5])

    def id_text1(self):
        return int(self.data[6])

    def value1(self):
        return int(self.data[7])

    def unit1(self):
        return int(self.data[8])

    def widget1(self):
        return self.data[9]

    def id_text2(self):
        return int(self.data[10])

    def value2(self):
        return int(self.data[11])

    def unit2(self):
        return int(self.data[12])

    def widget2(self):
        return self.data[13]

    def statistic(self):
        return int(self.data[14])
