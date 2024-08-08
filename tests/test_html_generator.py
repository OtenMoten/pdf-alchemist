# 🎭 HTMLGenerator Test Suite: The Dress Rehearsal 🕴️🔍
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This script puts our HTMLGenerator through its paces, ensuring
# it's ready for the grand performance.

import pytest  # 🎭 Our esteemed director for this test production
from src.html_generator import HTMLGenerator  # 🌐 Our star performer


@pytest.fixture
def sample_data():
    """
    Prepares a costume trunk full of sample data for our tests.
    Think of it as the props and scripts for our dress rehearsal.
    """
    return {
        'text': 'Sample text',  # 📜 Our script
        'images': ['base64_encoded_image_data'],  # 🖼️ Our visual props
        'layout': [  # 🎬 Our stage directions
            {'type': 0, 'text': 'Sample text', 'bbox': [0, 0, 100, 30]},
            {'type': 1, 'number': 0, 'bbox': [0, 30, 100, 60]}
        ]
    }


def test_html_generator_initialization():
    """
    Ensures our HTMLGenerator can make a grand entrance onto the stage.
    It's like checking if our star performer is present and ready.
    """
    generator = HTMLGenerator()
    assert generator is not None, "Oh no! Our star performer failed to show up!"


def test_create_page(sample_data):
    """
    Puts our HTMLGenerator through its paces, making sure it can
    create a stunning HTML performance from our sample data.

    :param sample_data: Our costume trunk of test props and scripts.
    """
    generator = HTMLGenerator()
    html = generator.create_page(sample_data['text'], sample_data['images'], sample_data['layout'])

    # 🕵️ Let's inspect the result of our performance
    assert isinstance(html, str), "Oops! Our performance didn't result in a string. The audience will be confused!"
    assert 'Sample text' in html, "Oh dear, our script didn't make it onto the stage!"
    assert 'base64_encoded_image_data' in html, "Uh-oh, our visual props are missing from the performance!"
