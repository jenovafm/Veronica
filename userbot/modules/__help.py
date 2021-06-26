import logging


from userbot import BOT_USERNAME
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.helpme")
async def yardim(event):
    try:
        tgbotusername = BOT_USERNAME
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@UserButt")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Bot tidak berfungsi! Harap setel Token Bot dan Nama Pengguna dengan benar. Module telah dihentikan.`"
            )
    except Exception:
        return await event.edit(
            "`Anda tidak dapat Menggunakan Perintah helpme, Bisa Jadi Grup Ini tidak Mensupport nya (Mungkin Anda Belum Menghidupakan Inline Mode Dan Inline Location Data)`"
        )
