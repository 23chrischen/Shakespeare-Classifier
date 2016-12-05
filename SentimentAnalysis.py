import nltk
from nltk.corpus import shakespeare
from nltk.sentiment.vader import SentimentIntensityAnalyzer 

sid = SentimentIntensityAnalyzer()

def diff(line):
    ss = sid.polarity_scores(line)
    tot = 0
    for k in sorted(ss):
        if(k=='neg'):
            tot = tot - ss[k]
        elif(k=='pos'):
            tot = tot + ss[k]
    return tot

def turn_lines_to_score(char_dict, score_func="diff"):
    new_dict = {}
    for (ch,line) in char_dict.items():
        new_dict[ch] = []
        for n, l in line:
            if score_func=="diff":
                score = diff(l)
            new_dict[ch].append((n, score))
    return new_dict
