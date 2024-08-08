# 🔍 OCREngine: The Text Archaeologist 📜🕵️‍♂️
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This class is like a skilled archaeologist, unearthing hidden text
# from the ancient artifacts of digital images.

import pytesseract  # 🔬 Our high-tech microscope for deciphering text
from PIL import Image  # 🖼️ Our artifact handling tools
import cv2  # 🎥 Our advanced imaging equipment
import numpy as np  # 🧮 Our computational abacus
from typing import Union  # 🔀 Our type-juggling assistant
import io  # 💾 Our data stream navigator
import os  # 🗺️ Our file system cartographer


class OCREngine:
    """
    A sophisticated tool for excavating text from various image formats.
    Think of it as a high-tech scanner that can reveal hidden inscriptions
    on digital artifacts, turning pixels into legible text.
    """

    def __init__(self):
        """
        Initializes our text archaeology lab, setting up the equipment for Windows explorers.
        For other operating systems, we assume the tools are already in their toolbelts (PATH).
        """
        # 🏗️ Setting up our dig site
        if os.name == 'nt':  # for Windows adventurers
            tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            if os.path.exists(tesseract_cmd):
                pytesseract.pytesseract.tesseract_cmd = tesseract_cmd

    def process_image(self, image: Union[np.ndarray, Image.Image, bytes, str]) -> str:
        """
        Processes an image artifact to extract its textual secrets.

        :param image: The image artifact in various possible forms.
        :return: The deciphered text from the image.
        """
        try:
            # 📜 If it's already text, just polish it
            if isinstance(image, str):
                return self.enhance_text(image)

            # 🖼️ Converting our artifact to a standard format
            if isinstance(image, Image.Image):
                image = np.array(image)
            elif isinstance(image, bytes):
                image = np.array(Image.open(io.BytesIO(image)))

            # 🌈 Ensuring our artifact is in the right color spectrum
            if len(image.shape) == 2:  # Monochrome relic
                image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
            elif len(image.shape) == 3 and image.shape[2] == 3:  # Colorful find
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            elif len(image.shape) == 3 and image.shape[2] == 4:  # Transparent treasure
                image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

            # 🧼 Cleaning our artifact for better analysis
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

            # 🔍 Deciphering the cleaned artifact
            text = pytesseract.image_to_string(threshold)
            return self.enhance_text(text)
        except pytesseract.TesseractNotFoundError:
            return "Error: Our deciphering tools (Tesseract) are missing from the expedition kit!"
        except Exception as e:
            return f"Error: Our artifact analysis encountered an unexpected challenge: {str(e)}"

    @staticmethod
    def enhance_text(text: str) -> str:
        """
        Polishes the extracted text, like a linguistic conservator
        restoring an ancient manuscript.

        :param text: The raw text extracted from the image.
        :return: The enhanced and cleaned text.
        """
        # 🧹 Here we'd implement text enhancement logic
        # (e.g., spell checking, formatting correction)
        return text.strip()

# 🌟 For more advanced text excavation techniques, consult the Tesseract scrolls:
# https://github.com/tesseract-ocr/tesseract
