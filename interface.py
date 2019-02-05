import fantasyNPCgenerator
import randomnamegenerator
import missiongenerator
import inngenerator
import fantasyinngenerator
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
		
		output += "\nTrait: " + NPC["trait"] + "\nSecret: " + NPC["secret"]
		secretoutput = output
		
	elif arg1 == "fantasyinn" or arg1 == "finn" or arg1 == "inn":
		inn = fantasyinngenerator.main()
		output = "__Inn__\nName: " + inn["name"] + "\nOddity: " + inn["oddity"]   \
			 + "\nSpeciality: " + inn["specialty"]
		openoutput = output
		
		output += "\nSecret: " + inn["secret"]
		secretoutput = output
		
		owner = fantasyNPCgenerator.main("Innkeeper")
		waiter = fantasyNPCgenerator.main("Waiter")
		
		openoutput += "\n\n__Owner__\nName: " + owner["name"] + "\nGender: " + owner["gender"] + "\nAge: " \
		+ str(int(owner["age"])) + "\nOccupation: " + str(owner["occupation"]) + "\nCharacteristic: " \
		+ owner["characteristic"]
		openoutput += "\n\n__Waiter__\nName: " + waiter["name"] + "\nGender: " + waiter["gender"] + "\nAge: " \
		+ str(int(waiter["age"])) + "\nOccupation: " + str(waiter["occupation"]) + "\nCharacteristic: " \
		+ waiter["characteristic"]
		secretoutput += "\n\n__Owner__\nName: " + owner["name"] + "\nGender: " + owner["gender"] + "\nAge: " \
		+ str(int(owner["age"])) + "\nOccupation: " + str(owner["occupation"]) + "\nCharacteristic: " \
		+ owner["characteristic"] + "\nTrait: " + owner["trait"] + "\nSecret: " + owner["secret"]
		secretoutput += "\n\n__Waiter__\nName: " + waiter["name"] + "\nGender: " + waiter["gender"] + "\nAge: " \
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
		
		
		
	# end of generator
	elif arg1 == "nothing was entered0":
		openoutput = "There must be an argument after gen, use !help gen to get a list"
		
	else:
		openoutput = arg1 + " is not a valid generator argument, use !help gen to get a list"
		
	try: secretoutput
	except NameError: secretoutput = openoutput
	
	return(openoutput, secretoutput)