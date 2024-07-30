import os
import discord
from discord.ext import commands
from random import choice

from myserver import server_on



# สามารถเพิ่มคำเรื้อนๆได้
leprosy_word = [
	"ควยไรเย็ดแม่",
	"มึงกับกูที่ไหนก็ได้",
	"ไม่ได้ตึงหรอกไอโง่",
	"กูเห็นแม่มึงขายหีอยู่สลัมจริงไหม",
	"อย่าเอ๋อไอสัส",
	"ไหวปาวไอเอ๋อ",
	"โง่",
	"สมเพช",
	"ควาย",
	"ไอ้เสี่ยวขี้เฟคอีดอกกระหรี่",
	"ไอ้บ้านนอก",
	"แม่มึงอะ",
	"ไอ่หำน้อย",
	"ไอ่ลูกตุ๊ด",
	"พ่อมึงตาย"
]

channel_id = "1265942533960110091" # <-- ใส่ไอดีห้องสำหรับให้บอทเรื้อน

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents = intents)

@bot.event
async def on_ready():
	print("Bot is ready !")
	
	
@bot.event
async def on_message(message):
	if (str(message.channel.id) == f"{channel_id}"):
		if message.author.id == bot.user.id:
			pass
		else:
			random_words = choice(leprosy_word) # <-- สุ่มคำใน List ที่เราเก็บไว้
			await message.reply(random_words) # <-- ส่งข้อความที่สุ่มได้ถึงผู้เขียน

server_on()

bot.run(os.getenv('TOKE'))