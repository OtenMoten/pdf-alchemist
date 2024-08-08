# 🎭 PDF to HTML Spectacular: The Grand Integration Gala 🌟🔮
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This script orchestrates a magnificent performance, bringing together
# all our star performers in a dazzling display of PDF to HTML transformation.

import pytest  # 🎭 Our esteemed director for this grand production
import os  # 🗺️ Our backstage navigator
from src.pdf_parser import PDFParser  # 🕵️ Our document detective
from src.ocr_engine import OCREngine  # 🔍 Our text archaeologist
from src.image_processor import ImageProcessor  # 🖼️ Our image alchemist
from src.html_generator import HTMLGenerator  # 🌐 Our web illusionist
from bs4 import BeautifulSoup  # 🍲 Our mystical HTML soup diviner


@pytest.fixture
def sample_pdf_path():
    """
    Summons the mystical PDF scroll for our grand performance.
    Ensure you've placed a 'sample.pdf' in the tests directory!
    """
    return os.path.join(os.path.dirname(__file__), 'sample.pdf')


def test_pdf_to_html_conversion(sample_pdf_path, tmp_path):
    """
    The main act of our PDF to HTML spectacular!
    This test brings together all our performers in a harmonious ballet
    of digital transformation.

    :param sample_pdf_path: The path to our mystical PDF scroll.
    :param tmp_path: A magical temporary stage for our creations.
    """
    # 🎭 Summoning our cast of star performers
    pdf_parser = PDFParser(sample_pdf_path)
    ocr_engine = OCREngine()
    image_processor = ImageProcessor()
    html_generator = HTMLGenerator()

    total_pages = pdf_parser.get_total_pages()
    print(f"🎬 Our PDF scroll unfurls to reveal {total_pages} magical pages!")

    for page_num in range(total_pages):
        print(f"✨ Act {page_num + 1} begins!")

        # 🕵️ Our document detective uncovers the secrets of each page
        text = pdf_parser.extract_text(page_num)
        print(f"📜 Extracted {len(text)} characters of ancient text")

        images = pdf_parser.extract_images(page_num)
        print(f"🖼️ Discovered {len(images)} hidden images")

        layout = pdf_parser.get_layout_info(page_num)
        print(f"🏛️ Unveiling the page's architecture: {layout[:2]}...")

        # 🖼️ Our image alchemist transmutes the visual elements
        processed_images = []
        base64_images = []
        for img in images:
            try:
                processed = image_processor.optimize_image(img['image'])
                base64 = image_processor.convert_to_base64(processed)
                processed_images.append(processed)
                base64_images.append(base64)
            except Exception as e:
                print(f"⚠️ A hiccup in our image alchemy: {e}")

        # 🔍 Our text archaeologist deciphers the ancient scripts
        ocr_text = ocr_engine.process_image(text)
        print(f"🔎 Deciphered {len(ocr_text)} characters of text")

        # 🌐 Our web illusionist weaves the elements into HTML magic
        try:
            html_content = html_generator.create_page(ocr_text, base64_images, layout)
        except Exception as e:
            print(f"🌋 Catastrophe in our HTML enchantment: {str(e)}")
            raise

        # 📜 Inscribing our creation onto mystical scrolls (HTML files)
        output_file = tmp_path / f"page_{page_num + 1}.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)

        # 🕵️ Verifying the quality of our magical creation
        assert output_file.exists(), "🌋 Oh no! Our HTML scroll failed to materialize!"

        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 🍲 Our HTML soup diviner examines the magical brew
        soup = BeautifulSoup(content, 'html.parser')

        # 🏗️ Ensuring our HTML architecture is sound
        assert soup.find('html') is not None, "🌋 Catastrophe! The foundational 'html' incantation is missing!"
        assert soup.find('body') is not None, "🌋 Disaster! The 'body' of our HTML being is absent!"

        # 📜 Checking for the presence of textual enchantments
        assert len(soup.get_text().strip()) > 0, "🌋 Alas! Our HTML scroll bears no textual inscriptions!"

        # 🖼️ Verifying the manifestation of visual elements
        if images:
            assert soup.find('img') is not None, "🌋 Curious! The images seem to have vanished in the transformation!"

    # 🎭 The final curtain falls
    pdf_parser.close()
