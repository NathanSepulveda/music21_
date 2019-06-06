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
StepWiseMotionList = []
RepeatedNotesList = []
PrimaryRegisterList = []
ImportanceOfMiddleRegisterList = []
ImportanceOfBassRegisterList = []
ImportanceOfHighRegisterList = []
PitchVarietyList = []
NoteDensityList = []
MostCommonMelodicIntervalList = []
MostCommonMelodicIntervalPrevalenceList = []

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
    fSw = features.jSymbolic.StepwiseMotionFeature(firstMelody)
    fRn = features.jSymbolic.RepeatedNotesFeature(firstMelody)
    primaryRegister = features.jSymbolic.PrimaryRegisterFeature(firstMelody).extract().vector[0]
    importanceOfMiddleRegister = features.jSymbolic.ImportanceOfMiddleRegisterFeature(firstMelody).extract().vector[0]
    importanceOfBassRegister = features.jSymbolic.ImportanceOfBassRegisterFeature(firstMelody).extract().vector[0]
    importanceOfHighRegister = features.jSymbolic.ImportanceOfHighRegisterFeature(firstMelody).extract().vector[0]
    pitchVariety = features.jSymbolic.PitchVarietyFeature(firstMelody).extract().vector[0]
    noteDensity = features.jSymbolic.PitchVarietyFeature(firstMelody).extract().vector[0]
    mostCommonInterval = features.jSymbolic.MostCommonMelodicIntervalFeature(firstMelody).extract().vector[0]
    mostCommonIntervalPrevalence = features.jSymbolic.MostCommonMelodicIntervalPrevalenceFeature(firstMelody).extract().vector[0]

    range = str(ambitus).split(" ")[1].split('>')[0]

    mostCommonPitchClass = fe.extract().vector[0]
    mostCommonPitchClassPrevalence = fp.extract().vector[0]
    direction = fd.extract().vector[0]
    stepwiseMotionPercentage = fSw.extract().vector[0]
    repeatedNotesPercentage = fRn.extract().vector[0]
   
    print(fe.extract().vector)
    print(fp.extract().vector)
    NotesPercentageList.append(notesPercentage)
    RestPercentageList.append(restsPercentage)
    MostCommonPitchClassList.append(mostCommonPitchClass)
    MostCommonPitchClassRelevanceList.append(mostCommonPitchClassPrevalence)
    StepWiseMotionList.append(stepwiseMotionPercentage)
    AmbitusList.append(range)
    DirectionList.append(direction)
    RepeatedNotesList.append(repeatedNotesPercentage)
    PrimaryRegisterList.append(primaryRegister)
    ImportanceOfMiddleRegisterList.append(importanceOfMiddleRegister)
    ImportanceOfBassRegisterList.append(importanceOfBassRegister)
    ImportanceOfHighRegisterList.append(importanceOfHighRegister)
    PitchVarietyList.append(pitchVariety)
    NoteDensityList.append(noteDensity)
    MostCommonMelodicIntervalList.append(mostCommonInterval)
    MostCommonMelodicIntervalPrevalenceList.append(mostCommonIntervalPrevalence)





dictToTest = {'Notes Percentage': NotesPercentageList, 
              'Rest Percentage' : RestPercentageList, 
              'Most Common Pitch Class': MostCommonPitchClassList, 
              'Most Common Pitch Class Prevalence': MostCommonPitchClassRelevanceList,
              'Ambitus': AmbitusList, 
              "Direction": DirectionList, 
              'Stepwise Motion Percentage': StepWiseMotionList,
              "Repeated Notes Percentage" : RepeatedNotesList, 
              "Primary Register": PrimaryRegisterList, 
              "Pitch Variety": PitchVarietyList,
              "Note Density": NoteDensityList, 
              "Most Common Melodic Interval": MostCommonMelodicIntervalList, 
              "Most Common Melodic Interval Prevalence": MostCommonMelodicIntervalPrevalenceList,
              "Importance of Middle Register": ImportanceOfMiddleRegisterList,
              "Importance of Bass Register": ImportanceOfBassRegisterList,
              "Importance of High Register": ImportanceOfHighRegisterList}
df = pd.DataFrame(dictToTest)
df.to_csv('file2.csv')