from telethon import *
import random
import logging
from .. import loader, utils
import asyncio
import os

logger = logging.getLogger(__name__)



class YourMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"name": "cw"}



   
    async def scwcmd(self,event):
      

        await event.delete()
        
        a=0
        while a <= 24:
            a+=1
            await event.respond("🕹 Действия")
            await asyncio.sleep(1)  
            await event.respond("🛠 Работаем")
            await asyncio.sleep(3601)  

