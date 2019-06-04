from music21 import *
import matplotlib.pyplot as plt
import pandas as pd



corpus.addPath('/Users/nathansepulveda/Desktop/TEST')

sadness = corpus.parse("Fancy.xml")
cello = sadness.getElementById("Spiked Bass")
measureStart = int(input("Start"))
measureEnd = int(input("End"))



firstMelody = cello.measures(measureStart, measureEnd).stripTies()
t = firstMelody.quantize([4], processOffsets=True, processDurations=True, inPlace=False)

durations = [0]
notes = ["Start"]
positions = [0]
sum = 0


totalDuration = 0
noteDuration = 0
restDuration = 0

for n in firstMelody.notesAndRests.flat:
    totalDuration += n.quarterLength
    if n.isNote:
        print("Note", n.quarterLength, n.pitch)
        noteDuration += n.quarterLength
    else: 
        print("Rest", n.quarterLength)
        restDuration += n.quarterLength

song = {}
    

notesPercentage = "%.2f" % (noteDuration/totalDuration)
restsPercentage = "%.2f" % (restDuration/totalDuration)
song["Notes Percentage"] = notesPercentage
song["Rests Percentage"] = restsPercentage
print(notesPercentage, restsPercentage)
fe = features.jSymbolic.MostCommonPitchClassFeature(firstMelody)
fp = features.jSymbolic.MostCommonPitchClassPrevalenceFeature(firstMelody)
mostCommonPitchClass = fe.extract().vector[0]
mostCommonPitchClassPrevalence = fp.extract().vector[0]
print(fe.extract().vector)
print(fp.extract().vector)
npS = [notesPercentage]
rpS = [restsPercentage]
mCPC = [mostCommonPitchClass]
mCPCP = [mostCommonPitchClassPrevalence]

dictToTest = {'Notes Percentage': npS, 'Rest Percentage' : rpS, 'Most Common Pitch Class': mCPC, 'Most Common Pitch Class Prevalence': mCPCP}

df = pd.DataFrame(dictToTest)
df.to_csv('file.csv')

song["Most Common Pitch Class"] = fe.extract().vector[0]
song["Most Common Pitch Class Prevalence"] = fp.extract().vector[0]
print(song)





p = graph.plot.HistogramPitchClass(firstMelody)
p.run()


