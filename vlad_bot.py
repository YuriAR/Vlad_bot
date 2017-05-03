# coding=utf-8

import sys
import time
import pprint
import telepot
import random
import os

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    op = random.randint(0,21);
    opAsk = random.randint(0,7);
    response = ["Risos", "Hausha7hausua7e","Calma","Nossa","Você tá bem, cara?", "Uia", "Te fode carlos", ".", "Egua" , "Nao ma", "Bacana", "Essa fera", "Que loucura", "O loco bichow", "Tenso", "Diz", "Rs", "E foi indo e foi indo... E tamo aqui agora", "Meu nome é Vladimir Lima tenho 24 anos, faço cerveja, ando de bicicleta e só", "Complicado esse humor", "boa", "Esse tempo todo?" ]
    responseAsk = ["Não sei, foda-se", "Que pergunta bosta, em? Vai se fuder", "Não, te fode", "Provavelmente nao em...", "Olha, eu acho que sim em...", "Dificil isso...", "Olha, talvez", "Sim! AEAEAEAEA!"]
    if command == '@vlademeeer_bot':
    	bot.sendMessage(chat_id, "Vlad Bot v1 (beta)\nCOMANDOS:\n/vlad - Frases épicas do mito!\n/askvlad - Pergunte qualquer coisa para o mito!\n/mito - Fotos sensacionais do mito!\n/calma - Calma\n\n\nDeveloped by: Yuri Reis / Bruno Monteiro")
    if command == '/calma' or command == '/calma@vlademeeer_bot':
        f = open('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/calma.jpg', 'rb') 
        bot.sendPhoto(chat_id, f)
    if command == '/teste':
        bot.sendMessage(chat_id, "testeUpdate")
    if command == '/vlad' or command == '/vlad@vlademeeer_bot':
    	bot.sendMessage(chat_id, response[op])
    if command == '/mito' or command == '/mito@vlademeeer_bot':
        img = random.randint(1,80);
        if os.path.exists('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/images/vlad%d.jpg' % img):
            f = open('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/images/vlad%d.jpg' % img, 'rb')
            bot.sendPhoto(chat_id, f)
            f.close();
        elif os.path.exists('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/images/vlad%d.jpeg' % img):
            f = open('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/images/vlad%d.jpeg' % img, 'rb')
            bot.sendPhoto(chat_id, f)
            f.close();
        else:
            f = open('/var/lib/openshift/573f29582d52714be30000dd/app-root/repo/images/vlad%d.png' % img, 'rb')
            bot.sendPhoto(chat_id, f)
            f.close();
    if command == '/askvlad' or command == '/askvlad@vlademeeer_bot':
        bot.sendMessage(chat_id, "Algo de errado não está certo, cadê a pergunta?")
    elif '/askvlad' in command:
        bot.sendMessage(chat_id, responseAsk[opAsk])
    # Do your stuff here ...


# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.

TOKEN = "220404785:AAHPsh6G845YNKpeexlaF2_-0TC-z4WSwJg"

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
