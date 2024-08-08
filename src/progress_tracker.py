# 🏃‍♂️ ProgressTracker: The Expedition Chronicler 🗺️📊
# Developed by Team BitFuture
# Website: www.team-bitfuture.de | Email: info@team-bitfuture.de
# Lead Developer: Ossenbrück
# Website: ossenbrück.de | Email: hi@ossenbrück.de
#
# This class is like a seasoned explorer, keeping meticulous records of our
# journey through the vast landscape of PDF pages.

from tqdm import tqdm  # 🌟 Our trusty compass for tracking progress


class ProgressTracker:
    """
    A sophisticated tool for monitoring our expedition through PDF territories.
    Think of it as a high-tech GPS system that provides real-time updates on our
    document processing adventure.
    """

    def __init__(self, total_pages: int):
        """
        Initializes our expedition tracker with the total number of pages to process.

        :param total_pages: The total number of pages in our PDF expedition.
        """
        self.pbar = tqdm(total=total_pages, desc="Processing pages", unit="page")
        # 🗺️ Setting up our digital map to track our journey

    def update(self, n: int = 1):
        """
        Updates our progress, like marking another milestone on our expedition map.

        :param n: The number of pages processed in this update (default is 1).
        """
        self.pbar.update(n)  # 📍 Marking our progress on the digital map

    def close(self):
        """
        Concludes our expedition, wrapping up our progress tracking.
        Always remember to close your tracker after the journey is complete!
        """
        self.pbar.close()  # 🏁 Rolling up our map and concluding the expedition

# 🌟 For more advanced progress tracking techniques, consult the tqdm field guide:
# https://github.com/tqdm/tqdm
