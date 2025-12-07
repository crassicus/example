import unittest
from . import add


class TestFunctions(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_add_success(self):
        x, y = (18, 19)
        result = add(x, y)
        self.assertEqual(result, 37)

    def test_add_fail(self):
        x, y = (18, 19)
        result = add(x, y)
        self.assertNotEqual(result, 30)
