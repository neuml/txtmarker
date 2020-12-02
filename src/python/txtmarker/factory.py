"""
Factory module
"""

from . import pdf

class Factory(object):
    """
    Creates document highlighters.
    """

    @staticmethod
    def create(extension, formatter=None, chunk=-1):
        """
        Creates a new highlighter.

        Args:
            extension: file format type
            formatter: optional formatter function to clean text, useful to match parsing in calling method
            chunks: chunks queries to allow partial matches, default is disabled

        Returns:
            Highlighter instance
        """

        if extension == "pdf":
            return pdf.Highlighter(formatter, chunk)

        return None
