"""
PDF module tests
"""

import re
import os
import unittest

# pylint: disable=E0401
from txtmarker.factory import Factory

class TestPDF(unittest.TestCase):
    """
    PDF tests
    """

    def path(self, name):
        """
        Generates a full path

        Args:
            name: file name

        Returns:
            full path to file
        """

        return os.path.join("/tmp/txtmarker/", name)

    def testHighlights(self):
        """
        Tests basic highlighting
        """

        highlighter = Factory.create("pdf")

        highlights = [
            ("Basic", "Hashing is a key part"),
            ("Multi-line", "Hashes are used to secure. Hashes can be deterministic or non-deterministic. Hashes can be significantly " +
             "different with small changes to data or very similar."),
            ("Regex", "This article.*Python"),
            ("Regex Multi-line", "The above(.|\n)+is deterministic"),
            (None, "Python provides the built-in .hash()")]

        annotations = highlighter.highlight(self.path("hash.pdf"), self.path("out.pdf"), highlights)

        # Check annotations created
        self.assertEqual(len(annotations), 5)

        # Check output file exists
        self.assertTrue(os.path.exists(self.path("out.pdf")))

    def testOverlaps(self):
        """
        Test overlapping ranges
        """

        highlighter = Factory.create("pdf")

        # Create duplicate highlights to test overlapping range
        highlights = [("Overlaps", "This article will explore various methods")] * 4

        annotations = highlighter.highlight(self.path("embeddings.pdf"), self.path("out.pdf"), highlights)

        # Check annotations created
        self.assertEqual(len(annotations), 4)

    def testFormatter(self):
        """
        Tests highlighter with formatting and chunks
        """

        highlighter = Factory.create("pdf", lambda x: re.sub(r"[^A-Za-z0-9]", "", x), 4)

        highlights = [("End newline", "txtai builds an AI-powered index over sections of text\n"),
                      ("Long line", "NeuML has years of relevant experience in building data strategies for both small and large organizations. " +
                       "With the right data, valuable insights can be gained by capitalizing on modern advances in machine learning. ")]

        annotations = highlighter.highlight(self.path("neuml.pdf"), self.path("out.pdf"), highlights)

        # Check annotations created
        self.assertEqual(len(annotations), 2)

    def testColumns(self):
        """
        Test multiple columns
        """

        highlighter = Factory.create("pdf")

        highlights = [("Multi-column", "enable machine-learning(.|\n)+specific domains")]

        annotations = highlighter.highlight(self.path("neuml.pdf"), self.path("out2.pdf"), highlights)

        # Check annotations created
        self.assertEqual(len(annotations), 2)

    def testText(self):
        """
        Tests line concatenation on hyphen.
        """

        highlighter = Factory.create("pdf")

        elements = [(x, x) for x in ["This is a hyph-\n", "en test\n"]]

        self.assertEqual(highlighter.text(elements), "This is a\nhyphen test\n")
