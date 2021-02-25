#########################################################
from config import bot
import config
from time import sleep
import re
#######################START##################################
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "\U0001F3B8 Hola Mi nombre es Music \U0001F3BC,\U0001F601 \U0001F601 Bienvenidos!  \U0001F601 \U0001F601 ",
        parse_mode="Markdown")@bot.message_handler(commands=['help'])
##########################HELP###############################
@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    response = (
                "Estos son los comandos y órdenes disponibles:\n"
                "\n"
                "*/start* - Inicia la interacción con el bot\n"
                "*/help* - Muestra este mensaje de ayuda\n"
                )

    bot.send_message(
        message.chat.id,
        response,
    parse_mode="Markdown")

##################Listar Canciones#####################
@bot.message_handler(regexp=r"^(listar canciones|lc)")
def es(message):
    bot.send_chat_action(message.chat.id, 'typing')
    listacanciones = canciones.get_canciones()
    response =''
    if listacanciones:
        for cancion in listacanciones:
            response += str(cancion.id) +' '+cancion.nombreCancion+'\n'
    else:
        response = 'No tienes canciones almacenadas por el momento'

    bot.reply_to(
        message,
        f"\U0001F3BC ¡Tus canciones son: \n"+response) 
##################Siempre al final#####################    
@bot.message_handler(func=lambda message: True)
def on_fallback(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)

    bot.reply_to(
        message,
        "\U0001F648 Ups, no entendí lo que me dijiste.")
#########################################################
if __name__ == '__main__':
    bot.polling(timeout=20)
#########################################################