""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hi, {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Instagram](http://instagram.com/jenovafm)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://instagram.com/jenovafm)")


CMD_HELP.update({
    "VeronicaAssistanthelper":
    "`.VeronicaAssistanthelp`\
\nPenjelasan: Bantuan Untuk VeronicaAssistant.\
\n`.VeronicaAssistantvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
