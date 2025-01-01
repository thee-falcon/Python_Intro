""" This module provides functions to convert a PDF to Text. """


class Converter:
    """A simple converter for convering PDFs to text.
    """

    def convert(self, path):
        """
        Convert the given PDF to text.
        
        Parameters:
        path (str): The path to a PDF file.
        
        Returns:
        str: The content of the PDF file as text.
        """
        print(f"Convert this pdf from the path{path}")
