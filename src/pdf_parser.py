# 🕵️‍♂️ PDFParser: The Document Whisperer 📚🔍
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This class is like a master detective, uncovering the hidden secrets
# within the enigmatic world of PDFs.

import fitz  # 📚 Our trusty magnifying glass for PDF investigation
from typing import List, Dict, Any  # 🧰 Our detective's toolkit for type hinting


class PDFParser:
    """
    A sophisticated tool for extracting intelligence from PDF documents.
    Think of it as a high-tech scanner that can peel back layers of a document,
    revealing text, images, and the very architecture of the file itself.
    """

    def __init__(self, pdf_path: str):
        """
        Initializes our document analyzer with the path to a PDF file.

        :param pdf_path: The location of the PDF file we're about to investigate.
        """
        self.doc = fitz.open(pdf_path)  # 📂 Opening our case file

    def extract_text(self, page_num: int) -> str:
        """
        Extracts text from a specific page, like a skilled linguist decoding
        an ancient manuscript.

        :param page_num: The page number to extract text from (0-indexed).
        :return: A string containing all the text from the specified page.
        """
        page = self.doc[page_num]  # 📄 Focusing on our target page
        return page.get_text()  # 🔍 Unveiling the hidden message

    def extract_images(self, page_num: int) -> List[Dict[str, Any]]:
        """
        Retrieves all images from a page, as if using X-ray vision to see
        through the document's layers.

        :param page_num: The page number to extract images from (0-indexed).
        :return: A list of dictionaries, each containing image data and metadata.
        """
        page = self.doc[page_num]  # 📄 Zeroing in on our page of interest
        image_list = page.get_images(full=True)  # 🖼️ Detecting all embedded visuals
        return [self.doc.extract_image(img[0]) for img in image_list]  # 🎨 Extracting each image

    def get_layout_info(self, page_num: int) -> List[Dict[str, Any]]:
        """
        Analyzes the structure of a page, like an architect examining the
        blueprints of a complex building.

        :param page_num: The page number to analyze (0-indexed).
        :return: A list of dictionaries describing the layout of the page.
        """
        page = self.doc[page_num]  # 📄 Focusing on our target page
        return page.get_text("dict")["blocks"]  # 🧱 Revealing the page's structural elements

    def get_total_pages(self) -> int:
        """
        Determines the total number of pages in our document, like a cartographer
        measuring the extent of newly discovered terrain.

        :return: The total number of pages in the PDF.
        """
        return len(self.doc)  # 📏 Calculating the document's full extent

    def close(self):
        """
        Closes the document, securing all the intelligence we've gathered.
        Always remember to close your files after investigation!
        """
        self.doc.close()  # 🔐 Sealing our case file

# 🌟 For more advanced PDF analysis techniques, consult the PyMuPDF field manual:
# https://pymupdf.readthedocs.io/en/latest/
