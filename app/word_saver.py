"""Module with a class saving words to database"""
import sqlite3
from typing import List

class WordSaver:
    """Handles creation of table and saving words to database"""
    def __init__(self, connection: sqlite3.Connection, config: dict):
        self.connection = connection
        self.config = config
        self.__create_table()

    def __create_table(self):
        """Creates table with name based on config 
        if there isn't one already"""
        cursor = self.connection.cursor()
        language: str = self.config["lobby_settings"]["language"]

        query = f"""
            CREATE TABLE IF NOT EXISTS words_{language.lower()}(
                word TEXT UNIQUE NOT NULL
            );
        """
        cursor.execute(query)

    def save_words(self, words: List[str]):
        """Saves words to database"""
        data = [(word,) for word in words] # convert array to tuple array
        language: str = self.config["lobby_settings"]["language"]
        query = f"""
            INSERT OR IGNORE INTO words_{language.lower()}(word)
            VALUES (?);
        """
        cursor = self.connection.cursor()
        cursor.executemany(query, data)
        self.connection.commit()
