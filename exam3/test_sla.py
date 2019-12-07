import unittest
from sla import show_sla


class TestUM(unittest.TestCase):
    def setUp(self):
        pass
    def test_sla99_9(self):
        self.assertEqual( show_sla(99.9), "8h 45.0m 57.0s")
    def test_sla99_8(self):
        self.assertEqual( show_sla(99.8), "17h 31.0m 55.0s")
    def test_sla99_5(self):
        self.assertEqual( show_sla(99.5), "43h 49.0m 48.0s")    
if __name__ == '__main__':
    unittest.main()