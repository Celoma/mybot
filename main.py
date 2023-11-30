import discord
from discord.ext import commands
import random
import function

idToken = 'MTE3OTQwOTk1MTM0MTQxMjM3Mg.GQuZPG.G5myc6ZB-wTo4BK9xyE_hJ1LkUnwsLars87Emk'
idServ = 1160897939724566648
idChan = 1179695466250772482
idOwn = 263776530327404554
prefix = '$'


intents = discord.Intents().all()
intents.message_content = True

client = commands.Bot(command_prefix=prefix, intents=intents)

@client.event
async def on_ready():
    guild = client.get_guild(idServ)
    if guild:
        channel = guild.get_channel(idChan)
        if channel:
            await channel.send("Je suis connecté !", delete_after=5)

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.content == "heil":
        await message.channel.send("Pas cool !", reference=message)
    elif "france" in message.content or "France" in message.content or "Marseillaise" in message.content or "marseillaise" in message.content:
        with open('basic.txt', 'r') as file:
            paroles = file.read().splitlines()
            for ligne in paroles:
                await message.channel.send(ligne)
    elif "quoi" in message.content.lower():
        await message.channel.send("feur", reference=message)
    elif "oui" == message.content:
        await message.channel.send("stiti", reference=message)
    elif "<@1179409951341412372>" in message.content:
        try:
            await message.author.kick()
        except:
            await message.channel.send("Vaillant chevalier tes rôles te sauvent !", reference=message)
    else:
        with open('liste_noir.txt', 'r') as file:
            existing_ids = file.read().splitlines()
        if str(message.author.id) in existing_ids:
            try:
                with open('liste_bienveillante.txt', 'r') as file:
                    words = file.read().splitlines()
                    random_word = random.choice(words)
                    await message.channel.send(f"{message.author.mention}, {random_word}")
            except:
                await message.channel.send("Erreur lors de la sélection d'un mot aléatoire de la liste bienveillante.")


@client.command(name='clear')
async def clear(ctx, amount: int = 10):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Cleared {amount} messages.', delete_after=5)

@client.command(name='add_victime')
async def addVictime(ctx, tag):
    try:
        if tag == 'zizi':
            for member in ctx.message.guild.members:
                    if member.display_name != "Malveillance Max":
                        member_id = str(member.id)
                        with open('liste_noir.txt', 'r') as file:
                            existing_ids = file.read().splitlines()
                        if member_id not in existing_ids:
                            with open('liste_noir.txt', 'a') as file:
                                file.write(member_id + '\n')
                            await ctx.send(f'La victime {member.name} a été ajoutée à la liste noire')
                        else:
                            await ctx.send(f'{member.name} est déjà dans la liste noire.')
                    else:
                        await ctx.send('You do not have permission to use this command.')
        elif ctx.author.guild_permissions.administrator:
            for member in ctx.message.guild.members:
                if member.mention == tag:
                    if member.display_name != "Malveillance Max":
                        member_id = str(member.id)
                        with open('liste_noir.txt', 'r') as file:
                            existing_ids = file.read().splitlines()
                        if member_id not in existing_ids:
                            with open('liste_noir.txt', 'a') as file:
                                file.write(member_id + '\n')
                            await ctx.send(f'La victime {tag} a été ajoutée à la liste noire')
                        else:
                            await ctx.send('Ce membre est déjà dans la liste noire.')
        else:
            await ctx.send('You do not have permission to use this command.')
    except:
        await ctx.send('Please mention a victim like @Celoma#0603')

@client.command(name='show_victime')
async def showVictime(ctx):
    try:
        with open('liste_noir.txt', 'r') as file:
            msg = 'Voici la liste des personnes persécutées : \n'
            existing_ids = file.read().splitlines()
            for member in ctx.message.guild.members:
                if str(member.id) in existing_ids:
                    msg += member.mention + '\n'
            await ctx.send(msg)
    except:
        await ctx.send('You do not have permission to use this command.')


@client.command(name='del_victime')
async def delVictime(ctx, tag):
    try:
        if ctx.author.guild_permissions.administrator:
            for member in ctx.message.guild.members:
                if member.mention == tag:
                    member_id = str(member.id)
                    with open('liste_noir.txt', 'r') as file:
                        existing_ids = file.read().splitlines()

                    if member_id in existing_ids:
                        existing_ids.remove(member_id)
                        with open('liste_noir.txt', 'w') as file:
                            file.write('\n'.join(existing_ids))
                        await ctx.send(f'La victime {tag} a été supprimée de la liste noire', delete_after=5)
                        await ctx.channel.purge(limit=2)
                    else:
                        await ctx.send('Ce membre n\'est pas dans la liste noire.')
        else:
            await ctx.send('Cheh')

    except:
        await ctx.send('Error while removing victim.')

@client.command(name='pardon_victime')
async def pardonVictime(ctx):
    if ctx.author.guild_permissions.administrator:
        with open('liste_noir.txt', 'w') as file:
            file.write('')
            await ctx.send(f'Liste de victime remis à 0')
    else:
        await ctx.send(f'Bah alors ? On pue le seum ??')


@client.command(name='helpme')
async def help(ctx):
    await ctx.send("Voici la liste des différentes fonctions actuellement :\n \
Ne surtout pas me ping !!!! \n \
$add_victime @VICTIM \n \
$del_victime @VICTIM \n \
$pardon_victime \n \
$show_victime \n \
$clear [arg: amount: int = 10] \n \
heil \n \
$generatePendu \n \
Tout message patriotique sera récompensé !")

@client.command(name='generatePendu')
async def pendu(ctx):
    mot = function.choisir_mot()
    print(mot)
    lettres_trouvees = []
    essais = 0

    await ctx.send("Bienvenue dans le jeu du pendu ! Devinez le mot.")

    while essais < 11:
        affichage = function.afficher_mot(mot, lettres_trouvees)
        try:
            await ctx.send(file=discord.File(f'ImagesPendu\image_{essais}.png'))
        except:
            print('error')
        await ctx.send(f"Mot actuel: {affichage}")

        await ctx.send("Devinez une lettre:")
        lettre = await client.wait_for('message', check=lambda message: message.author == ctx.author)
        lettre = lettre.content.upper()
        if lettre in mot:
            lettres_trouvees.append(lettre)
            if set(lettres_trouvees) == set(mot) or lettre == mot.upper():
                await ctx.send(f"Félicitations, vous avez trouvé le mot : {mot} !")
                await ctx.send(file=discord.File('ImagesPendu\image_12.png'))
                break
        else:
            essais += 1

    if essais == 11:
        await ctx.send(f"Désolé, vous avez épuisé tous vos essais. Le mot était : {mot}")
        await ctx.send(file=discord.File('ImagesPendu\image_11.png'))


client.run(idToken)
