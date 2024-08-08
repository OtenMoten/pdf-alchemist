# 🎭 HTMLGenerator: The Digital Illusionist 🌐✨
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This class is like a master illusionist, weaving text and images
# into a captivating web performance.

import dominate  # 🎭 Our magical stage for creating HTML performances
from dominate.tags import *  # 🎭 Our troupe of HTML element performers
from typing import List, Dict, Any  # 🎟️ Our type-checking usher


class HTMLGenerator:
    """
    A sophisticated toolkit for crafting HTML spectacles.
    Think of it as a grand theater where text and images come
    together in a perfectly choreographed web performance.
    """

    def create_page(self, text: str, images: List[str], layout: List[Dict[str, Any]]) -> str:
        """
        Directs a grand HTML performance, bringing together text and images
        in a visually stunning webpage.

        :param text: The script of our performance (OCR text).
        :param images: Our visual props (base64 encoded images).
        :param layout: The stage directions for our performance.
        :return: The rendered HTML performance as a string.
        """
        doc = dominate.document(title='PDF Page')  # 🎬 Setting the stage

        with doc.head:
            self.add_style()  # 🎨 Applying our artistic flair

        with doc.body:
            # 📜 Presenting our script at the top of the stage
            with p(cls="ocr-text"):
                for line in text.split('\n'):
                    span(line)
                    br()

            # 🎭 Positioning our performers (text and images) on stage
            for block in layout:
                if block['type'] == 0 and 'text' in block:  # Text performer
                    p(block['text'], style=f"position: absolute; top: {block['bbox'][1]}px; left: {block['bbox'][0]}px;")
                elif block['type'] == 1 and 'number' in block:  # Image performer
                    img_index = block['number']
                    if img_index < len(images):
                        img(src=f"data:image/jpeg;base64,{images[img_index]}",
                            style=f"position: absolute; top: {block['bbox'][1]}px; left: {block['bbox'][0]}px; width: {block['bbox'][2] - block['bbox'][0]}px; height: {block['bbox'][3] - block['bbox'][1]}px;")

        return doc.render()  # 🎉 Presenting our grand performance

    @staticmethod
    def add_style():
        """
        Applies the artistic styling to our HTML performance,
        like a costume designer dressing the stage.
        """
        style("""
            body { position: relative; font-family: Arial, sans-serif; }
            p { margin: 0; padding: 0; }
            .ocr-text { margin-bottom: 20px; white-space: pre-wrap; }
        """)

# 🌟 For more advanced HTML wizardry, consult the Dominate spellbook:
# https://github.com/Knio/dominate
