import ParsePlay
import Interpolate
import CharacterKMeans
import ScaleScores
import pprint
import SentimentAnalysis
import ScaleTime
import LowPassFilter
import matplotlib.pyplot as plt

def getTrainTestSplit(charDict, numTest=10):
    items = charDict.items()
    train = dict(items[10:])
    test = dict(items[:10])
    return train, test


def compare(l1, l2):
    x = []
    for i in range(len(l1)):
        x.append(i)
    plt.plot(x,l1)
    plt.plot(x,l2,'r')
    plt.show()


def main():
    charDict = ParsePlay.getAllTopChars(5) # Char Dict contains a bunch of chars w/ names as keys
    charDictScaled = ScaleTime.rescaleTime(charDict)
    charScores = SentimentAnalysis.turn_lines_to_score(charDictScaled)
    charScoresInterpolated = Interpolate.interpolate_chars_uniformly(charScores, 100)
    charScoresFiltered = LowPassFilter.lowPassAllChars(charScoresInterpolated, window_ratio=.2)
    charScoresScaled = ScaleScores.scale_all_scores(charScoresFiltered)
    train, test = getTrainTestSplit(charScoresScaled, numTest=1)
    clusters = CharacterKMeans.characterKMeans(train, 5)
    pp = pprint.PrettyPrinter()
    chars = zip(*clusters)[1]
    pp.pprint(chars)

    newWithPredicted = CharacterKMeans.predictCluster(test, zip(*clusters)[0], charScoresScaled)
    pp.pprint(newWithPredicted)

if __name__ == '__main__':
    main()