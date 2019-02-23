import discord
from discord.ext import commands
import interface
import homebrew as hb

with open("token.txt", encoding='latin-1') as f:
    TOKEN = f.read() 
	
with open("discordid.txt", encoding='latin-1') as f:
    idnum = f.read()
	
prefixes = hb.rotate(hb.arrayreader("prefixes.txt"))
prefixes[0] = [int(i) for i in prefixes[0]]

with open("helptext.txt", encoding='latin-1') as f:
		helptext = f.read().splitlines() 
	
with open("itemlisttext.txt", encoding='latin-1') as f:
    itemlisttext = f.read().splitlines()
	
def prefix(bot, message): # Function finds the prefix ussed by the guild
	
	prefix = "!"
	if isinstance(message.channel, discord.abc.GuildChannel):
		for n in range(len(prefixes[0])):
			if int(prefixes[0][n-1]) == message.guild.id:
				prefix = int(prefixes[0][n-1])
				prefix = str(prefixes[1][n-1])
			
	return(prefix)	

description = 'placeholder'
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(idnum)
	print('------')
	
	
@bot.command()
async def hi(ctx): # For testing


	output = "Hello there, General " + ctx.message.author.name
	await ctx.send(output)
	
# The most important function, calls interface to generate all the bots content
@bot.command()
async def gen(ctx, arg1  = "nothing was entered0", arg2 = "nothing was entered0", arg3  = "nothing was entered0", arg4  = "nothing was entered0"):

	openoutput, secretoutput = interface.main(ctx, arg1, arg2, arg3, arg4)
	
	if openoutput == secretoutput:
		await ctx.send(openoutput)
	else:
		if isinstance(ctx.message.channel, discord.abc.GuildChannel):
			await ctx.send(openoutput)
			await ctx.message.author.send(secretoutput)
		else:
			await ctx.send(secretoutput)
		
@bot.command()
async def help(ctx):

	output = ""
	for i in helptext:
		output += i + "\n"
		
	output = output.replace("@prefix@", prefix(bot, ctx.message))
		
	await ctx.send(output)
	
# Prints out the list of things that can be generated
@bot.command()	
async def itemlist(ctx):

	output = ""
	for i in itemlisttext:
		output += i + "\n"
		if i == "":
			await ctx.send(output)
			output = ""
		
	await ctx.send(output)
	
@bot.command()	
async def myid(ctx):

	output = ctx.message.author.id
		
	await ctx.send(output)
	
# Allows to change the bot prefix for one server
@bot.command()
async def gbchangeprefix(ctx, arg1):

	if isinstance(ctx.message.channel, discord.abc.GuildChannel):

		for n in range(len(prefixes[0])):
			if int(prefixes[0][n-1]) == ctx.message.guild.id:
				del prefixes[0][n-1]
				del prefixes[1][n-1]
				
		prefixes[0].append(ctx.message.guild.id)
		prefixes[1].append(arg1)
		
		with open("prefixes.txt", "w", encoding='latin-1') as f:
			for n in range(len(prefixes[0])):
				f.write(str(prefixes[0][n-1]) + ";" + str(prefixes[1][n-1] + "\n"))

		output = "prefix changed to \"" + arg1 + "\" for this server."
		
	else:
	
		output = "This hasn't been implemented for private messages. "
		
	await ctx.send(output)

# Terminated the bot, can only be called by the id in "discordid.txt"
@bot.command()	
async def kill(ctx, arg = 0):


	if ctx.message.author.id == int(idnum):
		await ctx.send("Bot terminated.")
		print("Bot terminated.")
		await bot.logout()
	else:
		await ctx.send("You are not the chossen one.")
	
bot.run(TOKEN)
	
