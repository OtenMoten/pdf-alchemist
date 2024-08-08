# 🎨 ImageProcessor: The Digital Alchemist 🖼️✨
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This class is like a skilled alchemist, transforming and optimizing
# digital images with mystical precision.

from PIL import Image  # 🖼️ Our magical canvas for image manipulation
import io  # 💾 Our mystical data stream conduit
import base64  # 🔐 Our arcane encoder for image secrets
from typing import Union  # 🔀 Our shape-shifting spell for type flexibility


class ImageProcessor:
    """
    A sophisticated toolkit for transmuting digital images.
    Think of it as an alchemist's laboratory, where pixels are
    refined and images are transformed into their most potent forms.
    """

    @staticmethod
    def optimize_image(image: Union[bytes, Image.Image], format: str = 'JPEG', quality: int = 85) -> bytes:
        """
        Optimizes an image, like distilling a potion to its most potent essence.

        :param image: The raw image material, either as bytes or a PIL Image.
        :param format: The desired format of our alchemical creation (default: 'JPEG').
        :param quality: The purity level of our image elixir (default: 85).
        :return: The optimized image as a bytes object.
        """
        # 🧪 Preparing our alchemical ingredients
        if isinstance(image, bytes):
            img = Image.open(io.BytesIO(image))
        else:
            img = image

        # 🏺 Creating our alchemical vessel
        img_io = io.BytesIO()

        # 🔥 Performing the alchemical transformation
        img.save(img_io, format=format, quality=quality, optimize=True)

        # 📦 Bottling our optimized image elixir
        return img_io.getvalue()

    @staticmethod
    def convert_to_base64(image_data: bytes) -> str:
        """
        Transmutes an image into its base64 form, like turning lead into gold.

        :param image_data: The raw image data to be transmuted.
        :return: The image data encoded in base64, as a string of mystical runes.
        """
        # 🔮 Casting our base64 encoding spell
        return base64.b64encode(image_data).decode('utf-8')

# 🌟 For more advanced image alchemy, consult the Pillow grimoire:
# https://pillow.readthedocs.io/en/stable/
