from emodul.values.base_value import BaseValue


class RelayValue(BaseValue):
    def __init__(self, data):
        super().__init__(data)

    def value(self):
        return int(self.data[4])

    def id_text(self):
        return int(self.data[5])

    def id_icon(self):
        return  int(self.data[6])
