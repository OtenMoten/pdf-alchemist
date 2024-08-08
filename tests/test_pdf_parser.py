# 🕵️‍♂️ PDFParser Test Suite: The Document Detective's Case Files 📁🔍
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This script puts our PDFParser through a series of investigative challenges,
# ensuring it can uncover the secrets hidden within the most mysterious of PDFs.

import pytest  # 🏛️ Our esteemed curator of investigative tests
from src.pdf_parser import PDFParser  # 🕵️‍♂️ Our document detective extraordinaire
import os  # 🗺️ Our file system cartographer


@pytest.fixture
def sample_pdf_path():
    """
    Procures a sample case file (PDF) for our investigations.
    Ensure you've placed a 'sample.pdf' in the tests directory!
    """
    return os.path.join(os.path.dirname(__file__), 'sample.pdf')


def test_pdf_parser_initialization(sample_pdf_path):
    """
    Ensures our PDFParser can open the case file successfully.
    It's like checking if our detective has all the necessary clearance.
    """
    parser = PDFParser(sample_pdf_path)
    assert parser.doc is not None, "Great Scott! Our detective couldn't access the case file!"


def test_extract_text(sample_pdf_path):
    """
    Tests the text extraction capabilities of our PDFParser.
    It's akin to challenging our detective to read the fine print.

    :param sample_pdf_path: The path to our sample case file.
    """
    parser = PDFParser(sample_pdf_path)
    text = parser.extract_text(0)  # Investigating the first page
    assert isinstance(text, str), "By Jove! Our extracted evidence isn't in textual form!"
    assert len(text) > 0, "Egad! Our case file appears to be devoid of textual clues!"


def test_extract_images(sample_pdf_path):
    """
    Examines the image extraction prowess of our PDFParser.
    It's like asking our detective to collect all visual evidence.
    """
    parser = PDFParser(sample_pdf_path)
    images = parser.extract_images(0)  # Collecting visual evidence from the first page
    assert isinstance(images, list), "Zounds! Our visual evidence isn't in the expected dossier format!"


def test_get_layout_info(sample_pdf_path):
    """
    Tests the layout analysis capabilities of our PDFParser.
    It's akin to having our detective map out the crime scene.
    """
    parser = PDFParser(sample_pdf_path)
    layout = parser.get_layout_info(0)  # Mapping the first page
    assert isinstance(layout, list), "Heavens! Our crime scene map isn't in the proper format!"
    assert len(layout) > 0, "Curious! Our case file seems to lack any discernible structure!"


def test_get_total_pages(sample_pdf_path):
    """
    Verifies that our PDFParser can determine the case file's extent.
    It's like ensuring our detective knows how deep the rabbit hole goes.
    """
    parser = PDFParser(sample_pdf_path)
    total_pages = parser.get_total_pages()
    assert isinstance(total_pages, int), "Good grief! The case file's extent isn't quantifiable!"
    assert total_pages > 0, "Impossible! We seem to have a case file with no pages!"


def test_close(sample_pdf_path):
    """
    Checks if our PDFParser can properly close the case file.
    It's crucial for our detective to know how to seal confidential documents.
    """
    parser = PDFParser(sample_pdf_path)
    parser.close()
    assert parser.doc.is_closed, "Oh dear! Our detective failed to seal the case file properly!"
