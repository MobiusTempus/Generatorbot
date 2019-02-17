import fantasyNPCgenerator
import randomnamegenerator
import missiongenerator
import inngenerator
import fantasyinngenerator
import fantasysettlementgenerator
import numpy as np

with open("femalename.txt", encoding='latin-1') as f:
    femalenamelist = f.read().splitlines() 	
	
with open("medievalfemalename.txt", encoding='latin-1') as f:
    medievalfemalenamelist = f.read().splitlines() 
	
with open("malename.txt", encoding='latin-1') as f:
    malenamelist = f.read().splitlines() 	
	
with open("medievalmalename.txt", encoding='latin-1') as f:
    medievalmalenamelist = f.read().splitlines() 
	
with open("surname.txt", encoding='latin-1') as f:
    surnamelist = f.read().splitlines() 	
	
with open("medievalsurname.txt", encoding='latin-1') as f:
    medievalsurnamelist = f.read().splitlines() 

def main(ctx, arg1, arg2, arg3, arg4):

	if arg1 == "randomname" or arg1 == "rname":
		openoutput = randomnamegenerator.main()
		
	elif arg1 == "malename" or arg1 == "mname":
		openoutput = np.random.choice(malenamelist)
		
	elif arg1 == "femalename" or arg1 == "fname":
		openoutput = np.random.choice(femalenamelist)
		
	elif arg1 == "surname" or arg1 == "sname":
		openoutput = np.random.choice(surnamelist)
		
	elif arg1 == "fantasyNPC" or arg1 == "fNPC":
		#Generates a fantasy NPC.
		if arg2 == "nothing was entered0":
			NPC = fantasyNPCgenerator.main()
		else: 
			NPC = fantasyNPCgenerator.main(arg2)
		output = "Name: " + NPC["name"] + "\nGender: " + NPC["gender"] + "\nAge: " + str(int(NPC["age"]))  \
			 + "\nOccupation: " + str(NPC["occupation"]) + "\nCharacteristic: " + NPC["characteristic"]
		openoutput = output
		
		output += "\nTrait: " + NPC["trait"] 
		
		dummy =  NPC["secret"]
		if str(dummy) != str("Has no secret"):
			output += "\nSecret: " + dummy
			
		secretoutput = output
		
	elif arg1 == "fantasyinn" or arg1 == "finn" or arg1 == "inn":
		inn = fantasyinngenerator.main()
		output = "__**Inn**__\nName: " + inn["name"] + "\nOddity: " + inn["oddity"]   \
			 + "\nSpeciality: " + inn["specialty"]
		openoutput = output
		
		output += "\nSecret: " + inn["secret"]
		secretoutput = output
		
		owner = fantasyNPCgenerator.main("Innkeeper")
		waiter = fantasyNPCgenerator.main("Waiter")
		
		openoutput += "\n\n**Owner**\nName: " + owner["name"] + "\nGender: " + owner["gender"] + "\nAge: " \
		+ str(int(owner["age"])) + "\nOccupation: " + str(owner["occupation"]) + "\nCharacteristic: " \
		+ owner["characteristic"]
		openoutput += "\n\n**Waiter**\nName: " + waiter["name"] + "\nGender: " + waiter["gender"] + "\nAge: " \
		+ str(int(waiter["age"])) + "\nOccupation: " + str(waiter["occupation"]) + "\nCharacteristic: " \
		+ waiter["characteristic"]
		secretoutput += "\n\n**Owner**\nName: " + owner["name"] + "\nGender: " + owner["gender"] + "\nAge: " \
		+ str(int(owner["age"])) + "\nOccupation: " + str(owner["occupation"]) + "\nCharacteristic: " \
		+ owner["characteristic"] + "\nTrait: " + owner["trait"] + "\nSecret: " + owner["secret"]
		secretoutput += "\n\n**Waiter**\nName: " + waiter["name"] + "\nGender: " + waiter["gender"] + "\nAge: " \
		+ str(int(waiter["age"])) + "\nOccupation: " + str(waiter["occupation"]) + "\nCharacteristic: " \
		+ waiter["characteristic"]+ "\nTrait: " + waiter["trait"] + "\nSecret: " + waiter["secret"]
		
	elif arg1 == "mission" or arg1 == "mis" or arg1 == "m":
			#Generates a mission.
			
		if arg2 == "nothing was entered0":
			mission = missiongenerator.main()
		else:
			mission = missiongenerator.main(int(arg2))
		
		output = "Difficulty: " + str(mission["difficulty"]) + "\nObjective: \n"
		i = 1
		while i < len(mission["objectives"]):
			output += "   * " + mission["objectives"][i-1] + "\n"
			i += 1
		
		output += "Reward: " + str(mission["reward"]) + "\nComplications: \n" 
		if len(mission["opencompications"]) > 0:
			i = 1
			while i < len(mission["opencompications"]):
				output += "   * " + mission["opencompications"][i-1] + "\n"
				i += 1
		openoutput = output

		if len(mission["secretcompications"]) > 0:	
			output += "Secret complications: \n"
			i = 1
			while i < len(mission["secretcompications"]):
				output += "   * " + mission["secretcompications"][i-1] + "\n"
				i += 1
		secretoutput = output
		
	elif arg1 == "jobboard" or arg1 == "jb":
	
		if arg2 == "nothing was entered0":
			arg2 = 5
			
		openoutput = "__Job Board__\n\n"
		secretoutput = "__Job Board__\n\n"
	
		k = 0
		while k < int(arg2):
			k += 1
			
			
			mission = missiongenerator.main()
			
			output = "\n__Job: " + str(k) + "/" + str(arg2) + "__\nDifficulty: " + str(mission["difficulty"]) + "\nObjective: \n"
			i = 0
			while i < len(mission["objectives"]):
				output += "   * " + mission["objectives"][i] + "\n"
				i += 1
			
			output += "Reward: " + str(mission["reward"]) + "\nComplications: \n" 
			if len(mission["opencompications"]) > 0:
				i = 0
				while i < len(mission["opencompications"]):
					output += "   * " + mission["opencompications"][i] + "\n"
					i += 1
			openoutput += output
			
			if len(mission["secretcompications"]) > 0:	
				output += "Secret complications: \n"
				i = 0
				while i < len(mission["secretcompications"]):
					output += "   * " + mission["secretcompications"][i] + "\n"
					i += 1
			secretoutput += output
			output = ""
			
	elif arg1 == "fantasysettlement" or arg1 == "fsettlement" or arg1 == "fset": #fantasy settlement
		if arg2 == "nothing was entered0":
			arg2 = 0
			
		openoutput, secretoutput = fantasysettlementformat(fantasysettlementgenerator.main(arg2))
		
	elif arg1 == "fantasyoutpost" or arg1 == "foutpost": #fantasy outpost
			
		openoutput, secretoutput = fantasysettlementformat(fantasysettlementgenerator.main(1))

	elif arg1 == "fantasyhamlet" or arg1 == "fhamlet": #fantasy hamlet
			
		openoutput, secretoutput = fantasysettlementformat(fantasysettlementgenerator.main(2))
		
	elif arg1 == "fantasyvillage" or arg1 == "fvillage": #fantasy village
			
		openoutput, secretoutput = fantasysettlementformat(fantasysettlementgenerator.main(3))
		
	elif arg1 == "fantasytown" or arg1 == "ftown": #fantasy town
			
		openoutput, secretoutput = fantasysettlementformat(fantasysettlementgenerator.main(4))
		
	elif arg1 == "fantasyvcity" or arg1 == "fcity": #fantasy city
			
		openoutput, secretoutput = fantasysettlementformat(fantasysettlementgenerator.main(5))

			
			
					
		
	# end of generator
	elif arg1 == "nothing was entered0":
		openoutput = "There must be an argument after gen, use !itemlist to get a list"
		
	else:
		openoutput = arg1 + " is not a valid generator argument, use !itemlist to get a list"
		
	try: secretoutput
	except NameError: secretoutput = openoutput
	
	return(openoutput, secretoutput)
	
