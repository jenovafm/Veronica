from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.bang$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("DASAR KAU")
        sleep(2)
        await e.edit("BANGSAT")
        sleep(2)
        await e.edit("KONTOL")
        sleep(2)
        await e.edit("MEMEK")
        sleep(2)
        await e.edit("ANAK HARAM")
        sleep(2)
        await e.edit("ASU ASU ASU")
        sleep(2)
        await e.edit("MAMPUS KAU")
        sleep(2)
        await e.edit("MINTA DI ADOPSI")
        sleep(2)
        await e.edit("SAMA DAJAL")
        sleep(2)
        await e.edit("BIAR GUNA")
        sleep(2)
        await e.edit("DIKIT")
        sleep(2)
        await e.edit("DARI PADA")
        sleep(2)
        await e.edit("KAMU")
        sleep(2)
        await e.edit("SELAMANYA")
        sleep(2)
        await e.edit("JADI BEBAN")
        sleep(2)
        await e.edit("ORTU")
        sleep(1)
        await e.edit("KAMU")
        
@register(outgoing=True, pattern="^.tob$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
      await e.edit("WAHAY CUCUKU")
      sleep(1)
      await e.edit("IGATLAH")
      sleep(1)
      await e.edit("KAU DILAHIRKAN")
      sleep(1)
      await e.edit("BUKAN UNTUK")
      sleep(1)
      await e.edit("HANYA MAKAN SAJA")
      sleep(1)
      await e.edit("DAN MENJADI")
      sleep(1)
      await e.edit("BEBAN KELUARGA")
  

CMD_HELP.update({
    "BANGSAT":
      "\n\nPenjelasan: ini berisi kata kata mutiara yang sangat dalam\
       n\n.tob\
       n\nPenjelasan: Perintah petuah."
})
