"""
Outputs a .toml file to use in a course page for gdquest.com
Takes a CSV file as input
"""
import os
import tkinter as tk
from tkinter import filedialog
import codecs
import csv


CHAPTER_TEMPLATE = "title = \"\"\nsmall = \"\"\ndescription = \"\"\n"


def get_csv_file_ui(start_folder=""):
    tk.Tk().withdraw()
    folder = filedialog.askdirectory(initialdir=start_folder).replace('/', '\\')
    files = os.listdir(folder)
    return next(f for f in files if f.endswith('.csv'))


def get_csv_data(file_path):
    """Generator that yields brush file data from a CSV file"""
    with codecs.open(file_path, 'r', 'utf-8-sig') as data:
        csv_iterable = csv.reader(data)
        header = next(csv_iterable)
        for row in csv_iterable:
            current_line = dict(zip(header, row))
            yield current_line


csv_file = get_csv_file_ui()

if not csv_file:
    raise AttributeError('Missing CSV file')

print('Processing file \'' + csv_file + '\'')

# ------
# SCRIPT
# ------
chapter_id = 0
video_id = 0
with open('output.toml', 'w') as output:
    for data in get_csv_data(csv_file):
        if data['TITLE'].startswith('CHAPTER'):
            chapter_id += 1
            if chapter_id != 1:
                output.write('\n\n')
            output.write("[chapters.{}]\n".format(chapter_id) + CHAPTER_TEMPLATE + '\n')
            continue

        video_id += 1
        output.write("[chapters.{}.videos.{}]\n".format(chapter_id, video_id))
        output.write("title = \"{}\"\n".format(data['TITLE']))
        output.write("url = \"{}\"\n".format(data['URL']))
