import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from threading import Thread
from flask import Flask

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Setup intents and bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Discord bot events
@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

# Flask server setup
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Start Flask server in a separate thread
Thread(target=run_flask).start()

# Run the Discord bot
bot.run(DISCORD_TOKEN)
