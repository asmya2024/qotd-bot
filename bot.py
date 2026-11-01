import os
import discord
from discord.ext import tasks, commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

domande = [
    "Qual è il tuo gioco preferito di tutti i tempi e perché?",
    "Se potessi avere un superpotere per un giorno, quale sceglieresti?",
    "Qual è il cibo che potresti mangiare per il resto della tua vita senza stancarti mai?",
    "Se potessi viaggiare in qualsiasi epoca storica, dove andresti?",
    "Qual è il film o la serie TV che hai rivisto più volte?",
    "Qual è la tua canzone preferita del momento?",
    "Se potessi vivere in un universo di un videogioco, quale sceglieresti?"
    "Qual è il tuo gioco preferito di tutti i tempi e perché?",
    "Se potessi avere un superpotere per un giorno, quale sceglieresti?",
    "Qual è il cibo che potresti mangiare per il resto della tua vita senza stancarti mai?",
    "Se potessi viaggiare in qualsiasi epoca storica, dove andresti?",
    "Qual è il film o la serie TV che hai rivisto più volte?"
]

@bot.event
async def on_ready():
    print(f'Bot connesso come {bot.user}!')
    if not invia_domanda.is_running():
        invia_domanda.start()

@tasks.loop(hours=24)
async def invia_domanda():
    try:
        canale = await bot.fetch_channel(1561278288603779192)
        domanda = random.choice(domande)
        embed = discord.Embed(
            title="Domanda del Giorno!",
            description=domanda,
            color=discord.Color.blue()
        )
        embed.set_footer(text="Rispondi qua sotto nei commenti!")
        await canale.send(embed=embed)
    except Exception as e:
        print(f"Errore nell'invio del messaggio: {e}")
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)
