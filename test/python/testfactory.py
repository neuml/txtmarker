"""
Factory module tests
"""

import unittest

# pylint: disable=E0401
from txtmarker.factory import Factory


class TestFactory(unittest.TestCase):
    """
    Factory tests
    """

    def testCreate(self):
        """
        Tests factory create method.
        """

        self.assertIsNotNone(Factory.create("pdf"))
        self.assertIsNone(Factory.create("abc"))
