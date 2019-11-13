import unittest
from emodul.values.temperature_sensor import TemperatureSensor


class BaseTemperatureSensor(unittest.TestCase):
    def setUp(self):
        data = '1657,5004,1,1,1,3834,68,-1,-1,1'
        self.temp_sensor = TemperatureSensor(data)

    def test_is_broken(self):
        is_broken = self.temp_sensor.is_broken()
        self.assertEqual(1, is_broken)

    def test_id_text(self):
        id_text = self.temp_sensor.id_text()
        self.assertEqual(3834, id_text)

    def test_value(self):
        value = self.temp_sensor.value()
        self.assertEqual(68, value)

    def test_battery(self):
        battery = self.temp_sensor.battery()
        self.assertEqual(-1, battery)

    def test_signal(self):
        signal = self.temp_sensor.signal()
        self.assertEqual(-1, signal)

    def test_statistic(self):
        statistic = self.temp_sensor.statistic()
        self.assertEqual(1, statistic)
