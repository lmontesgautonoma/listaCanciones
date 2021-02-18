#########################################################
from config import bot
import config
from time import sleep
import re
import database.db as db
import daos.cancionesDao as canciones
import daos.usuariosDao as usuarios
#######################START##################################
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    sleep(1)
    bot.send_message(
        message.chat.id,
        "\U0001F3B8 Hola Mi nombre es Music \U0001F3BC,\U0001F601 \U0001F601 Bienvenidos!  \U0001F601 \U0001F601 ",
        parse_mode="Markdown")
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
##########################VERSION###############################
def get_about_this(VERSION):
    response = (
        f"Lista Canciones v{VERSION}"
        "\n\n"
        "Desarrollado por jpmsvlchblmgbot "
    )
    return response

##########################Agregar Canción#######################
@bot.message_handler(regexp=r"^(agregar cancion|ag) ([a-zA-Z]{3,20})")
def on_get_balance(message):
    bot.send_chat_action(message.chat.id, 'typing')
    parts = re.match(r"^(agregar cancion|ag) ([a-zA-Z]{3,20})",message.text,re.IGNORECASE)
    print (parts.groups())
    nombreCancion = (parts[2])
    #duracionCancion = (parts[3])
    nombreUsuario=usuarios.register_usuario(message.from_user.id)
    cancion = canciones.register_cancion(message.from_user.id,nombreCancion,"5")
    if nombreUsuario != None:
        print(nombreUsuario)
    bot.reply_to(
        message,
        f"\U0001F4B0 ¡Dinero ganado!: " if cancion == True
        else "\U0001F4A9 Tuve problemas registrando la transacción, ejecuta /start y vuelve a intentarlo")
    

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