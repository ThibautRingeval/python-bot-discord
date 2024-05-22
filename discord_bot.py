import discord #import du module
from discord.ext import commands
import random
#Intents
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
intents.message_content = True
# guilds = serveurs discords
intents.guilds = True
intents.members = True
# fonction "on_ready" pour confirmer la bonne connexion du bot sur votre serveur

# fonction pour montrer qu'un bot est bien connecté
@bot.event
async def on_ready():
    print (f"{bot.user.name} s'est bien connecté !")
    
# fonction "on_message"
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

#fonction ping pour le bot
    if message.content.startswith('!ping'):
        await message.channel.send('pong')
        
#fonction pour le bot saluer + conversation avec le bot
    elif message.content.startswith('Salut'):
        await message.channel.send('Salut ! ça va ?')
    elif message.content.startswith('Ça va bien'):
        await message.channel.send('Cool, super !')
    elif message.content.startswith('Ça va pas bien'):
        await message.channel.send('Pas cool, pas super :sob: !')
    elif message.content.startswith('ahahah'):
        await message.channel.send('hihihi')
        
#fonction members pour voir les membres du serveur et les roles
    elif message.content.startswith('!members'):
        guild = message.guild
        members = guild.members
        member_list = []
        for member in members:
            emoji = random.choice(["👑", "🤖", "🎉", "🎁"])
            pseudonym = f"{member.name}_#{member.discriminator}"
            role = member.top_role.name if member.top_role else "None"
            member_list.append(f"{emoji} {pseudonym} ({role})")
        await message.channel.send('\n'.join(member_list))
        
#fonction jokes pour le bot pour faire des blagues
    elif message.content.startswith('!joke'):
        await message.channel.send(random.choice(jokes))
        
jokes = [
    "Comment appelle-t-on une chauve-souris avec une perruque ?",
    "Une souris.",
]

jokes = [
    "C'est l'histoire du ptit dej, tu la connais ?",
    "Pas de bol.",
]
    #connexion du bot au serveur avec au token
bot.run("TOKEN")