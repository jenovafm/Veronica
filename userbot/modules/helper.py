""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Kaisar {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/kenkanasw)"
        "\n[Repo](https://github.com/kenkannih/Kaisar-userbot)"
        "\n[Instagram](Instagram.com/kenkanasw_)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/kenkannih/Kaisar-userbot/Kaisar-userbot/varshelper.txt)")


CMD_HELP.update({
    "Kaisarhelper":
    "`.Kaisarhelp`\
\nPenjelasan: Bantuan Untuk Kaisar-userbot.\
\n`.Kaisarvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
