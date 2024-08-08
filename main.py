# 🎭 PDF Transformation Extravaganza: The Grand Performance 🎪✨
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This script orchestrates a magnificent show, transforming PDFs into 
# a dazzling HTML spectacle.

import os  # 🗺️ Our backstage map for navigating the file system

# 🎭 Summoning our troupe of talented performers
from src.html_generator import HTMLGenerator  # 🌐 Our web illusionist
from src.image_processor import ImageProcessor  # 🖼️ Our image alchemist
from src.logger import Logger  # 📝 Our diligent chronicler
from src.ocr_engine import OCREngine  # 🔍 Our text archaeologist
from src.pdf_parser import PDFParser  # 🕵️ Our document detective
from src.progress_tracker import ProgressTracker  # 🏃 Our expedition tracker


def main(path_to_pdf: str, out_dir: str):
    """
    The main act of our PDF transformation extravaganza.

    :param path_to_pdf: The mystical scroll (PDF) to be transformed.
    :param out_dir: The enchanted realm where our creations will manifest.
    """
    # 📜 Summoning our chronicler to document this grand adventure
    logger = Logger(__name__).get_logger()
    logger.info(f"🎬 Raising the curtain on {path_to_pdf}")

    # 🎭 Assembling our cast of performers
    pdf_parser = PDFParser(path_to_pdf)  # Our lead investigator
    ocr_engine = OCREngine()  # Our linguistic expert
    image_processor = ImageProcessor()  # Our visual effects wizard
    html_generator = HTMLGenerator()  # Our grand illusionist

    # 🗺️ Charting the course of our adventure
    total_pages = pdf_parser.get_total_pages()
    progress_tracker = ProgressTracker(total_pages)

    # 🎭 Let the show begin! Processing each page of our mystical scroll
    for page_num in range(total_pages):
        try:
            # 🕵️ Uncovering the secrets of each page
            text = pdf_parser.extract_text(page_num)
            images = pdf_parser.extract_images(page_num)
            layout = pdf_parser.get_layout_info(page_num)

            # 🖼️ Transforming our visual elements
            processed_images = [image_processor.optimize_image(img['image']) for img in images]
            base64_images = [image_processor.convert_to_base64(img) for img in processed_images]

            # 🔍 Enhancing our textual discoveries
            enhanced_text = ocr_engine.process_image(text)

            # 🌐 Weaving our elements into a web spectacle
            html_content = html_generator.create_page(enhanced_text, base64_images, layout)

            # 📁 Manifesting our creation in the physical realm
            output_file = os.path.join(out_dir, f"page_{page_num + 1}.html")
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html_content)

            # 🏃 Marking our progress on this grand expedition
            progress_tracker.update()
            logger.info(f"🎉 Act {page_num + 1} completed successfully")

        except Exception as e:
            logger.error(f"🎭 Plot twist in Act {page_num + 1}: {str(e)}")

    # 🎬 The grand finale
    progress_tracker.close()
    pdf_parser.close()
    logger.info("🎭 The curtain falls on our PDF transformation extravaganza!")


if __name__ == "__main__":
    # 🎟️ Setting the stage for our performance
    pdf_path = "input.pdf"  # Our starring scroll
    output_dir = "output"  # The gallery for our creations
    os.makedirs(output_dir, exist_ok=True)  # Preparing our exhibition space

    # 🎭 Let the show begin!
    main(pdf_path, output_dir)

# 🌟 For an encore performance or to join our troupe, contact Team BitFuture!
