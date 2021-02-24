#########################################################
from config import bot
import config
from time import sleep
import re
import database.db as db
import daos.cancionesDao as canciones
import daos.usuariosDao as usuarios
import models.Canciones as cancion

#########################################################
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
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
                "*agregar cancion o ag* - Te permite agregar una nueva cacione\n"
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
def on_set_cancion(message):
    bot.send_chat_action(message.chat.id, 'typing')
    parts = re.match(r"^(agregar cancion|ag) ([a-zA-Z]{3,20})",message.text,re.IGNORECASE)
    print (parts.groups())
    # print(message.from_user)
    nombreCancion = (parts[2])
    #duracionCancion = (parts[3])
    nombreUsuario=usuarios.register_usuario(message.from_user.id, message.from_user.first_name)
    print(nombreUsuario)
    cancion = canciones.register_cancion(nombreCancion,"5",message.from_user.id)
  ##  if nombreUsuario != None:
  ##      print(nombreUsuario)
    bot.reply_to(
        message,
        f"\U0001F4B0 ¡Cancion almacenada cone exito!: " if cancion == True
        else "\U0001F4A9 Tuve problemas registrando la cancion, ejecuta /start y vuelve a intentarlo")


##################Siempre al final#####################

@bot.message_handler(regexp=r"^(listar canciones|lc)")
def es(message):
    bot.send_chat_action(message.chat.id, 'typing')
    cancion = canciones.get_canciones()
    print (cancion)
  ##  if nombreUsuario != None:
  ##      print(nombreUsuario)
    bot.reply_to(
        message,
        f"\U0001F4B0 ¡Cancion almacenada cone exito!: " if cancion == True
        else "\U0001F4A9 Tuve problemas registrando la cancion, ejecuta /start y vuelve a intentarlo")

##################Buscar canción#####################
@bot.message_handler(regexp=r"^(buscar cancion|bc) ([a-zA-Z]{3,20})")
def on_find_cancion(message):
    bot.send_chat_action(message.chat.id, 'typing')
    parts = re.match(r"^(buscar cancion|bc) ([a-zA-Z]{3,20})",message.text,re.IGNORECASE)
    nombreCancion = (parts[2])
    cancion=canciones.find_canciones(nombreCancion)
    if cancion:
        mensaje="¡Su canción encontrada es: ID: "+ str(cancion.id) +" NOMBRE: "+ cancion.nombreCancion +" DURACION:" +cancion.duracionCancion
    else :
        mensaje= "Tuve problemas buscando la canción, ejecuta /start y vuelve a intentarlo"
    bot.reply_to(
        message,
        f"\U0001F4B0" +mensaje)
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