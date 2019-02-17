import random
import randomnamegenerator
import homebrew as hb
import fantasyNPCgenerator
import fantasyinstitutiongenerator

#The output is an object with seven keys output["name"], output["age"], output["characteristic"], output["trait"], output["occupation"], output["gender"], output["secret"]
 
with open("medievalsettlementproblem.txt", encoding='latin-1') as f:
    problemlist = f.read().splitlines() 
 
with open("fantasysettlementproblem.txt", encoding='latin-1') as f:
    problemlist += f.read().splitlines() 
	
with open("medievalsettlementasset.txt", encoding='latin-1') as f:
    assetlist = f.read().splitlines() 
	
with open("fantasysettlementasset.txt", encoding='latin-1') as f:
    assetlist += f.read().splitlines() 	
	
with open("medievalsettlementoddity.txt", encoding='latin-1') as f:
    odditylist = f.read().splitlines() 
	
with open("fantasysettlementoddity.txt", encoding='latin-1') as f:
    odditylist += f.read().splitlines() 	
	
with open("medievalsettlementname.txt", encoding='latin-1') as f:
    namelist = f.read().splitlines()
	
councillist = ["religious council", "council of guild leaders", "noble parlement", "magic council", "mixed council"]

counciladjectivelist = ["A bickering", "A cruel", "A weak", "A greedy", "A wise", "An eccentric",\
	"A confusing", "A brutal", "A cunning", "A stern", "A secretive", "A drunkard", "A zealous",\
	"A fanatical", "A pious", "A chaotic", "A methodical"]
	
rulerlist = ["Despot", "Elder", "Mayor", "Druid", "Commander", "Merchants", "Hight priest", "Crime lord", "Lord", "Count"]
	
	
def main(size = 0):
# Generates a random settlement from tables and RNGs, the output is an object
#The input selects the size 0: Random, 1:Outpost, 2:Village, 3:Town, 4:City

	output = {}

	if size == 0:
		rand = random.random()
		size = 1
		if rand < 0.87:
			size = 2
			if rand < 0.65:
				size = 3
				if rand < 0.30:
					size = 4
					if rand < 0.30:
						size = 5
						
						
	if size == 1:
		output["population"] = random.randint(6, 20)
	elif size == 2:
		output["population"] = random.randint(21, 100)
	elif size == 3:
		output["population"] = random.randint(101, 400)
	elif size == 4:
		output["population"] = random.randint(401, 2500)
	elif size == 5:
		output["population"] = random.randint(2501, 30000)
		
	dummy = ["Outpost", "Hamlet", "Village", "Town", "City"]
	output["size"] = dummy[size-1]	
	
	
	
	if random.random() < 0.65:
		output["name"] = random.choice(namelist)
	else:
		output["name"] = randomnamegenerator.main()
			
	if random.random() < 0.97:			
		output["age"] = random.randint(0, 300) + (size-1) * random.randint(20, 250)
	else:
		output["age"] = "Unknown"
		
	
	
	if random.random() < 0.85:

		output["ruler"] = fantasyNPCgenerator.main(random.choice(rulerlist))
		output["ruler"]["individual"] = True 
		if output["ruler"]["occupation"] == "Elder":
			output["ruler"]["age"] = round(output["ruler"]["age"]/2) + 60
	else:
		output["ruler"] = {}
		output["ruler"]["individual"] = False
		if random.random() < 0.85:
			output["ruler"]["number"] = random.randint(2, 14)
		else:
			output["ruler"]["number"] = random.randint(15, 30)
		if output["ruler"]["number"] > output["population"]/2:
			output["ruler"]["number"] = round(output["population"]/2)
		output["ruler"]["title"] = str(random.choice(councillist))
		output["ruler"]["adjective"] = str(random.choice(counciladjectivelist))
		
	institutionnum = random.randint(1, size)
	output["institutions"] = []
	for i in range(institutionnum):
		output["institutions"].append(fantasyinstitutiongenerator.main())
		output["institutions"][i]["name"] = output["institutions"][i]["name"].replace("@here", output["name"])
		
	output["problem"] = str(random.choice(problemlist))
	output["asset"] = str(random.choice(assetlist))
	output["oddity"] = str(random.choice(odditylist))

	return(output)
   


   

