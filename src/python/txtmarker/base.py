"""
Base highlighter module
"""

# Highlight colors
COLORS = [(0.914, 0.118, 0.388), # Red
          (0.129, 0.588, 0.953), # Blue
          (1.000, 0.757, 0.027), # Yellow
          (0.298, 0.686, 0.314), # Green
          (0.404, 0.227, 0.718), # Purple
          (1.000, 0.596, 0.000), # Orange
          (0.475, 0.333, 0.282)] # Bronze

class Highlighter(object):
    """
    Base class that finds text and adds annotations to files.
    """

    def __init__(self, formatter=None, chunks=-1):
        """
        Creates a new highlighter.

        Args:
            formatter: optional formatter function to clean text, useful to match parsing in calling method
            chunks: chunks queries to allow partial matches, default is disabled
        """

        self.formatter = formatter
        self.chunks = chunks

    def highlight(self, infile, outfile, highlights):
        """
        Finds and highlights text sections in input file. Highlighted file written to output file.

        Args:
            infile: path to read input file
            outfile: path to store annotated file
            highlights: list of (name, text) elements to highlight. Supports text or regular expressions.
        """
