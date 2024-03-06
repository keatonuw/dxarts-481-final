# Bespoke CSV parsing for this dataset
# Just a simple script - grab the tweets, drop links & newlines, write to corpus.

import csv
import re

with open("corpus.txt", "w") as file:
    with open("ChatGPT-tweets.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) > 2:
                s: str = str(row[2].encode("ascii", "ignore").decode())

                # drop links
                s = re.sub(r"(https:|http:|www\.)\S*", "", s)
                # drop new lines (per row)
                s = re.sub(r"\n", "", s)

                file.write(f"{s}\n")
