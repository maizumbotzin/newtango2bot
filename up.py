from pathlib import Path
import os
class Config:
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = os.environ.get('API_HASH')
    BOT_TOKEN2 = os.environ.get('BOT_TOKEN2')
    CHATID = int(os.environ.get('CANAL_Sendvideo'))

import secrets
import argparse
parser = argparse.ArgumentParser(description = 'test')
parser.add_argument('--nomedoarquivo', action = 'store', dest = 'nomedoarquivo',default = 'WORK', required = True,help = 'Nome do aquivo de video')
parser.add_argument('--legenda', action = 'store', dest = 'legenda',default = 'WORK', required = True,help = 'legendadoarquivo')
parser.add_argument('--photo', action = 'store', dest = 'photo',default = 'WORK', required = True,help = 'photo')
parser.add_argument('--photo2', action = 'store', dest = 'photo2',default = 'WORK', required = True,help = 'photo2')
arguments = parser.parse_args()



import asyncio
from telethon import TelegramClient, sync
from telethon.tl.types import DocumentAttributeVideo
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
usuario = secrets.token_hex(15)
#Dados Telegram:
client = TelegramClient(f'bot{usuario}', Config.API_ID, api_hash=Config.API_HASH).start(bot_token=Config.BOT_TOKEN2)

# duração video:
file_name = ('{}'.format(arguments.nomedoarquivo))
Duracao_video = extractMetadata(createParser(file_name))
duration = Duracao_video.get('duration').seconds

# imagem dimensões:
file_foto = ('{}'.format(arguments.photo))
Dimensao_Imagem = extractMetadata(createParser(file_foto))


try:
    async def main():
        file = await client.upload_file(file_name)
        await client.send_file(Config.CHATID,file,thumb=f'{arguments.photo}',caption=f'{arguments.legenda}',use_cache=False,attributes=(DocumentAttributeVideo((0, Duracao_video.get('duration').seconds)[Duracao_video.has('duration')],(0, Dimensao_Imagem.get('width'))[Dimensao_Imagem.has('width')],(0, Dimensao_Imagem.get('height'))[Dimensao_Imagem.has('height')],supports_streaming=True),))
        await client.send_file(Config.CHATID, f'{arguments.photo2}' , caption=f'{arguments.legenda}')
        os.system(f'(rm {arguments.nomedoarquivo} && rm {arguments.photo} && rm {arguments.photo2})&')
except:
    pass
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
