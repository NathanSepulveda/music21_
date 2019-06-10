#tranposes the melody given the key and melody
def transpose(currentKey, melody):
    transpositionKey = {
    "b minor": -2,
    "D major": -2,
    "D- major": -1,
    "c minor": -3,
    "E- major": -3
}
    currentKey = str(currentKey)
    print("Current KEY", currentKey)
    if currentKey in transpositionKey:
        transposedMelody = melody.transpose(transpositionKey[currentKey])
    return transposedMelody


# return ratio of pentatonic notes
def derivePentatonicism(totalNotes, currentNoteDictionary):
    pentNoteCount = 0
    pentatonicPitchClasses = [0, 2, 4, 7, 9]
    for k in currentNoteDictionary:
        if k in pentatonicPitchClasses:
            pentNoteCount += currentNoteDictionary[k]
    ratio = pentNoteCount/totalNotes
    return ratio