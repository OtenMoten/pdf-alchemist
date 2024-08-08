# 🎨 ImageProcessor Test Suite: The Alchemist's Trials 🧪✨
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This script puts our ImageProcessor through rigorous alchemical experiments,
# ensuring it can transmute images with precision and skill.

import pytest  # 🧙‍♂️ Our wise wizard overseeing these alchemical trials
from src.image_processor import ImageProcessor  # 🖼️ Our image alchemist
from PIL import Image  # 🎨 Our magical paintbrush
import io  # 💾 Our mystical data stream


@pytest.fixture
def sample_image_bytes():
    """
    Conjures a sample image for our alchemical experiments.
    Think of it as creating a basic elemental substance for transmutation.
    """
    img = Image.new('RGB', (100, 30), color=(255, 255, 255))  # 🌟 Creating a white canvas
    img_byte_arr = io.BytesIO()  # 🧪 Our alchemical vial
    img.save(img_byte_arr, format='PNG')  # 🖼️ Capturing our image essence
    return img_byte_arr.getvalue()  # 💧 Extracting the pure image elixir


def test_image_processor_initialization():
    """
    Ensures our ImageProcessor can materialize in our alchemical laboratory.
    It's like checking if our alchemist has arrived and is ready to work.
    """
    processor = ImageProcessor()
    assert processor is not None, "Egads! Our image alchemist failed to appear!"


def test_optimize_image(sample_image_bytes):
    """
    Tests the image optimization spell of our ImageProcessor.
    It's like ensuring our alchemist can distill the image essence effectively.

    :param sample_image_bytes: Our base image elixir for the experiment.
    """
    processor = ImageProcessor()
    optimized = processor.optimize_image(sample_image_bytes)

    # 🔍 Inspecting the results of our alchemical transformation
    assert isinstance(optimized, bytes), "Zounds! Our image wasn't transformed into the expected ethereal form (bytes)!"
    assert len(optimized) > 0, "By Merlin's beard! Our optimized image elixir is empty!"


def test_convert_to_base64(sample_image_bytes):
    """
    Examines the base64 encoding transmutation of our ImageProcessor.
    It's akin to verifying our alchemist can turn image lead into base64 gold.

    :param sample_image_bytes: Our base image elixir for the experiment.
    """
    processor = ImageProcessor()
    base64_str = processor.convert_to_base64(sample_image_bytes)

    # 🔍 Scrutinizing our alchemical gold
    assert isinstance(base64_str, str), "Great Scott! Our base64 spell didn't produce the expected string of mystical runes!"
    assert len(base64_str) > 0, "Gadzooks! Our base64 transformation yielded an empty incantation!"
