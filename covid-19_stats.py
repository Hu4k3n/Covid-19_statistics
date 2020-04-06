
from __future__ import unicode_literals
from telegram.ext import Updater, CommandHandler
import logging
import youtube_dl
import os
import sys
import mechanize as mc
from bs4 import BeautifulSoup

updater=Updater(token='1147623764:AAF4Yf6khqHAbO3abobfS9Q_znWPIsB5-dk',use_context=True)
dispatcher=updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
def start(update,context) :
    context.bot.send_message(chat_id=update.effective_chat.id, text="CoronaUpdates")
def srch(update, context):
    p=update.message.text
    br=mc.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    
    site=br.open("https://www.worldometers.info/coronavirus/")
    tablebody = ['<tbody'+i for i in site.get_data().decode().split('<tbody')][1:3]
    tbody=[i.split('</tbody>')[0]+'</tbody>' for i in tablebody]
    
    countries=BeautifulSoup(tbody[0],features="html5lib")
    total=BeautifulSoup(tbody[1],features="html5lib")
    
    #tmp=open("tmp.txt","w")
    c=countries.get_text().split('\n')
    #print (c)
    del c[0:2]
    i=0
    f=0
    print("Searched : "+str(p))
    while i <= len(c)-14:
        if(p.casefold()==c[i].casefold()) :
            
            context.bot.send_message(chat_id=update.effective_chat.id, text="Country: "+str(c[i])+"\nActive Cases : "+str(c[i+6])+"\nTotal critical cases : "+str(c[i+7])+"\nTotal recovered : "+str(c[i+5])+"\nTotal Cases : "+str(c[i+1])+"\nTotal Deaths : "+str(c[i+3])+"\nTotal Tests : "+str(c[i+10]))
            f=1
            break                                                                                                               
        else:
              i=i+14
    
    if f==0 :
        context.bot.send_message(chat_id=update.effective_chat.id, text="World wide cases updates\n\nActive Cases : "+str(c[6])+"\nTotal critical cases : "+str(c[7])+"\nTotal recovered : "+str(c[5])+"\nTotal Cases : "+str(c[1])+"\nTotal Deaths : "+str(c[3]))
        context.bot.send_message(chat_id=update.effective_chat.id, text='Enter Country name to know updates')
            
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text, srch)
dispatcher.add_handler(echo_handler)

start_handler=CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()

# list c values representations  
# 0 world
# 1 total cases
# 2 new cases
# 3 total deaths
# 4 new ddeaths
# 5 total recovered
# 6 active cases
# 7 serious crritical 
# 8 total cases per mill
# 9 deaths/mill
# 10 total tests
# 11 tests/mill