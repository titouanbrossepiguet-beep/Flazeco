import discord
from discord.ext import commands
from flask import Flask
import threading
import os

# --- Flask pour garder le bot actif sur Render ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# --- Discord Bot ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Connecté en tant que {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong ! Le bot fonctionne !")

keep_alive()

# --- Lancement du bot ---
TOKEN = os.environ['DISCORD_BOT_TOKEN']  # 🔒 Token stocké sur Render
bot.run(TOKEN)
