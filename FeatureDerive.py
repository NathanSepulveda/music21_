from music21 import *
import matplotlib.pyplot as plt
import pandas as pd


corpus.addPath('/Users/nathansepulveda/Desktop/TEST')


# define the local corpora 
localCorpus = corpus.corpora.LocalCorpus()
listOfWorks = localCorpus.getPaths()

NotesPercentageList = []
RestPercentageList = []
MostCommonPitchClassList = []
MostCommonPitchClassRelevanceList = []
AmbitusList = []
DirectionList = []


for work in listOfWorks:
    print(work)
    work = str(work)
    work = work.split("TEST/")[1]
    t = work.split(".")[0]
    work = corpus.parse(work)

    section = work.getElementById("Spiked Bass")
    measureStart = int(input("Start"))
    measureEnd = int(input("End"))

    firstMelody = section.measures(measureStart, measureEnd).stripTies()

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
    
    notesPercentage = "%.2f" % (noteDuration/totalDuration)
    restsPercentage = "%.2f" % (restDuration/totalDuration)
  
    print(notesPercentage, restsPercentage)
    fe = features.jSymbolic.MostCommonPitchClassFeature(firstMelody)
    fp = features.jSymbolic.MostCommonPitchClassPrevalenceFeature(firstMelody)
    ambitus = firstMelody.analyze('ambitus')
    fd = features.jSymbolic.DirectionOfMotionFeature(firstMelody)
    print(dir(fd))

    range = str(ambitus).split(" ")[1].split('>')[0]

    mostCommonPitchClass = fe.extract().vector[0]
    mostCommonPitchClassPrevalence = fp.extract().vector[0]
    direction = fd.extract().vector[0]
    print(fe.extract().vector)
    print(fp.extract().vector)
    NotesPercentageList.append(notesPercentage)
    RestPercentageList.append(restsPercentage)
    MostCommonPitchClassList.append(mostCommonPitchClass)
    MostCommonPitchClassRelevanceList.append(mostCommonPitchClassPrevalence)
    AmbitusList.append(range)
    DirectionList.append(direction)


dictToTest = {'Notes Percentage': NotesPercentageList, 'Rest Percentage' : RestPercentageList, 'Most Common Pitch Class': MostCommonPitchClassList, 'Most Common Pitch Class Prevalence': MostCommonPitchClassRelevanceList,
                'Ambitus': AmbitusList, "Direction": DirectionList}
df = pd.DataFrame(dictToTest)
df.to_csv('file2.csv')