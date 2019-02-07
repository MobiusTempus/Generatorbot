# Generates missions using tables, they include objectives, expected complications and unexpected complications.
import random
import numpy as np
import homebrew as hb

def main(difficulty = 0):

	objectivelist = hb.rotate(hb.arrayreader("missionobjectives.txt"))
	objectivelist[1] = [float(i) for i in objectivelist[1]]

	#The complications has four rows, name, relative probability of expected complication, relative probability of unexpected complication, reward multiplier .
	complicationlist = hb.rotate(hb.arrayreader("missioncomplications.txt"))
	j=1
	while j < 3:
		compicationlist[j] = [float(i) for i in compicationlist[j]]
		j += 1
		
	if difficulty == 0:
		difficulty = round(np.random.triangular(0.6, 0.6, 10.5))
	reward = random.randint(8, 12) * 4**difficulty * 10

	objectivenum = 1
	objectivenum += round((random.random()*difficulty/3))

	objectives = []
	while len(objectives) < objectivenum:
		objectivelist[1] = hb.normalise(objectivelist[1])
		dumb = np.random.choice(objectivelist[0], p=objectivelist[1])
		index = objectivelist[0].index(dumb)
		objectives.append(dumb)
		objectivelist = hb.arraycleaner(objectivelist, index)
		

	opencompicationnum = random.randint(0, 2) + round((random.random()*difficulty/4))
	
	opencomplications = []
	while len(opencomplications) < opencompicationnum:
		compicationlist[1] = hb.normalise(compicationlist[1])
		dumb = np.random.choice(compicationlist[0], p=compicationlist[1])
		index = compicationlist[0].index(dumb)
		opencomplications.append(dumb)
		reward *= float(compicationlist[3][index])
		compicationlist = hb.arraycleaner(compicationlist, index)
		
		
	secretcompicationnum = random.randint(0, 2) + round((random.random()*difficulty/4))
	
	secretcomplications = []
	while len(secretcomplications) < secretcompicationnum:
		compicationlist[2] = hb.normalise(compicationlist[2])
		dumb = np.random.choice(compicationlist[0], p=compicationlist[2])
		index = compicationlist[0].index(dumb)
		secretcomplications.append(dumb)
		reward *= float(compicationlist[3][index])
		compicationlist = hb.arraycleaner(compicationlist, index)
		
	reward = hb.sigfig(reward,2)
	
	output = {}
	output["difficulty"] = difficulty
	output["objectives"] = objectives
	output["reward"] = reward
	output["opencomplications"] = opencomplications
	output["secretcomplications"] = secretcomplications
	
	
	return(output)
