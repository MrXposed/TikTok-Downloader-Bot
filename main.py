from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent
import shutil
import requests
import json
import os
import re
from bs4 import BeautifulSoup as bs
import time
from datetime import timedelta
import math
import base64
from progress_bar import progress, TimeFormatter, humanbytes
from dotenv import load_dotenv

load_dotenv()
bot_token = os.environ.get('BOT_TOKEN')
workers = int(os.environ.get('WORKERS'))
api = int(os.environ.get('API_KEY'))
hash = os.environ.get('API_HASH')
chnnl = os.environ.get('CHANNEL_URL')
BOT_URL = os.environ.get('BOT_URL')
app = Client("JayBee", bot_token=bot_token, api_id=api, api_hash=hash, workers=workers)



@app.on_message(filters.command('start'))
def start(client, message):
    kb = [[InlineKeyboardButton('𝗡𝗘𝗪 𝗬𝗢𝗥𝗞 ✈'('𝗕𝘆'
    reply_markup = InlineKeyboardMarkup(kb)
    app.send_message(chat_id=message.from_user.id, text=f"𝗛𝗲𝗹𝗹𝗼 𝘁𝗵𝗲𝗿𝗲, 𝗜 𝗮𝗺 **𝗧𝗶𝗸𝗧𝗼𝗸 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 𝗕𝗼𝘁**\n𝗜 𝗰𝗮𝗻 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗧𝗶𝗸𝗧𝗼𝗸 𝘃𝗶𝗱𝗲𝗼 𝘄𝗶𝘁𝗵𝗼𝘂𝘁 𝗪𝗮𝘁𝗲𝗿𝗺𝗮𝗿𝗸\n"
                          "__**𝗕𝘆 :**__ __@us6a02__\n"
                     parse_mode='md',
                     reply_markup=reply_markup)




@app.on_message(filters.command('help'))
def help(client, message):
    kb = [[InlineKeyboardButton('𝗡𝗘𝗪 𝗬𝗢𝗥𝗞 ✈'
    reply_markup = InlineKeyboardMarkup(kb)
    app.send_message(chat_id=message.from_user.id, text=f"𝗛𝗲𝗹𝗹𝗼 𝘁𝗵𝗲𝗿𝗲, 𝗜 𝗮𝗺 **𝗧𝗶𝗸𝗧𝗼𝗸 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗿 𝗕𝗼𝘁**.\n𝗜 𝗰𝗮𝗻 𝗱𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗮𝗻𝘆 𝗧𝗶𝗸𝗧𝗼𝗸 𝘃𝗶𝗱𝗲𝗼 𝗳𝗿𝗼𝗺 𝗮 𝗴𝗶𝘃𝗲𝗻 𝗹𝗶𝗻𝗸\n"
                                            "__𝗦𝗲𝗻𝗱 𝗺𝗲 𝗮 𝗧𝗶𝗸𝗧𝗼𝗸 𝘃𝗶𝗱𝗲𝗼 𝗹𝗶𝗻𝗸__🖇️",
                     parse_mode='md',
                     reply_markup=reply_markup)


@app.on_message((filters.regex("http://")|filters.regex("https://")) & (filters.regex('tiktok')|filters.regex('douyin')))
def tiktok_dl(client, message):
    a = app.send_message(chat_id=message.chat.id,
                         text='__𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗙𝗶𝗹𝗲 𝘁𝗼 𝘁𝗵𝗲 𝗦𝗲𝗿𝘃𝗲𝗿__🥁',
                         parse_mode='md')
    link = re.findall(r'\bhttps?://.*[(tiktok|douyin)]\S+', message.text)[0]
    link = link.split("?")[0]



    
    params = {
      "link": link
    }
    headers = {
      'x-rapidapi-host': "tiktok-info.p.rapidapi.com",
      'x-rapidapi-key': "f9d65af755msh3c8cac23b52a5eep108a33jsnbf7de971bb72"
    }
    
    ### Get your Free TikTok API from https://rapidapi.com/TerminalWarlord/api/tiktok-info/
    #Using the default one can stop working any moment 
    
    api = f"https://tiktok-info.p.rapidapi.com/dl/"
    r = requests.get(api, params=params, headers=headers).json()['videoLinks']['download']
    directory = str(round(time.time()))
    filename = str(int(time.time()))+'.mp4'
    size = int(requests.head(r).headers['Content-length'])
    total_size = "{:.2f}".format(int(size) / 1048576)
    try:
        os.mkdir(directory)
    except:
        pass
    with requests.get(r, timeout=(50, 10000), stream=True) as r:
        r.raise_for_status()
        with open(f'./{directory}/{filename}', 'wb') as f:
            chunk_size = 1048576
            dl = 0
            show = 1
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                dl = dl + chunk_size
                percent = round(dl * 100 / size)
                if percent > 100:
                    percent = 100
                if show == 1:
                    try:
                        a.edit(f'__**URL :**__ __{message.text}__\n'
                               f'__**Total Size :**__ __{total_size} MB__\n'
                               f'__**Downloaded :**__ __{percent}%__\n',
                               disable_web_preview=False)
                    except:
                        pass
                    if percent == 100:
                        show = 0

        a.edit(f'__𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗲𝗱 𝘁𝗼 𝘁𝗵𝗲 𝘀𝗲𝗿𝘃𝗲𝗿__♻️\n'
               f'𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝘁𝗼 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗡𝗼𝘄 ⏳__')
        start = time.time()
        title = filename
        app.send_document(chat_id=message.chat.id,
                          document=f"./{directory}/{filename}",
                          caption=f"**File :** __{filename}__\n"
                          f"**Size :** __{total_size} MB__\n\n"
                          f"__Uploaded by @{BOT_URL}__",
                          file_name=f"{directory}",
                          parse_mode='md',
                          progress=progress,
                          progress_args=(a, start, title))
        a.delete()
        try:
            shutil.rmtree(directory)
        except:
            pass


app.run()
