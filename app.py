import time
import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.default()  # Подключаем "Разрешения"
intents.message_content = True
# Задаём префикс и интенты
bot = commands.Bot(command_prefix='/', intents=intents)


# подключение и отключение к голосовому
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()

        await ctx.voice_client.disconnect()
    return


# звук звонка в голосовой канал
@bot.command()
async def bell(ctx):
    voice_channel = ctx.message.author.voice.channel
    await voice_channel.connect()
    channel = ctx.message.guild.voice_client

    audio_file = f'zvonok.mp3'
    if not os.path.isfile(audio_file):
        await ctx.send(f"Файл не найден.")
        return
    source = discord.FFmpegPCMAudio(audio_file)
    channel.play(source)

    await asyncio.sleep(4)
    await ctx.voice_client.disconnect()
    return


# настраиваемое расписание
@bot.command()
async def schedule(ctx, work_time, break_time, quantity):
    await ctx.send(
        f'Длительность работы:{work_time}\nДлительность перерыва:{break_time}\nКолличество сессий:{quantity}')
    work_time = int(work_time)
    break_time = int(break_time)
    quantity = int(quantity)
    s = 0

    while quantity > s:
        await ctx.send('Начало занятий')
        # Подключение ,звонок,отключение
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()
        channel = ctx.message.guild.voice_client

        audio_file = f'zvonok.mp3'
        if not os.path.isfile(audio_file):
            await ctx.send(f"Файл не найден.")
            return
        source = discord.FFmpegPCMAudio(audio_file)
        channel.play(source)
        await asyncio.sleep(4)
        await ctx.voice_client.disconnect()
        time.sleep(work_time)

        await ctx.send('Перерыв')
        # Подключение ,звонок,отключение
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()
        channel = ctx.message.guild.voice_client

        audio_file = f'zvonok.mp3'
        if not os.path.isfile(audio_file):
            await ctx.send(f"Файл не найден.")
            return
        source = discord.FFmpegPCMAudio(audio_file)
        channel.play(source)
        await asyncio.sleep(4)
        await ctx.voice_client.disconnect()
        time.sleep(break_time)
        s += 1

    await ctx.send('Запланированные занятия завершены')
    return
bot.run('TOKEN_DISCORD_BOT')