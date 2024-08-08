# 🔍 OCREngine Test Suite: The Text Archaeologist's Expedition 📜🕵️‍♂️
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This script puts our OCREngine through a series of archaeological challenges,
# ensuring it can decipher the most cryptic of textual artifacts.

import pytest  # 🏛️ Our esteemed curator of archaeological tests
from src.ocr_engine import OCREngine  # 🔍 Our text archaeologist extraordinaire
from PIL import Image  # 🖼️ Our magical painting kit
import numpy as np  # 🧮 Our mystical abacus for numerical manipulations


@pytest.fixture
def sample_image():
    """
    Conjures a sample artifact (image) for our textual excavations.
    Think of it as creating a blank papyrus for our tests.
    """
    # 🎨 Painting a pristine white canvas
    img = Image.new('RGB', (100, 30), color=(255, 255, 255))
    return np.array(img)  # 🔢 Converting our canvas to a numerical tapestry


def test_ocr_engine_initialization():
    """
    Ensures our OCREngine can materialize in our archaeological lab.
    It's like checking if our text archaeologist has arrived with all their tools.
    """
    engine = OCREngine()
    assert engine is not None, "Great Scott! Our text archaeologist failed to show up for the expedition!"


def test_process_image(sample_image):
    """
    Tests the image processing prowess of our OCREngine.
    It's like challenging our archaeologist to decipher a blank papyrus.

    :param sample_image: Our pristine papyrus for the test.
    """
    engine = OCREngine()
    text = engine.process_image(sample_image)

    # 🔍 Examining the results of our textual excavation
    assert isinstance(text, str), "By Jove! Our excavation didn't yield a string. What manner of artifact is this?"
    # The papyrus is blank, so we expect either an empty string or an error message
    assert text == "" or text.startswith("Error"), "Curious! Our blank papyrus seems to have hidden text or an unexpected message."


def test_enhance_text():
    """
    Examines the text enhancement capabilities of our OCREngine.
    It's akin to asking our archaeologist to clean and restore an ancient inscription.
    """
    engine = OCREngine()
    enhanced_text = engine.enhance_text("  Sample text  ")

    # 🧼 Inspecting our cleaned and restored text
    assert enhanced_text == "Sample text", "Egad! Our text restoration process seems to have gone awry!"
