"""Module with a class saving words to database"""
import sqlite3

class WordSaver:
    """Handles creation of table and saving words to database"""
    def __init__(self, connection: sqlite3.Connection, config: dict):
        self.connection = connection
        self.config = config
        self.create_table()

    def create_table(self):
        """Creates table"""
        cursor = self.connection.cursor()
        language: str = self.config["lobby_settings"]["language"]

        query = f"""
            CREATE TABLE IF NOT EXISTS words_{language.lower()}(
                word TEXT UNIQUE NOT NULL
            );
        """
        cursor.execute(query)

    def save_words(self, words):
        """Saves words to table"""
        data = [(word,) for word in words]
        language: str = self.config["lobby_settings"]["language"]
        query = f"""
            INSERT OR IGNORE INTO words_{language.lower()}(word)
            VALUES (?);
        """
        cursor = self.connection.cursor()
        cursor.executemany(query, data)
        self.connection.commit()
