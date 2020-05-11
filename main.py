import sys
import json
from collections import Counter

sys.path.insert(0, '../')

import Reader as rd
with open("info_update.json", "r") as json_file:
    info_update = json.load(json_file)

with open("info.txt", "r") as listFile:
    info = json.load(listFile)


def WordPrediction(sel_input):

    indexes = []

    if sel_input in info_update.keys():

        for i in range(len(info)):
            if sel_input == info[i] and i+1 < len(info):
                indexes.append(i+1)

        if indexes:
            repeat = []
            for i in indexes:
                posible = info[i]
                if sel_input == info[i-1]:
                    repeat.append(posible)

        a = Counter(repeat)
        prediction = []
        for i in range(0, 3):
            if len(a):
                key_max = max(a.keys(), key=(lambda k: a[k]))
                if key_max == "":
                    del a[key_max]
                else:
                    prediction.append(key_max)
                    del a[key_max]

        if len(prediction) == 2:
            prediction.append('')

        elif len(prediction) == 1:
            prediction.append('')
            prediction.append('')
        
        prediction = tuple(prediction)

        return prediction  


if __name__ == "__main__":

    inpu = input()

    inpu.lower()
    
    total = inpu + ' '

    if WordPrediction(inpu.lower()):
        while inpu:
            a, b, c = WordPrediction(inpu.lower())
            if a:
                print('Type 1 to choose ', a)
            if b:
                print('Type 2 to choose ', b)
            if c:
                print('Type 3 to choose ', c)
            inpu = input()
            if inpu == '1' and a:
                inpu = a
            if inpu == '2' and b:
                inpu = b
            if inpu == '3' and c:
                inpu = c
            total += inpu + ' '
            print(total)
    
    









