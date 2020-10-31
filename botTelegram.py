import telebot
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import logging
bot= telebot.TeleBot("AQUÍ VA TU API DE TELEGRAM")

#Se usuara método para establecer conversación
logging.basicConfig(filename='archivarlog.log',level=logging.DEBUG)
def bot_conversacion(message):
    chatbot=ChatBot('Intranet Chat: ')
    entrenador= ChatterBotCorpusTrainer(chatbot)
    #entrenador.train('chatterbot.corpus.spanish')
    
    # while True:
    respuesta=chatbot.get_response(message)
            #print('Intranet Chat',respuesta)
    respuesta=str(respuesta)
            #bot.reply_to(message,respuesta)
    mensaje=open("respuesta.txt","w")
    mensaje.write(respuesta)
    mensaje.close()       

#Recibimos y enviamos una respuesta al comando start
@bot.message_handler(commands=["help","start"])
def enviar_mensaje(message):
    bot.reply_to(message,"Hola soy el bot del Intranet UAMI :) ")

#Recibimos cualquier otro mensaje
@bot.message_handler(func=lambda message:True)
def mensaje(message):
    bot_conversacion(message.text)
    respuesta=open("respuesta.txt","r")
    respuesta=respuesta.read()
    bot.reply_to(message, respuesta)
bot.polling()