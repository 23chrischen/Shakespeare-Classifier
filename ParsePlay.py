import numpy as np 
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
import xml.etree.ElementTree as ET
import pprint
import os

"""Parsing the Play""" 
def parsePlay(title):
    
    tree = ET.parse(title)
    root = tree.getroot()
    
    dialogs = {}
    line_number = 0
    
    playtitle = root.findtext("TITLE")
    
    acts = root.findall("ACT")
    for act in acts:
        scenes = act.findall("SCENE")
        for scene in scenes:
            speeches = scene.findall("SPEECH")
            for speech in speeches:
                characters = speech.findall("SPEAKER")
                for character in characters:
                    dialog_line = "\n".join([s.text for s in speech.findall("LINE") if s.text])
                    if character.text not in dialogs.keys():
                        dialogs[character.text] = []
                    if len(dialog_line) > 0:
                        dialogs[character.text].append((line_number,dialog_line))
                        line_number += 1
    
    for character in dialogs.keys():
            if len(dialogs[character]) < 2:
                del dialogs[character]
    return dialogs

def merge_two_dicts(x, y):
    '''Given two dicts, merge them into a new dict as a shallow copy.'''
    z = x.copy()
    z.update(y)
    return z


def getAllTopChars(max_chars=5, dir="./shaks200"):
    chars = {}
    for file in os.listdir(dir):
        if file.endswith(".xml"):
            dialog = parsePlay(dir + '/' + file)
            d = sorted(dialog.items(), key=lambda x: len(x[1]), reverse=True)
            if len(d) > max_chars:
                d = d[:max_chars]
            for i in range(len(d)):
                d[i] = (d[i][0] + '_' + file[:-4] , d[i][1]) #prepend play name to character name
            chars = merge_two_dicts(chars, dict(d))

    return chars

