"""Module with class that counts words per sec"""
import time

class ScrapeSpeedTracker():
    """Counts words per sec"""

    def __init__(self):
        self.start_time = None
        self.total_words = 0

    def start(self):
        """Starts counting time"""
        self.start_time = time.time()
        print("WPS tracker started")

    def record(self, word_count):
        """Records words added"""
        self.total_words += word_count

    def get_words_per_second(self):
        """Calculates and returns words per second"""
        if not self.start_time:
            return 0
        elapsed_time = time.time() - self.start_time
        if elapsed_time == 0:
            return 0
        return self.total_words / elapsed_time

    def report(self):
        """Creates and prints a report about words per second"""
        wps = self.get_words_per_second()
        print(f'''[Scraper Stats]
WPS: {wps:.2f}
Time: {time.time() - self.start_time:.2f}s
Words {self.total_words}
        ''')
