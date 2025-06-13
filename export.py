# pylint: skip-file
import sqlite3
import json
import argparse

def main():

    parser = argparse.ArgumentParser(description="Skribbl.io scraper")

    parser.add_argument("--language", type=str, 
                        required=True, help="Table that words are going to be exported from")
    parser.add_argument("--export-file", type=str, 
                        default="words.json", help="File that words are exported to")

    args = parser.parse_args()

    database = 'words'
    table = f'words_{args.language.lower()}'
    query = f'SELECT word FROM {table}'
    export_file = args.export_file

    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute(query)
    except sqlite3.OperationalError as e:
        if "no such table" in str(e):
            print("Table with words in selected language doesn't exist")
            return
        else:
            raise

    rows = cursor.fetchall()

    words = [row[0] for row in rows]

    with open(export_file, 'w', encoding='utf-8') as file:
        json.dump(words, file, ensure_ascii=False, indent = 2)

    connection.close()
    print(f'{len(words)} words were saved to {export_file}')

if __name__ == "__main__":
    main()