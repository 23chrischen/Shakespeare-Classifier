import matplotlib.pyplot as plt
import numbers

def bar(scaled):
    x = []
    y = []
    z = []
    for i in range(len(scaled)):
        x.append(i)

    for (ch, l) in scaled.items():
        z.append(ch)
        y.append(len(l))
    plt.bar(x,y)
    plt.xticks(x, z, rotation=90)
    plt.show()

# Pass dict of characters
# charList is list of char names
def compare(charDict, charList):
    for name in charList:
        x = []
        y = []
        if isinstance(charDict[name][0], numbers.Number):
            y = charDict[name]
            x = [i*(float(1)/len(y)) for i in range(len(y))]
        else:
            x, y = zip(*charDict[name])
        plt.plot(x, y, label=name)
    plt.legend()
    plt.show()