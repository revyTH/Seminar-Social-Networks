

import json
import os






def main():

    dir = os.listdir("results/")

    for file in dir:
        if file[:1] == ".":
            continue

        jsonData = json.load(file)
        print jsonData
        break





