from music21 import *

# connect to local corpus
corpus.addPath('/Users/nathansepulveda/Desktop/TEST')

# define the local corpora 
localCorpus = corpus.corpora.LocalCorpus()



# make into a list
listOfWorks = localCorpus.getPaths()


for work in listOfWorks:
  print(work)
  work = str(work)
  work = work.split("TEST/")[1]
  t = work.split(".")[0]
  work = corpus.parse(work)
  p = graph.plot.HistogramPitchClass(work, title = t,)
  p.run()
  work.show()
  


