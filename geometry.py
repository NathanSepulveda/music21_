from music21 import *
import matplotlib.pyplot as plt



corpus.addPath('/Users/nathansepulveda/Desktop/TEST')

sadness = corpus.parse("Sadness.xml")
cello = sadness.getElementById("Inst 2")
measureStart = int(input("Start"))
measureEnd = int(input("End"))

print(measureStart)

firstMelody = cello.measures(measureStart, measureEnd).stripTies()
t = firstMelody.quantize([4], processOffsets=True, processDurations=True, inPlace=False)

# print([e.offset for e in t])
# firstMelody.show()


durations = [0]
notes = ["Start"]
positions = [0]
sum = 0

for n in firstMelody.notes.flat:
	notes.append(str(n.pitch))
	durations.append(n.quarterLength)

for i in range(len(durations)):
	sum += durations[i]
	positions.append(sum)

positions.pop(0)
# print(positions)
# print(e.offset for e in firstMelody)

plt.step(positions, notes)
plt.show()

