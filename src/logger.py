# 📝 Logger: The Expedition Chronicler 📔🖋️
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This class is like a diligent scribe, meticulously recording every
# step of our PDF processing adventure.

import logging  # 📚 Our enchanted quill for recording the journey
from typing import Any  # 🔮 Our crystal ball for type divination


class Logger:
    """
    A sophisticated tool for documenting our PDF expedition.
    Think of it as a magical journal that automatically records
    our progress, challenges, and triumphs in real-time.
    """

    def __init__(self, name: str, log_file: str = 'app.log'):
        """
        Prepares our magical journal for the upcoming adventure.

        :param name: The name of our expedition (logger name).
        :param log_file: The sacred scroll where we'll record our journey (default: 'app.log').
        """
        self.logger = logging.getLogger(name)  # 📜 Creating our magical journal
        self.logger.setLevel(logging.DEBUG)  # 🔍 Setting our journal to record even the tiniest details

        # 🖋️ Preparing our different writing implements
        c_handler = logging.StreamHandler()  # For quick notes (console output)
        f_handler = logging.FileHandler(log_file)  # For detailed records (file output)
        c_handler.setLevel(logging.INFO)  # 📢 Set to record important announcements
        f_handler.setLevel(logging.DEBUG)  # 🔬 Set to record every minute detail

        # 🎨 Designing our journal entry templates
        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)  # 🖌️ Applying our quick note template
        f_handler.setFormatter(f_format)  # 🖌️ Applying our detailed record template

        # 📚 Binding our writing implements to the magical journal
        self.logger.addHandler(c_handler)
        self.logger.addHandler(f_handler)

    def get_logger(self) -> Any:
        """
        Retrieves our magical journal for use in documenting the expedition.

        :return: The enchanted logger object, ready to record our adventure.
        """
        return self.logger  # 🎁 Presenting our fully prepared magical journal

# 🌟 For more advanced chronicling techniques, consult the Python logging grimoire:
# https://docs.python.org/3/library/logging.html
