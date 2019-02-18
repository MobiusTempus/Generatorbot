import discord
from discord.ext import commands
import interface

with open("token.txt", encoding='latin-1') as f:
    TOKEN = f.read() 
	
with open("discordid.txt", encoding='latin-1') as f:
    idnum = f.read()
	
	

with open("helptext.txt") as f:
    helptext = f.read().splitlines() 
	
with open("itemlisttext.txt") as f:
    itemlisttext = f.read().splitlines() 

description = 'placeholder'
bot = commands.Bot(command_prefix='!', description=description)
bot.remove_command("help")


@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print(idnum)
	print('------')
	
	
@bot.command(pass_context=True)
async def hi(ctx):


	output = "Hello there, General " + ctx.message.author.name
	await bot.say(output)
	
@bot.command(pass_context=True)
async def gen(ctx, arg1  = "nothing was entered0", arg2 = "nothing was entered0", arg3  = "nothing was entered0", arg4  = "nothing was entered0"):

	openoutput, secretoutput = interface.main(ctx, arg1, arg2, arg3, arg4)
	
	if openoutput == secretoutput:
		await bot.say(openoutput)
	else:
		if ctx.message.channel.is_private:
			await bot.send_message(ctx.message.author, secretoutput)
		else:
			await bot.say(openoutput)
			await bot.send_message(ctx.message.author, secretoutput)
		
@bot.command(pass_context=True)
async def help(ctx):

	output = ""
	for i in helptext:
		output += i + "\n"
		
	await bot.say(output)
	
@bot.command(pass_context=True)	
async def itemlist(ctx):

	output = ""
	for i in itemlisttext:
		output += i + "\n"
		if i == "":
			await bot.say(output)
			output = ""
		
	await bot.say(output)
	
@bot.command(pass_context=True)	
async def myid(ctx):

	output = ctx.message.author.id
		
	await bot.say(output)

@bot.command(pass_context=True)		
async def kill(ctx, arg = 0):


	if ctx.message.author.id == str(idnum):
		await bot.say("Bot terminated.")
		print("Bot terminated.")
		await bot.logout()
	else:
		await bot.say("You are not the chossen one.")
	
bot.run(TOKEN)
	
