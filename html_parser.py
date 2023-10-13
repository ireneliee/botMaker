import os 
import glob
import re
from config import DATA_FOLDER, CONTACT_NAMES, EXCLUDED_ITEMS

def collect_all_conversation(folder_name):
    with open('parse_result.txt', 'a') as write_result:
        file_paths = glob.glob(os.path.join(folder_name, '*'))
        for file_path in file_paths:
            with open(file_path, 'r') as file:
                content = file.read()
                parse_content(content, write_result)

excluded_items = CONTACT_NAMES + EXCLUDED_ITEMS
def parse_content(content, write_result):
    lines = content.split("\n")
    for line in lines:
        excluded = False
        for item in excluded_items:
            if line.find(item) != -1:
                excluded = True
        if not excluded and not re.search(r'\d', line) and len(line) > 2:
            write_result.write(line)
            write_result.write("\n")

def empty_file():
    with open('parse_result.txt', 'w') as write_result:
        write_result.write("")

empty_file()
collect_all_conversation(DATA_FOLDER)
