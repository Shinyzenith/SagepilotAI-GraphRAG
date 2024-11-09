import nest_asyncio
import os
import urllib.request

nest_asyncio.apply()

path = os.path.join(os.getcwd(), 'input.txt')
with open(path, 'r+', encoding='utf-8') as file:
    # Only perform RAG on first 900 lines
    lines = file.readlines()
    file.seek(0)
    file.writelines(lines[:900])  # Decrease this number if you want to save api key cost.
    file.truncate()
