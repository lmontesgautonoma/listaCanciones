#########################################################
from config import bot
import config
from time import sleep
import re
import database.db as db
import daos.cancionesDao as canciones
import models.Canciones as cancion

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

##########################Agregar Canción#######################
@bot.message_handler(regexp=r"^(agregar cancion|ag) ([a-zA-Z]{3,20}) ([0-9]{1,2})")
def on_set_cancion(message):
    bot.send_chat_action(message.chat.id, 'typing')
    parts = re.match(r"^(agregar cancion|ag) ([a-zA-Z]{3,20}) ([0-9]{1,2})",message.text,re.IGNORECASE)
    print (parts.groups())

    nombreCancion = (parts[2])
    idtipoMusica = int(parts[3])
    response =''
    if idtipoMusica > 0 :   
        nombreUsuario=usuarios.register_usuario(message.from_user.id, message.from_user.first_name)
        print(nombreUsuario)
        canciones.register_cancion(nombreCancion,"5",message.from_user.id,idtipoMusica)
        response ='¡Cancion almacenada con éxito!:'
    else:
        listatipoMusica = tipoMusica.get_tipoMusica()
        if listatipoMusica:
            response ='Debe seleccionar el ID del tipo de música \n Los tipos de música son: \n'
            for tipomusica in listatipoMusica:
                response +=str(tipomusica.id) +' '+tipomusica.nombreTipoMusica+'\n'
        else:
            response = 'No existe Tipo de música, debe crearla con {agtm}'
        
    bot.reply_to(
        message,
        f"\U0001F4B0"+response)
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