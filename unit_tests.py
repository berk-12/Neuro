import unittest
from blueprint import getCoordinates


class TestBlueprint(unittest.TestCase):
    def testGetCoordinates(self):
        with self.assertRaises(ValueError):
            getCoordinates("0")
            getCoordinates("x")