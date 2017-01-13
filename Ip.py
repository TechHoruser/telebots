#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tokens   #Usado para la importación de los tokens asignados por botfather
import urllib2  #Usado para la conexión a una web
import telebot
from telebot import types

tb = telebot.TeleBot(tokens.ip) 

@tb.message_handler(commands=['ip_pub_bitsman'])
def handle_message(message):
    ip = urllib2.urlopen('http://ip.42.pl/raw').read()  # Lectura de la ip en la web
    tb.send_message(message.chat.id, '<b>IP: </b>'+ip, parse_mode = 'HTML')
    
tb.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algn fallo.
