#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tokens
import telebot
from telebot import types

tb = telebot.TeleBot(tokens.wgamers) 

@bot.message_handler(commands=['account'])
def handle_start_help(message):
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton('Gestionar Juegos', callback_data = 'manage_games'))
    tb.send_message( cid, "Editando Cuenta...\n¿Qué desas hacer?", reply_markup = markup )
 
tb.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algn fallo.
