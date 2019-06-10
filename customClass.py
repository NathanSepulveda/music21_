from music21 import *


corpus.addPath('/Users/nathansepulveda/Desktop/TEST')

sadness = corpus.parse("0084.xml")
cello = sadness.getElementById("Bass Hook")

print(cello.analyze('key'))

for n in cello.notes.recurse():
    print(n)