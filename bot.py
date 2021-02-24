#########################################################
from config import bot
import config
from time import sleep
import re
import database.db as db
import daos.cancionesDao as canciones
import daos.usuariosDao as usuarios
import models.Canciones as cancion
import daos.tipoMusicaDao as tipoMusica
import daos.utilDao as util


#########################################################
if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
#######################START##################################
@bot.message_handler(commands=['start'])
def on_command_start(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(
        message.chat.id,
        util.get_welcome_message(bot.get_me()),
        parse_mode="Markdown")
        
    bot.send_message(
        message.chat.id,
        util.get_help_message(),
        parse_mode="Markdown")
##########################HELP###############################
@bot.message_handler(commands=['help'])
def on_command_help(message):
    bot.send_chat_action(message.chat.id, 'typing')

    bot.send_message(
        message.chat.id,
        util.get_help_message(),
        parse_mode="Markdown") 
##########################VERSION###############################
@bot.message_handler(commands=['about'])
def on_command_about(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(
        message.chat.id,
        message.from_user,
        parse_mode="Markdown")
    bot.send_message(
        message.chat.id,
        util.get_version(config.VERSION),
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
        f"\U0001F941" +mensaje)
##########################Agregar Tipo de música#######################
@bot.message_handler(regexp=r"^(agregar tipo musica|agtm) ([a-zA-Z]{3,20})")
def on_set_tipo(message):
    bot.send_chat_action(message.chat.id, 'typing')
    parts = re.match(r"^(agregar tipo musica|agtm) ([a-zA-Z]{3,20})",message.text,re.IGNORECASE)
    print (parts.groups())
    nombre= (parts[2])
    nombreTipoMusica=tipoMusica.register_tipoMusica(nombre)
    bot.reply_to(
        message,
        f"\U0001F399 Tipo de música almacenada con éxito!: " if nombreTipoMusica == True
        else "\U0001F507Tuve problemas registrando el tipo de música, ejecuta agregar tipo musica ó agtm a intentarlo")
##################Listar Canciones por tipo música#####################
@bot.message_handler(regexp=r"^(listar tipo musica por cancion |ltmc) ([0-9]{1,2})")
def list_tipomusica(message):
    bot.send_chat_action(message.chat.id, 'typing')
    parts = re.match(r"^(listar tipo musica por cancion |ltmc) ([0-9]{1,2})",message.text,re.IGNORECASE)
    idTipoMusica= (parts[2])
    listacanciones = canciones.lista_canciones(idTipoMusica)
    response =''
    if listacanciones:
        for cancion in listacanciones:
            response += str(cancion.id) +' '+cancion.nombreCancion+'\n'
    else:
        response = 'No tienes canciones almacenadas por el momento'

    bot.reply_to(
        message,
        f"\U0001F3B9	 ¡Tus canciones de la lista "+ idTipoMusica +" son: \n"+response)
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