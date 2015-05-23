import unittest


class SimpleTests(unittest.TestCase):
    def test_it(self):
        result = "".join("a b c")
        self.assertEqual(result, "a b c")


# $ python -m unittest simpletest
