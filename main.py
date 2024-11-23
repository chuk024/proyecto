import discord
from discord.ext import commands
from model import get_class
import os, random
import requests

intents = discord.intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$",intents=intents)

@bot.event
async def on_ready():
    print(f'Te has logueado como {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="./labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("no has subido ninguna imagen")

bot.run("MTI1MDYzMjU5ODQ4MTI3Njk0OA.GK4xk1.qNvAu20FWVapVhJQLUJdjwX56TQbPqONy1WEGI")