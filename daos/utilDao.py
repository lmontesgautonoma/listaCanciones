########################Mensaje de bienvenida#########################################
def get_welcome_message(bot_data):
    response = (
        f"\U0001F3B8 Hola Mi nombre es Music \U0001F3BC,\U0001F601 \U0001F601 Bienvenidos!  \U0001F601 \U0001F601 \n Soy *{bot_data.first_name}* "
        f"también conocido como *{bot_data.username}*.\n\n"
        "¡Estoy aquí para ayudarte a almacenar y listar tú música!"
    )
    return response
############################HELP #############################
def get_help_message ():
    response = (
        "Estos son los comandos y órdenes disponibles:\n"
        "\n"
        "*/start* - Inicia la interacción con el bot (obligatorio)\n"
        "*/help* - Muestra este mensaje de ayuda\n"
        "*/about* - Muestra detalles de esta aplicación\n"
        "*agregar tipo musica|agtm {tipomusica} * - Registra tipo de música\n"
        "*agregar cancion|ag {nombrecanción} y {tipomusica}* - Registra canción y tipo de música\n"
        "*listar canciones|lc* - Lista las canciones agregadas\n"
        "*listar tipo musica por cancion |ltmc {índice}* - Listar canciones por un tipo música\n"
        "*buscar cancion|bc en {nombrecanción} * - Buscar canción por nombre\n"
    )
    return response
##########################VERSION###############################
def get_version(VERSION):
    response = (
        f"Lista Canciones v{VERSION}"
        "\n\n"
        "Desarrollado por jpmsvlchblmgbot "
    )
    return response