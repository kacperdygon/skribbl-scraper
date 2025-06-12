# pylint: skip-file
import sqlite3
import json

database = 'words'
table = 'words_polish'
query = f'SELECT word FROM {table}'
export_file = 'words.json'

connection = sqlite3.connect(database)
cursor = connection.cursor()

cursor.execute(query)
rows = cursor.fetchall()

words = [row[0] for row in rows]

with open(export_file, 'w', encoding='utf-8') as file:
    json.dump(words, file, ensure_ascii=False, indent = 2)

connection.close()
print(f'{len(words)} were saved to {export_file}')
