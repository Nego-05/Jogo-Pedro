# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Narutinha")
define b = Character("Sasuke")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene vilaf 

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show naruta

    # These display lines of dialogue.

    e "Você acabou de criar um mundo."

    e "Adicione imagens, musicas, fundo e publique para o mundo!"
    
    e "Olá, prazer em te conhecer!"

    e "Posso saber qual o seu nome?"

    hide naruta

    show sasuke

    b "O prazer é todo meu!"

    b "Me chamo Sasuke."

    hide sasuke

    show naruta

    e "De onde você veio?"

    e "Nunca te vi por aqui antes..."

    hide naruta

    show sasuke

    b "Não sou dessa vila."

    b "Sou da Vila da Névoa."

    b "Já ouviu falar de lá?"

    # aqui começa o menu
menu:

    "Já ouvi sim!":
        jump sim

    "Não, nunca ouvi.":
        jump não

label sim:

    m "Vou para sala do hokage agora"

    jump marry

label não:

    m "Vou para a sala dos uchihas "

    jump marry

label marry:

    "And so, we become a visual novel creating duo."
    # This ends the game.

    return