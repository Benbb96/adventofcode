import unittest
from day2 import first, second


class Day2Test(unittest.TestCase):

    """Test case de l'énigme du jour 2."""

    def setUp(self):
        """Initialisation des tests."""
        with open('testInput1.txt', 'r') as f:
            content1 = f.readlines()
        self.content1 = [x.strip() for x in content1]
        with open('testInput2.txt', 'r') as f:
            content2 = f.readlines()
        self.content2 = [x.strip() for x in content2]

    def test_first(self):
        """Test de la première partie du puzzle."""
        elt = first(self.content1, ' ')
        self.assertEqual(elt, 18)

    def test_second(self):
        """Test de la deuxième partie du puzzle."""
        elt = second(self.content2, ' ')
        self.assertEqual(elt, 9)


if __name__ == '__main__':
    unittest.main()