def charaformat(character):

	output = "Name: " + character["name"] + "\nGender: " + character["gender"]
	output += "\nAge: " + str(int(character["age"])) + "\nOccupation: "  \
		 + str(character["occupation"]) + "\nCharacteristic: " + character["characteristic"]
		 
	openoutput = output
	
	output += "\nTrait: " + character["trait"] 
	
	dummy =  character["secret"]
	if str(dummy) != str("Has no secret"):
		output += "\nSecret: " + dummy
		
	secretoutput = output
	
	return(openoutput, secretoutput)
	
def secretcharaformat(character):

	output = "Name: " + character["name"] + "\nGender: " + character["gender"]
	output += "\nAge: " + str(int(character["age"]))
	if character["occupationgenerated"]:
		output += "\nOccupation: " + str(character["occupation"])
	output += "\nCharacteristic: " + character["characteristic"]	
	output += "\nTrait: " + character["trait"] 
	
	dummy =  character["secret"]
	if str(dummy) != str("Has no secret"):
		output += "\nSecret: " + dummy
		
	secretoutput = output
	
	return(secretoutput)
	
def fantasysettlementformat(settlement):
	
	# general settlement stuff
		
	output = "__**" + settlement["size"] + "**__\n"
	output += "Name: " + settlement["name"] + "\n"
	output += "Population: " + str(settlement["population"]) + "\n"
	
	openoutput = output
	
	output += "Age: " + str(settlement["age"]) + "\n"
	
	secretoutput = output
	
	output = "Asset: " + settlement["asset"] + "\n"
	output += "Oddity: " + settlement["oddity"] + "\n"

	
	openoutput += output + "\n"
	
	output += "Problem: " + settlement["problem"] + "\n"
	
	secretoutput += output + "\n"	
	
	# Ruler stuff
	
	output = "**Ruler**\n"
	
	if settlement["ruler"]["individual"]:
		output += "Name: " + settlement["ruler"]["name"] + "\n"
		output += "Gendre: " + settlement["ruler"]["gender"] + "\n"
		output += "Title: " + settlement["ruler"]["occupation"] + "\n"
		
		openoutput += output + "\n"
		
		output += "Age: " + str(settlement["ruler"]["age"]) + "\n"	
		output += "Characteristic: " + settlement["ruler"]["characteristic"] + "\n"
		output += "Trait: " + settlement["ruler"]["trait"] + "\n"
		if str(settlement["ruler"]["secret"]) != str("Has no secret"):
			output += "Secret: " + settlement["ruler"]["secret"] + "\n"
			
		secretoutput += output + "\n"
		
	else:
		output += settlement["ruler"]["adjective"] + " " + settlement["ruler"]["title"]
		output += "\nNumber of membres: " + str(settlement["ruler"]["number"])
		
		openoutput += output + "\n\n"
		secretoutput += output + "\n\n"
		
	# Institutions
	
	output = "**Institutions**"
	
	for institution in settlement["institutions"]:
		output += "\n\n**" + institution["discriptor"] + "**\n"
		output += "Name: " + institution["name"]
		
		openoutput += output + "\n"
		secretoutput += output
		output = ""
		
		if institution["identifier"] == 1 or institution["identifier"] == 2: #inn/tavern
		
			output += "\nOddity: " + institution["oddity"]   \
				 + "\nSpeciality: " + institution["specialty"]				
			output += "\nSecret: " + institution["secret"]		
			
			owner = fantasyNPCgenerator.main("Owner")
			waiter = fantasyNPCgenerator.main("Waiter")
			
			secretoutput += "\n\n**Owner**\n" + secretcharaformat(owner)
			secretoutput += "\n\n**Waiter**\n" + secretcharaformat(waiter)
		
		elif institution["identifier"] == 3: #trading post
	
			secretoutput += "\nFood vendors:\n"
			for vendor in institution["food"]:
				secretoutput += "    " + vendor + "\n"
				
			secretoutput += "Smell: " + institution["smell"]
			
		elif institution["identifier"] == 4: #Temple
		
			secretoutput += "\nPrincipal succour: " + institution["succour"] + "\n"
			
			highpriest = fantasyNPCgenerator.main("High priest")
			
			secretoutput += "\n**High priest**\n" + secretcharaformat(highpriest)
			
		elif institution["identifier"] == 5: #Library
		
			secretoutput += "\nAreas of focus:\n"
			for discipline in institution["disciplines"]:
				secretoutput += "    " + discipline + "\n"
				
			librarian = fantasyNPCgenerator.main("Librarian")
			
			secretoutput += "\n**Librarian**\n" + secretcharaformat(librarian)
				
		elif institution["identifier"] == 6: #University
		
			secretoutput += "\nClasses taught:\n"
			for discipline in institution["disciplines"]:
				secretoutput += "    " + discipline + "\n"
				
			dean = fantasyNPCgenerator.main("Dean")
			
			secretoutput += "\n**Dean**\n" + secretcharaformat(dean)
			
	return(openoutput, secretoutput)