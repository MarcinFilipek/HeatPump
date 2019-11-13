import unittest
from emodul.values.base_value import BaseValue


class BaseValueTest(unittest.TestCase):
    def setUp(self):
        data = '1657,5004,1,1,1,3834,68,-1,-1,1'
        self.base_value = BaseValue(data)

    def test_id(self):
        id = self.base_value.get_id()
        self.assertEqual(1657, id)

    def test_id_parent(self):
        id_parent = self.base_value.get_id_parent()
        self.assertEqual(5004, id_parent)

    def test_type(self):
        type = self.base_value.get_type()
        self.assertEqual(1, type)

    def test_visibility(self):
        vis = self.base_value.get_visibility()
        self.assertEqual(1, vis)
