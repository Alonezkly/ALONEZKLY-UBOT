# Port By @VckyouuBitch From GeezProject

from telethon import utils
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID, InputStickerSetShortName

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.sspam (.*)")
async def _(e):
    geez = await e.get_reply_message()
    if not (geez and geez.media("document")):
        return await e.edit("`Reply To Sticker Only`")
    set = geez.document.attributes[1]
    sset = await bot(
        GetStickerSetRequest(
            InputStickerSetID(
                id=set.stickerset.id,
                access_hash=set.stickerset.access_hash,
            )
        )
    )
    pack = sset.set.short_name
    docs = [
        utils.get_input_document(geez)
        for geez in (
            await bot(GetStickerSetRequest(InputStickerSetShortName(pack)))
        ).documents
    ]
    for xx in docs:
        await bot(file=(xx))


CMD_HELP.update({"sspam": "\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sspam` <Reply on Sticker>"
                 "\n↳ : Balas Pesan Ke sticker."})
