import unittest
from unittest.mock import patch, MagicMock
from models.category import Category


class TestModels(unittest.TestCase):
    def test_category_creation(self):
        category = Category(1, "John Doe")
        self.assertEqual(category.name, "John Doe")


if __name__ == "__main__":
    unittest.main()