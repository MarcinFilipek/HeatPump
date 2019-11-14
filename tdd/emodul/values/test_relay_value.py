import unittest
from emodul.values.relay_value import RelayValue


class RelayValueTest(unittest.TestCase):
    def setUp(self):
        data = '1007,5000,11,1,0,1383,101'
        self.relay_value = RelayValue(data)

    def test_id(self):
        id = self.relay_value.get_id()
        self.assertEqual(1007, id)

    def test_id_parent(self):
        id_parent = self.relay_value.get_id_parent()
        self.assertEqual(5000, id_parent)

    def test_type(self):
        type = self.relay_value.get_type()
        self.assertEqual(11, type)

    def test_visiable(self):
        vis = self.relay_value.get_visibility()
        self.assertEqual(1, vis)

    def test_value(self):
        value = self.relay_value.value()
        self.assertEqual(0, value)

    def test_id_text(self):
        id_text = self.relay_value.id_text()
        self.assertEqual(1383, id_text)

    def test_id_icon(self):
        id_icon = self.relay_value.id_icon()
        self.assertEqual(101, id_icon)
