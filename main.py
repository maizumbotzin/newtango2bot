import os
from pathlib import Path
import secrets
class Config:
    TaskId = int(os.environ.get('TaskId'))
    Digest = os.environ.get('Digest')
    Auth_Token = os.environ.get('Auth_Token')
    Bot_token = os.environ.get('BOT_TOKEN1')
    chatid = int(os.environ.get('CANALID'))

import requests
import re
import telepot
import time

# dados da conta direto no heroku
TangoMe_TaskId =Config.TaskId # tango taskid
Tango_Auth_Token =Config.Auth_Token # tango Auth_Token
Tango_Digest=Config.Digest # tango Digest
chatid=Config.chatid # chat ID CANAL
Bot_token=Config.Bot_token
#####################################################

bot=telepot.Bot(Bot_token)
jaenviados=[]
def loading():
  while True:
    time.sleep(5)
    headers = {'Host': 'stream.tango.me','Accept': '*/*','TangoMe-TaskId': f'{TangoMe_TaskId}', 'Tango-Cipher-Name': 'TANGO1111','Tango-Cipher-Version': '1.0','Tango-Auth-Token': f'{Tango_Auth_Token}','Tango-Body-Encrypted': 'req','Tango-Body-Compressed': 'none','Tango-Digest': f'{Tango_Digest}','Content-Type': 'application/octet-stream',}
    params = (('pageCount', '0'),('sessionId', ''),('version', '4'),('locale', 'pt_BR'),('pageSize', '48'),('excludeUnmoderated', '0'),)
    response = requests.get('http://stream.tango.me/stream/social/v2/list/following', headers=headers, params=params)
    y4 = re.findall('.*\x00\x00\x00\x00@\x02H\x04.*"*',response.text)
    for x in range(len(y4)):
      user=y4[x][25:80]
      user1 = re.split('.*',user)[0].replace('Broadcast!*Khttp://cget.tango.me/contentserver/downloa','')
      r=requests.get(f'https://proxycador-cdn.tango.me/proxycador/api/profiles/v2/single?id={user1}&basicProfile=true&liveStats=true&followStats=true&liveFamily=true')
      try:
        dados = r.json()
        #print(dados)
        #print(user1)
        url = re.findall('https://.*?/*.?m3u8',y4[x])[0]
        if url not in jaenviados:
          ts = secrets.token_hex(5)
          jaenviados.append(url)
          nickname=(dados['basicProfile']['firstName'])
          photo=(dados['basicProfile']['profilePictureUrl'])
          profile=f'https://www.tango.me/profile/{user1}'
          caption=(f'{nickname} \n{url}')
          #bot.sendMessage(chatid, f'{caption}',file=photo)
          bot.sendPhoto(chatid, f'{photo}',caption=caption)
          os.system(f'(ffmpeg -i {url}  -fs 1.5G -c copy  video_{ts}.mp4 && ffmpeg -hide_banner -loglevel panic -i  video_{ts}.mp4 -ss 00:00:05 -vframes 1  -q:v 2  video_{ts}.jpg && vcsi video_{ts}.mp4 -t -w 850 -g 4x4 --end-delay-percent 20  -o video_2_{ts}.jpg && python3 up.py  --nomedoarquivo "video_{ts}.mp4" --legenda "{nickname}" --photo "video_{ts}.jpg" --photo2 "video_2_{ts}.jpg" &)&')
      except:
        pass



  




loading()
