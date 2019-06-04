from music21 import *
import matplotlib.pyplot as plt



corpus.addPath('/Users/nathansepulveda/Desktop/TEST')

sadness = corpus.parse("Fancy.xml")
cello = sadness.getElementById("Spiked Bass")
measureStart = int(input("Start"))
measureEnd = int(input("End"))


firstMelody = cello.measures(measureStart, measureEnd).stripTies()
t = firstMelody.quantize([4], processOffsets=True, processDurations=True, inPlace=False)

# print([e.offset for e in t])
# firstMelody.show()


durations = [0]
notes = ["Start"]
positions = [0]
sum = 0

totalDuration = 0
noteDuration = 0
restDuration = 0


for n in firstMelody.notesAndRests.flat:
	if n.isNote:
		notes.append(n.pitch.midi)
		durations.append(n.quarterLength)
	else:
		notes.append(None)
		durations.append(n.quarterLength)

arrayForRange = list(filter(lambda x: (x != None) , notes))
arrayForRange = list(filter(lambda x: (x != "Start"), arrayForRange))
print(arrayForRange)
yLow = min(arrayForRange) - 1
yHigh = max(arrayForRange) + 1



for i in range(len(durations)):
	sum += durations[i]
	positions.append(sum)

positions.pop(0)
notes[0] = 0
# print(positions)
# print(e.offset for e in firstMelody)

plt.step(positions, notes)
plt.ylim(yLow, yHigh)
plt.show()

