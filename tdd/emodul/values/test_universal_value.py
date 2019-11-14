import unittest
from emodul.values.universal_value import UniversalValue


class UniversalValueTest(unittest.TestCase):
    def setUp(self):
        data = '1006,5000,6,1,0,102,0,0,-1,0{0;0;0;0;0},866,0,8,1{0;0;0;0;0},1'
        self.universal_value = UniversalValue(data)

    def test_id(self):
        id = self.universal_value.get_id()
        self.assertEqual(1006, id)

    def test_id_parent(self):
        id_parent = self.universal_value.get_id_parent()
        self.assertEqual(5000, id_parent)

    def test_type(self):
        type = self.universal_value.get_type()
        self.assertEqual(6, type)

    def test_visiable(self):
        vis = self.universal_value.get_visibility()
        self.assertEqual(1, vis)

    def test_status(self):
        status = self.universal_value.status()
        self.assertEqual(0, status)

    def test_icon(self):
        icon = self.universal_value.id_icon()
        self.assertEqual(102, icon)

    def test_id_text1(self):
        id_text1 = self.universal_value.id_text1()
        self.assertEqual(0, id_text1)

    def test_value1(self):
        value1 = self.universal_value.value1()
        self.assertEqual(0, value1)

    def test_unit1(self):
        unit1 = self.universal_value.unit1()
        self.assertEqual(-1, unit1)

    def test_widget1(self):
        widget1 = self.universal_value.widget1()
        self.assertEqual('0{0;0;0;0;0}', widget1)

    def test_id_text2(self):
        id_text2 = self.universal_value.id_text2()
        self.assertEqual(866, id_text2)

    def test_value2(self):
        value2 = self.universal_value.value2()
        self.assertEqual(0, value2)

    def test_unit2(self):
        unit2 = self.universal_value.unit2()
        self.assertEqual(8, unit2)

    def test_widget2(self):
        widget2 = self.universal_value.widget2()
        self.assertEqual('1{0;0;0;0;0}', widget2)

    def test_statistic(self):
        statistic = self.universal_value.statistic()
        self.assertEqual(1, statistic)
