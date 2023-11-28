import os
#os.system("pip install -r requirements.txt")
#os.system("pip install Pillow")
#os.system("pip install easy-pil")
#os.system("pip install zipfile36")
os.system("clear||cls")
#from BotAmino import *
from BotAmino import BotAmino
import random
import giphy_client as gc
from giphy_client.rest import ApiException
#from random import *
#from PIL import Image, ImageDraw, ImageFont
#from easy_pil import Editor, Canvas, load_image, Font
import base64
#from zipfile import ZipFile
from random import uniform, choice, randint
from time import *
import datetime
from gtts import gTTS
import urllib.request
import urllib.parse
from os import system
import wikipedia
import re
from json import load
from os import path
from pathlib import Path
from os import scandir, getcwd
from os.path import abspath
from sys import argv as args
#import json
import sys
import threading
import ujson as json
import time
from fancy_text import fancy
from threading import Thread
from time import time,sleep
from time import asctime
import threading, time
from joincomm import joincomm
import io
from io import BytesIO
import suppress
#import BytesIO
import requests

from keep_alive import keep_alive
print("Iniciando...")

keep_alive() #==>Solo activar para hostear

client = BotAmino("serval8@1secmail.com", "submundoreina","19F358D56D61688812900E7989D4C83BE2AB7092202AE5668432F8161FF7C228A9E2D90EA0E43AAD53")


#fs = open("sids.txt","r+")
#sidd = (fs.read())
#client = BotAmino(sid=sidd)


client.wait = 2
client.prefix = "!"
client.no_command_message = "Tontito! Este comando no existe. Pon !help 2 para acceder a mi guia de comandos.. ₍ᐢ. .ᐢ₎"
client.activity = True
client.spam_message = ""
wikipedia.set_lang("es")

#Dueños del bot.

def tradlist(sub):
    sublist = []
    for elem in sub:
        try:
            sublist.append(client.get_from_code(f"http://aminoapps.com/u/{elem}").objectId)
            continue
        except Exception:
            pass
        sublist.append(elem)
    return sublist


whitefile = 'whiteauthor.txt'
whitelist = []
try:
    with open(whitefile, 'r') as file:
        for whitelistmember in file.readlines():
            whitelist.append(whitelistmember.strip())
except FileNotFoundError:
    a = open(whitefile, "w")
    a.close()

whitelist = tradlist(whitelist)


def is_it_me(data):
    if any(user in data.authorId for user in whitelist):
        return True
    data.subClient.send_message(chatId=data.chatId, message="Tontito! No tienes acceso a mis comandos de Dueño. ૮₍ ˃̵͈᷄ . ˂̵͈᷅ ₎ა")
    return False

###

def url_like(url):
    link = requests.get(url)
    result = BytesIO(link.content)

    return result


###

# La estética base para cosas de bot
def esteticabase(t, conteudo, subtitulo=""):
    return f"""
[c]┏                    ───                      ┓ 
[C]──   Kotomi   ──
[C]✩✼　｡ﾟ･　　ﾟ･　☆　° ｡ 
[C] ❤️’• {t}
[C]         ╺╺╺╺╺╺╺╺(☕)
[C] — {subtitulo}
{conteudo}
[C]┗                                                  ┛    
        """


# Sistema de logros (la parte principal del código)
def conquista(cid, achievement, pontos):
    # Primero se ejecuta para crear el archivo JSON si no tiene uno
    system(f"python3 scripts/conquistas.py {cid} ignore 0")

    # Se lee el archivo JSON para comprobar si ya se ha conseguido el logro
    userjson = load(open(f"info/{cid}.json", "r"))

    # É checado
    try:
        if achievement not in userjson["achievements"]:
            system(f"python3 scripts/conquistas.py {cid} {achievement} {pontos}")
            # Si el usuario no tiene este logro, se devuelve True
            return True
        else:
            # Si no, se devuelve False.
            return False
    except KeyError:
        # En caso de KeyError, el logro se considera como no ganado
        system(f"python3 scripts/conquistas.py {cid} {achievement} {pontos}")
        return True


def conquistado(nome, pontos, descript):
    return f"""[c]Logros
[c]
[bc]{nome}
[ci]{descript}
[cu]+{pontos} puntos"""


def edastaff(authid):
    system(f"python3 scripts/ranking.py {authid} ! 0")
    jinfo = load(open(f"info/{authid}.json", "r"))
    if jinfo["type"] == "staff":
        return jinfo["staff_type"]
    else:
        return False


# Comando simple que envía mensaje
@client.command("Serval")
def serval(data):
    if conquista(data.authorId, "Serval", 10000):
        data.subClient.send_message(data.chatId, conquistado("Serval!", 10000, "Por escribir !Serval obtienes un logro mitico"))
    data.subClient.send_message(data.chatId, "Serval es una persona genial :3 !")

@client.command("Amesulogro")
def amesulogro(data):
    if conquista(data.authorId, "¡Fiore_Felicita!", 5000):
        data.subClient.send_message(data.chatId, conquistado("¡Fiore_Felicita!", 5000, "Por ganar el sorteo obtienes un logro ganador"))
    data.subClient.send_message(data.chatId, "Kotomi agradece su participación del sorteo y futuro apoyo que seguirás brindando")

@client.command("Kotomi")
def kotomilogro(data):
    if conquista(data.authorId, "Kotomi", 20000):
        data.subClient.send_message(data.chatId, conquistado("Kotomi!", 10000, "Por escribir !Kotomi obtienes un logro bonus"))
    data.subClient.send_message(data.chatId, "Kotomi agradece que hayas aceptado los terminos y condiciones, en caso no sepas escribir !terminosuser y luego !aceptar")


@client.command("Dominator")
def dominator(data):
    if conquista(data.authorId, "Dominator", 5000):
        data.subClient.send_message(data.chatId, conquistado("Dominator!", 5000, "Por escribir !Dominator obtienes un logro mitico"))
    data.subClient.send_message(data.chatId, "Sabes algo te quiero con todo mi corazón. !")

@client.command("Otaku")
def otaku(data):
    if conquista(data.authorId, "Otaku", 5000):
        data.subClient.send_message(data.chatId, conquistado("Otaku!", 5000, "Por escribir !Otaku obtienes un logro mitico"))
    data.subClient.send_message(data.chatId, "Lo que todo amante del anime es en realidad :3")

@client.command("Gamer")
def gamer(data):
    if conquista(data.authorId, "Gamer", 5000):
        data.subClient.send_message(data.chatId, conquistado("Gamer!", 5000, "Por escribir !Gamer obtienes un logro mitico"))
    data.subClient.send_message(data.chatId, "Por que te gustan los juegos tanto como a mi :3")
 
@client.command("Granjero")
def granjero(data):
    if conquista(data.authorId, "Granjero", 5000):
        data.subClient.send_message(data.chatId, conquistado("Granjero!", 5000, "Por escribir !Granjero obtienes un logro mitico"))
    data.subClient.send_message(data.chatId, "Por que te gustan los animales, eres el mejor :3")
 

    
# !help
@client.command("help")
def ajuda(data):
    if conquista(data.authorId, "Principiante", 1000):
        data.subClient.send_message(data.chatId, conquistado("Principiante!", 1000, "Por escribir !help por primeira vez"))
    # Comprueba la página solicitada y luego muestra los comandos
    if data.message == "1":
        data.subClient.send_message(data.chatId, esteticabase("help", """
[c]!ship [Persona1, Persona2] - Shippea a dos usuarios, (Ejemplo: !ship Saki Kotomi),  (No mencionar a los usuarios solo escribir su nombre).
[c]!compatibilidad [Usuario] - Revisa su compatibilidad con el usuario mencionado, (Ejemplo: !ship @Emilia).
[c]!pvp [1, 2, rounds] - Pvp entre 2 usuarios con un cierto número de rondas, (Ejemplo: !pvp Saki Kotomi 2).
[c]!msg [Mensaje] - Enviar un mensaje específico, (Ejemplo: !msg Hola soy Kotomi).
[c]!sorteos [tipo; argumento] - Realiza un sorteo, para ver los tipos escribe !help sorteos
[c]!quote [Usuario, frase] - Cita una frase, (Ejemplo: !quote r Kotomi es genial).
[c]!vote [criar, votar, ver] - Cree, vote o vea una encuesta. !help vote para más información.
        """, "Página 1"))
    elif data.message == "2":
        data.subClient.send_message(data.chatId, esteticabase("help", """  [c] Recuerda para registrarse solo debe colocar !help 2 y !logros
[c] !ayuda - Ver la lista de comandos adicionales.
[c] !puntos - Visualiza la cantidad de puntos que tienes actualmente.
[c] !logros - Ver sus logros actuales.
[c] !terminosuser - Revise los términos y condiciones de Kotomi
[c] !ahorcado play - para comenzar a jugar a "adivina la palabra" - Recuerda adivinar la palabra con !ahorcado y la palabra
[c] !claim [ver, claim] - Ver - Vea cuántos acs puede retirar, claim - retira sus acs (a partir de 10 acs, se puede retirar)
[cib] Proximamente se agregaran nuevos comandos, espero su apoyo, gracias!!!
        """, "Página 2"))
    elif data.message == "sorteos":
        data.subClient.send_message(data.chatId, esteticabase("help", """
[c]Tipos de sorteos:
[c]     n - Sortea números. Argumentos: número inicial; número final, (Ejemplo: !sorteos n; 1 5)
[c]     p - Sortea nombres. Argumentos: nombres (No tiene límites), (Ejemplo: !sorteos p; Saki Kotomi Emilia)
        """, "Sorteos"))
    elif data.message == "vote":
        data.subClient.send_message(data.chatId, esteticabase("help", """
[c] Modos:
[c]    crear - Crea una encuesta
[c]       Argumentos: !vote criar; Nombre de la encuesta; opción 1; opcion 2; etc, , (Ejemplo: !vote crear;Saki es genial?; si; no; tal vez)
[c]     votar - Votar en una encuesta
[c]         Argumentos: !vote votar; id; opción, (Ejemplo: !vote votar;Saki_es_genial?;si)
[c]     ver - Ver los resultados de la encuesta
[c]         Argumentos !vote ver; id, (Ejemplo: !vote ver;Saki_es_genial?)
        """, "Vote"))
    elif data.message == "mod":
        data.subClient.send_message(data.chatId, esteticabase("Mod", """
[c] !tag [@user] - Dá tag a um usuário
[c] !op [role, @users] - Dá um titulo para um usuário (VALIDO APENAS PARA O BOT)
[c] !deop [@users] - Tira o op de um usuário
[c] !ban [@user, motivo] - Bane alguém
[c] !strike [@user, motivo] - Dá um castigo de 24hrs para alguém
[c] !avisar [@user, motivo] - Manda um aviso
[c] !end - Desliga o bot
        """, "  Mod"))
    else:
        data.subClient.send_message(data.chatId, "Digite o número da página. (Total de páginas: 2)")


# Comando !ship
@client.command("ship")
def ship(data):
    # Esta parte define a las personas dadas como argumento (en la variable "personas")
    # utilizando el carácter de espacio como base y, poco después, comprueba la cantidad
    # número de caracteres en cada nombre (en el bucle for) para que el nombre del envío se realice sin errores
    # (o al menos estaba libre de errores)
    # Al final, el resultado se ve así: [[pessoa1, False], [pessoa2, True]]
    # Cada elemento representa a la persona del argumento más si el tamaño es inferior a 3
    pessoas = data.message.split(" ")
    pessoas_preserve = data.message.split(" ")
    for loop in range(0, 2):
        if len(pessoas[loop]) < 3:
            pessoas[loop] = [pessoas[loop], True]
        else:
            pessoas[loop] = [pessoas[loop], False]

    shippname = []
    # Esta parte es lo que define el nombre del shipp.
    for index in range(0, 2):
        # Condicional utilizado para crear el nombre de shipp
        if pessoas[index][1]:
            shippname.append(pessoas[index][0])
        # Si esta condición es negativa, se cortarán los 3 caracteres iniciales o los 3 finales.
        else:
            if index == 0:
                shippname.append(pessoas[index][0][0:3])
            else:
                reverse = len(pessoas[index][0]) - 4
                for loop in range(0, len(pessoas[index][0]) + 1):
                    reverse += 1
                    shippname.append(pessoas[index][0][reverse])
                    if loop == 2:
                        break

    # Toma la lista de caracteres generados y la une en una cadena con el nombre del shipp
    # y luego tirar todo a minúsculas y finalmente a mayúscula la primera letra
    shippname = ((''.join(shippname)).lower()).capitalize()

    if shippname.lower() in ["Kotomi", "Saki"]:
        if conquista(data.authorId, "incesto", 500):
            data.subClient.send_message(data.chatId, conquistado("Es un, incesto", 500, "Ewww..."))
    # Frases, tomé de lo antiguo
    mtruim = ["Poco amorosos", "Son hermanos, y eso es incesto...", "Ellos se odian", "Meh.",
              "Realmente quería que eso funcionara, pero nunca funcionará.",
              "Son sólo amigos...", "Voy a tener que cancelarte por enviar esto."]
    ruim = [f"Podría funcionar si {pessoas[randint(0, 1)][0]} quisieran UwU...", "Okay...", "Eh..."]
    ok = ["Se verían tan bien juntos... ¿Pero qué hacer?", "Confieso que el porcentaje sólo es superior al 25 porciento, por que? "
                                                              "Ellos son "
                                                              "amigos íntimos",
          f"{pessoas[0][0]} realmente quiere estar con {pessoas[1][0]}, pero {pessoas[1][0]} no quiere", "No creo que diera "
                                                                                                  "bien, pero siempre"
                                                                                                  "tiene un "
                                                                                                  "talvez.",
          "Quién sabe algún un día?", "Lindo, pero no", f"Ya están saliendo, pero "
                                                   f"{pessoas[randint(0, 1)][0]} no sabe."]
    bom = ["Ya están juntos en secreto.", f"Hombre, confieso que no fue al 100% porque {pessoas[randint(0, 1)][0]} es "
                                                 f"kpopper", f" Mi pareja favorita <3", "Lindo, apenas.",
           "Ojalá tuviera una webnamorada como ustedes :(", ""]
    mtbom = [f"YA ESTÁN SALIENDO {randint(2, 15)} AÑOS, COMO LO SINTIERON ANTES??", "Una pareja muy genial :3.",
             "É̷͙̪̝̏̿̽̀s̸̳̭̄̅s̸̞̪̊̓̇̂̔e̴̲̰̎͌̌̐͛̍̈́ ̴̡̡̝̙̥̪͕͉͉̈́̎c̸̛̻̼̟̹̭͛̈́͝ͅḁ̶̆̄̿͊̽̕s̶̡̾̑̐a̴̼̱̲̦͍̜̩̖͐̓́̑̆͋̈̅̕l"
             "̷̧̗̬͕͖̯̖͓̻̈́̃̈̒͌̒̚͠ͅ ̴̘̩͖̓͒ͅé̵͔͛͌͐̈́̔̑͛̓̈ ̷͈̹̻̂̈̀̂͋̀͛̃͝t̸̡̛̝̫̯̲̗̻̬͇̎ã̵͖̰̑͆̄̋͒̈̇ő̵͚͓͂̅̈͂̆̃̏̄ "
             "̵̧̮̟͈̟̌͊̑̃͘b̶͉̯͋̕ö̸̧̰͕̥̹͓͙̰͑͐̈́̆̌̄̓͂͝m̴̡̧̰̥̥͖̻̑͌̌͑͐̋ "
             "̵̛͚͕̠̭̳͉͓̘́͜q̴̱̲͓̆͆͗̇̎̅͌̓̈́u̸̧̢̼̞̱͆͑͂̃͋͘͜͠e̴̬̩̬͓̪͍̭͕̓̚͠ ̴̺̍̋͋̆̽͜ṁ̷̱͐́͐͌̈ě̷̛̪̜͔̉͑̀̇̉̑ͅ "
             "̶͍̘̒̾͌̕̕d̸̞̳̱̗͉͙̫̠͖̂͊̋̏̍̆̽̋͜ȃ̴̜̜̮̱̫̺̺̑ "
             "̵̡̨̑̍̓̊̄̅̐̿̊̋ņ̵̬̙̳͕͖̩̫͓̦̍͑͛̅͒̌̇͠o̴̘̯̩͒͆͜j̵͚̖̹̱̠̘̣̟͊̾͂͌͘͝o̸̠͍̳͙̐.̴͑͒́̓̆̕̚͜",
             "No tenía ni idea de qué escribir, era tan bueno.", "Esa pareja perfecta...", "bot.exe se ha detenido"
                                                                                             "podría no funcionar."]

    #El porcentaje se establece para que se pueda tomar una frase aleatoria de las listas anteriores
    # También se define la variable de valor porcentual restante.
    # Estos valores también servirán para crear la barra.
    porcentagem = float(f"{uniform(0, 100):.2f}")
    vazio = 100 - porcentagem

    # Por fim, uma condicional para pegar uma string de uma das listas
    if porcentagem <= 10:
        quote = choice(mtruim)
    elif 10 <= porcentagem <= 25:
        quote = choice(ruim)
    elif 25 <= porcentagem <= 50:
        quote = choice(ok)
    elif 50 <= porcentagem <= 75:
        quote = choice(bom)
    elif 75 <= porcentagem <= 100:
        quote = choice(mtbom)
    else:
        quote = "NaN"

    # Enviar el mensaje final
    data.subClient.send_message(data.chatId, esteticabase(shippname, f"""   
[c]
[c][{"█" * int(porcentagem / 5)}{"⠀" * int(vazio / 5)}]
[ciu]{porcentagem}% de posibilidades de estar juntos.
[ci]
[ci]"{quote}"
""", f"{pessoas_preserve[0]} x {pessoas_preserve[1]}"))


# !pvp
@client.command("pvp")
def fight(data):
    # Argumentos
    args = data.message.split(" ")
    args.append(5)

    # Aquí sucede el juego en sí.
    score = [0, 0]
    r = 0
    winner = ""
    for loop in range(0, int(args[2])):
        r += 1
        score[0] = score[0] + randint(0, 1)
        score[1] = score[1] + randint(0, 1)

        # Se define el ganador de esta ronda
        if score[0] > score[1]:
            winner = args[0]
        elif score[0] < score[1]:
            winner = args[1]
        else:
            winner = "Nadie"
        data.subClient.send_message(data.chatId, esteticabase("PvP", f"""
[cu]{args[0]} {score[0]} x {score[1]} {args[1]}
[c]
[c]{winner} está en ventaja!
        """, f"Round {r}"))
        sleep(3)
    data.subClient.send_message(data.chatId, f"{winner} ganó.")


# !spam
@client.command("spam", is_it_me)
def flood(data):
    args = data.message.split(" ")
    for loop in range(0, int(args[0])):
        data.subClient.send_message(data.chatId, ' '.join(args[1:]))
        sleep(1)


# !msg
@client.command("msg")
def sms(data):
    data.subClient.send_message(data.chatId, data.message)


# !cancelar
@client.command("cancelar")
def cancel(data):
    #La persona cancelada en cuestión.
    pessoa = data.message

    # Las razones de las cancelaciones están aquí.:
    data.subClient.send_message(data.chatId, esteticabase(f"Cancelado", conteudo=f"""
[c]
[c]O motivo é que {pessoa} {choice(['shippou incesto', 'disse que não gosta de gatos', 'a',
                                    'gosta do Felipe Neto', "não gosta de Gumball", "é o Neymar", "é gado para caralho"
                                                                                     , "é lindo dms", "gosta de Kpop",
                                    "não fez nada", "é comunista", "apoia o anarcocapitalismo", "apoia o narcotráfico",
                                    "被中共黑了", "é chato pra krl",
                                    "odeia cachorros", "assiste boku no hero", "não gosta do Felipe Neto",
                                    "dbdzkfhgvkdhf",
                                    "é hacker",
                                    "gosta do bts", "não gosta do bts", "falou que gosta de gumwin", "é shitposter",
                                    "assiste tio orochi", "usa windows", "usa linux",
                                    "apoia o comunismo", "apoia o monarquismo", "come figado de frango",
                                    "eu quero mijar"])}.""", subtitulo=f"{pessoa} foi enviado(a) para a prisão após "
                                                                       f"sofrer cancelamento."))



# !sorteio
@client.command("sorteos")
def luck(data):
    args = data.message.split(";")

    # En primer lugar, se define el tipo de sorteo.
    if args[0] == 'n':

        # En el caso de sorteos numéricos, es usado randint() sacar un número entre los especificados. las categorias
        # especificados se colocan en la lista argx
        argsx = args[1].split(" ")
        if argsx[0] == "" or argsx[0] == " ":
            del argsx[0]
        num = randint(int(argsx[0]), int(argsx[1]))
        data.subClient.send_message(data.chatId, str(num))
    elif args[0] == 'p':

        # Mismo esquema que el anterior, solo cambia la función de la librería random. Esto elige nombres de una lista.
        argsx = args[1].split(" ")
        if argsx[0] == "" or argsx[0] == " ":
            del argsx[0]
        p = choice(argsx)
        data.subClient.send_message(data.chatId, p)


# !wiki
@client.command("wiki")
def wiki(data):
    # Tome la página y el resumen y luego divídalo para que pueda caber en el límite
    try:
        wp = wikipedia.page(data.message)
    except wikipedia.exceptions.DisambiguationError as e:
        # Si aterriza en una página de desambiguación, imprime un error
        may_referir_a = '\n[c]'.join(e.options)
        data.subClient.send_message(data.chatId, esteticabase("Desambiguación", f"""[c]{may_referir_a}""",
                                                              f"{data.message} Puede referirse a: "))
        return False
    wpr = wp.content.split("\n")

    # Manda o primeiro paragrafo
    data.subClient.send_message(data.chatId, esteticabase(wp.title, f"""[c]{wpr[0]}

[c]Mas información en: {wp.url}""", f"Resumen de {wp.title}"))


# !quote
@client.command("quote")
def fala(data):
    args = data.message.split(" ")
    if args[0] == 'r':
        args[0] = choice(
            ["Ednaldo Pereira","Saki Saki", "Gumball Watterson", "Darwin Watterson", "Felipe Neto", "Diggo", "Juilo Caesar",
                "Aristoceles", "Isaac Newton", "Albert Einsten", "Joseph Stalin", "Vladmir Putin", "Karl Marx",
                "Vladmir Lenin", "Jesus Cristo", "Mark Zuckerberg", "Bill Gates", "Steve Jobs", "Autor Desconhecido",
             "Dom Pedro II do Brasil", "Dom Pedro I do Brasil", "Pitagoras", "Galileu Galileu", "Pedro",
                "Stephen Hawking"])
    data.subClient.send_message(data.chatId, f"[cui]{' '.join(args[1:])} ~{args[0]}")




# !compatibilidad
@client.command("compatibilidad")
def kotomi_compatibilidad(data):
    # porcentaje de compatibilidad
    porcentagem = float(f"{uniform(0, 100):.2f}")
    resto = 100 - porcentagem

    data.subClient.send_message(data.chatId, esteticabase("Compatibilidade", f"""
[c] Las posibilidades de {data.author} y {data.message} combinadas son de {porcentagem}%
[c]
[c][{"█" * int(porcentagem / 5)}{"⠀" * int(resto / 5)}]
    """, f"{data.message} x {data.author}"))


# Esto es sólo para probar, ignorar
@client.command("teste")
def teste(data):
    if data.message == "0":
        os.system("python3 scripts/filewriter.py")
        data.subClient.send_message(data.chatId, str(''.join(open("scripts/file", "r").readlines())))


# !puntos
@client.command("puntos")
def points(data):
    # Mira la cantidad de puntos
    pontos = load(open(f"info/{data.authorId}.json", "r"))
    pontos = str(pontos["points"])

    data.subClient.send_message(data.chatId, pontos)


# !logros
@client.command("logros")
def conquistas(data):
    # Almacena en el archivo JSON
    conq = load(open(f"info/{data.authorId}.json", "r"))
    conqs = conq["achievements"]
    conqsform = []

    # Hace formateos de logros
    for loop in range(0, len(conqs)):
        conqsform.append((conqs[loop].replace("_", " ")).capitalize())
    conqsform = "\n[c]".join(conqsform)

    # Enviar los logros
    data.subClient.send_message(data.chatId, esteticabase("Logros", f"""
[c]
[c]{conqsform}""", f"Logros de {data.author}"))


# !vote
@client.command("vote")
def votar(data):
    args = data.message.split(";")
    # Crea una encuesta con pollid
    if args[0] == "crear":
        pollid = ((args[1]).strip(" ")).replace(" ", "_")
        # Los archivos JSON no admiten espacios
        for loop in range(0, len(args[1:])):
            args[loop + 1] = (args[loop + 1].strip(" ")).replace(" ", "_")

        system(f"python3 scripts/polls.py criar {pollid} {' '.join(args[2:])}")
        data.subClient.send_message(data.chatId, f"Criada uma enquete com o ID '{pollid}'")
    elif args[0] == "votar":
        args[2] = (args[2].strip(" ")).replace(" ", "_")
        system(f"python3 scripts/polls.py votar {args[1]} {args[2]}")
        data.subClient.send_message(data.chatId, "Votado!")
    elif args[0] == "ver":
        polljson = load(open(f"enquetes/{args[1].strip(' ')}.json", "r"))
        # Guardar valores en una lista
        jvalues = []
        for k, v in polljson.items():
            jvalues.append(f"\n[c]{k}: {v}")

        # Mostrar los resultados
        data.subClient.send_message(data.chatId, esteticabase("Enquete", f"{''.join(jvalues)}",
                                                              f"{((args[1].strip(' ')).replace('_', ' ')).capitalize()}"
                                                              f""))


# !claim (comando tomado y adaptado del servidor de discord de Phoenix)
@client.command("claim")
def claim(args):
    file = open(f"info/{args.authorId}.json", "r")
    jclaims = load(open(f"info/{args.authorId}.json", "r"))

    blogs = args.subClient.get_user_blogs(args.authorId).blogId

    coins = args.subClient.get_wallet_amount()
    if coins >= 1 and jclaims["claims"] >= 0.1 and args.message == "claim":
        args.subClient.pay(int(jclaims["claims"] * 10), blogId=blogs[0])
        args.subClient.send_message(args.chatId, "Enviado!")
        if conquista(args.authorId, "claim", 1000):
            args.subClient.send_message(args.chatId, conquista("Usuario_Beta", 1000, "Da !claim y gana acs por primera vez."))
        system(f"python3 scripts/ranking.py {args.authorId} ! {jclaims['claims'] * 1000}")
    elif args.message == "ver":
        args.subClient.send_message(args.chatId, f"Usted puede recoger {jclaims['claims'] * 10} acs.")
    else:
        if coins < 1:
            args.subClient.send_message(args.chatId, f"cuenta vacia :(")
        else:
            args.subClient.send_message(args.chatId, "¡Error! Solo puedes reclamar desde 1 AC!")


# !tag
@client.command("tag")
def titulo(data):
    if not edastaff(data.authorId):
        return False
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    data.subClient.add_title(mention[0], ' '.join(data.message.split(" ")[1:]))
    data.subClient.send_message(data.chatId, "Pronto.")


# !op
@client.command("op")
def op(data):
    staff = edastaff(data.authorId)
    if not staff:
        return False
    else:
        if staff != "leader":
            return False

    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    for loop in mention:
        system(f"python3 scripts/op.py {loop} {data.message.split(' ')[0]}")
    data.subClient.send_message(data.chatId, f"Dado op para os usuarios mencionados")


@client.command("ban")
def banir(data):
    staffstatus = edastaff(data.authorId)
    if staffstatus:
        if staffstatus == "leader":
            mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
            data.subClient.ban(mention[0], reason=" ".join(data.message.split(' ')[1:]), banType=0)
            data.subClient.send_message(data.chatId, f"Usuário banido com sucesso!")


@client.command("end")
def botexit(data):
    if edastaff(data.authorId):
        os._exit(1)


@client.command("strike")
def castigar(data):
    staff = edastaff(data.authorId)
    if staff:
        if staff in ["leader", "curator"]:
            args = data.message.split(" ")
            mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
            data.subClient.strike(userId=mention[0], time=5, title=' '.join(args[1:]))


@client.command("avisar")
def avisar(data):
    if edastaff(data.authorId):
        mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
        data.subClient.warn(mention[0], f"{' '.join(data.message.split(' ')[1:])}")


@client.command("deop")
def deop(data):
    if data.authorId == "2ddaa4b1-8562-45c4-a87e-e494ac4c291d":
        mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
        for loop in mention:
            system(f"python3 scripts/deop.py {loop}")
        data.subClient.send_message(data.chatId, "Tirado o op dos usuários mencionados")


@client.command("information")
def info(data):
    mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
    if type(mention) == None:
        user = load(open(f"info/{data.authorId}.json", "r"))
        information = []
        for key, value in user.items():
            information.append(f"{key}: {value}")
        data.subClient.send_message(data.chatId, "\n".join(information))
    else:
        for loop in mention:
            try:
                user = load(open(f"info/{loop}.json", "r"))
            except FileNotFoundError:
                user = {
                    "nodata": "nodata"
                }
            information = []
            for key, value in user.items():
                information.append(f"{key}: {value}")
            sleep(0.5)
            data.subClient.send_message(data.chatId, "\n".join(information))



@client.command("Ahorcado")
def f(data):
    if data.message.split(" ")[0] != "play":
        os.system(f"python3 scripts/forca.py {data.authorId} {data.message}")
    else:
        splitmsg = data.message.split(" ")
        try:
            os.system(f"python3 scripts/forca.py {data.authorId} {splitmsg[0]} {splitmsg[1]}")
        except IndexError:
            os.system(f"python3 scripts/forca.py {data.authorId} {splitmsg[0]} easy")
    sinfo = load(open(f"info/forca/{data.authorId}.json", "r"))
    try:
        sinfo = load(open(f"info/forca/{data.authorId}.json", "r"))
    except FileNotFoundError:
        data.subClient.send_message(data.chatId, f"!f play para comenzar a jugar.")
    if sinfo["gamestatus"] == "defeat":
        data.subClient.send_message(data.chatId, f"""[bc]DERROTA!
[i]{data.author} 
[cu]la palabra era "{sinfo["word"]}"!
        """)
        if conquista(data.authorId, "Derrota_fuerza", 300):
            data.subClient.send_message(data.chatId, conquistado("Derrota", 300, "Perder Fuerza"))
    elif sinfo["gamestatus"] == "victory":
        if conquista(data.authorId, "Victoria_fuerza", 700):
            data.subClient.send_message(data.chatId, conquistado("Victoria", 700, "Ganar Fuerza."))
        data.subClient.send_message(data.chatId, f"""[bc]Victoria! {data.author}
[cu]Felicidades!
        """)
    else:
        letterset = set(sinfo["letters"])
        data.subClient.send_message(data.chatId, esteticabase(f"Ahorcado de {data.author}", f"[c]{sinfo['playerview'].replace('', ' ')}\n[c]{' '.join(letterset)}", f"{len(sinfo['word'])} letras, {sinfo['tries']} Intentos."))

@client.command("coin")
def monedero(data):
    balance = data.subClient.get_wallet_amount()
    data.subClient.send_message(data.chatId, message=f"Mis coins disponibles al momento son: {balance}.")


#Comandos Copia 1.1

####

@client.command("ayuda")
def ayudakotomi(data):
    data.subClient.send_message(chatId=data.chatId, message="""[BC]
[C]Hola,  ¿qué tal? Mi nombre
[C]es ╰ Kotomi ╯  y esta  es  mi
[C]guía   de    comandos,  los
[C]cuales están separados en
[C]las  siguientes  categorías:
[C]. 𐑺 !chats           . 𐑺 !entretenimiento
[C].   𐑺 !perfil     . 𐑺 !dueño
[C].     𐑺 !acciones     . 𐑺 !cutes
[Cu]𖧧 Para ver  los  comandos
[Cu]𖧧 pon el nombre de cada
[Cu]𖧧 categoría  en   el  chat.

[C]Ejemplo: !acciones
[C]꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷""", replyTo = data.messageId)


@client.command()
def chats(data):
    data.subClient.send_message(data.chatId, message="""[bc]⤥〃Comandos Para Chats༴ 

[c]joinchat • leavechat • kickchat • banchat • view • unview • descripcion • tittlechat • anuncio • pinanuncio """)

@client.command()
def perfil(data):
    data.subClient.send_message(data.chatId, message="""[bc]⤥〃Comandos para el Perfil༴ de Kotomi

[c]name • bio • icon • bgperfil • bloquear • desbloquear """)

@client.command()
def dueño(data):
    data.subClient.send_message(data.chatId, message="""[bc]⤥〃Comandos para el admin

[c]bienvenidamuro • reiniciar • everyone • ping
[c][c]!spam [Cantidad, mensaje] - Escribe un mensaje la cantidad de veces que coloque, (Ejemplo: !spam Kotomi 2)""")

@client.command()
def entretenimiento(data):
    data.subClient.send_message(data.chatId, message="""[bc]⤥〃𝐄ntreten᷍imiento༴

[c]wiki • stickerimg • stickergif • selfie • fondo • comentar • comenta • id • global • globallink • sigueme • unfollow • idlink • datos • datosusuario • gif • fancytext • coin • staffpregunta""")

@client.command()
def cutes(data):
    data.subClient.send_message(data.chatId, message="""[bc]⤥〃Cutes

[c]bailar • beber • comer • dibujar • enojado • jugar • llora • saltar • sonreir""")

@client.command()
def acciones(data):
    data.subClient.send_message(data.chatId, message="""[bc]⤥〃Acciones

[c]abrazar • alimentar • besar • cosquillas • enamorado • guiño • hifives • huir • matar • mejilla • morder • pat • patada • pegar • sonrojarse""")



######COMANDOS CHATS

@client.command("joinchat", is_it_me)
def join(data):
    val = data.subClient.join_chatroom(data.message, data.chatId)
    if val or val == "":
        data.subClient.send_message(data.chatId, f""" {data.author} me ha unido al siguiente chat: {val}
        
Debes cuidarme, si no, puede ocurrirme algo.. :((""".strip())
    else:
        data.subClient.send_message(data.chatId, "No me he podido unir al chat, ha ocurrido un error. Estoy muy triste de no poder estar en ese chat.. :((")

@client.command("leavechat", is_it_me)
def leave(data):
    if data.message:
        chat_ide = data.subClient.get_chat_id(data.message)
        if chat_ide:
            data.chatId = chat_ide
    data.subClient.send_message(chatId=data.chatId, message="Ok.. es momento de irme. Para volver a este chat, usa !joinchat para volver al chat.")
    data.subClient.leave_chat(data.chatId)

@client.command("kickchat", is_it_me)
def kickchat(data):
          mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
          for user in mention:
            data.subClient.kick(userId=str(user), chatId=data.chatId, allowRejoin=True)
            data.subClient.send_message(data.chatId, message="Ese chico malo ha sido kickeado del chat.. >w<")

@client.command("banchat", is_it_me)
def banchat(data):
          mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
          for user in mention:
            data.subClient.kick(userId=str(user), chatId=data.chatId, allowRejoin=False)
            data.subClient.send_message(data.chatId, message="Ese chico malo ha sido baneado del chat.. >w<")


@client.command("view", is_it_me)
def Vmode(data):
    id=data.subClient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
     try:
         data.subClient.edit_chat(chatId=chat, viewOnly=True)
     except:
        pass

@client.command("unview", is_it_me)
def unvmode(data):
    id=data.subClient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
     try:
         data.subClient.edit_chat(chatId=chat, viewOnly=False)
     except:
        pass

@client.command("descripcion", is_it_me)
def descripcionchat(data):
    id=data.subClient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
     try:
         data.subClient.edit_chat(chatId=chat, content=data.message)
         data.subClient.send_message(chatId=data.chatId, message="Descripcion del Chat cambiada! :3.")
     except:
        pass

@client.command("anuncio", is_it_me)
def anuncio(data):
    id=data.subClient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
     try:
         data.subClient.edit_chat(chatId=chat, announcement=data.message)
         data.subClient.send_message(chatId=data.chatId, message="Anuncio agregado! :3.")
     except:
        pass

@client.command("pinanuncio", is_it_me)
def pinanuncio(data):
    id=data.subClient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
     try:
         data.subClient.edit_chat(chatId=chat, pinAnnouncement=True)
         data.subClient.send_message(chatId=data.chatId, message="Anuncio destacado! :3.")
     except:
        pass

@client.command("titlechat", is_it_me)
def tittlechat(data):
    id=data.subClient.get_chat_threads(start=0, size=40).chatId
    for chat in id:
     try:
         data.subClient.edit_chat(chatId=chat, title=data.message)
         data.subClient.send_message(chatId=data.chatId, message="Titulo agregado! :3.")
     except:
        pass

###COMANDOS PARA KOTOMI(BOT)

@client.command("name", is_it_me)
def name(data):
	data.subClient.edit_profile(nickname=data.message)
	data.subClient.send_message(chatId=data.chatId,message=f"Mi nombre ha sido cambiado a {data.message}.. >//<", replyTo = data.messageId)

@client.command("bio", is_it_me)
def bio(data):
	data.subClient.edit_profile(content=data.message)
	data.subClient.send_message(chatId=data.chatId,message=f"Mi biografia ha sido cambiada, soy más cute.. :3", replyTo = data.messageId)

@client.command("bloquear", is_it_me)
def bloquear(data):
          mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
          for user in mention:
            data.subClient.block(userId=str(user))
            data.subClient.send_message(data.chatId, message="Ese chico malo ha sido bloqueado.. :33")

@client.command("desbloquear", is_it_me)
def desbloquear(data):
          mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
          for user in mention:
            data.subClient.unblock(userId=str(user))
            data.subClient.send_message(data.chatId, message="Ese chico malo ha sido desbloqueado.. :(")

@client.command("bgperfil", is_it_me)
def fondoperfil(data):
	info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
	reply_message = info.json['extensions']
	if reply_message:
		image = info.json['extensions']['replyMessage']['mediaValue']
		for i in range(1,5):
			data.subClient.subclient.edit_profile(backgroundImage=image)
	data.subClient.send_message(data.chatId, message="Mi fondo de perfil ha sido cambiado por el que me han enviado.. :3", replyTo = data.messageId)


###COMANDOS ADMINS IMPORTANTES

@client.command("bienvenidamuro", is_it_me)
def welcome(data):
	datamess = data.message
	if datamess:
		data.subClient.set_welcome_message(data.message)
		data.subClient.send_message(data.chatId, message="Mi bienvenida de muro, ha sido activada y cambiada con lo que me han puesto.. >w<")
	else:
		data.subClient.send_message(data.chatId, message="""Con este comando puedes ponerme una bienvenida de muro!
Dare bienvenida a cada nuevo usuario en su muro, para esto usa el mismo comando poniendo la bienvenida que quieras que tenga en la comunidad!""")

@client.command("reiniciar", is_it_me)
def reboot(args):
    sys.argv
    sys.executable
    args.subClient.send_message(args.chatId, "Reiniciandome, por favor espere.. :33")
    os.execv(sys.executable, ["Python"] + sys.argv)

@client.command()
def aminojoin(data):
  resp = joincomm(client, f"{data.message}")

  if resp["error"] == "not found":
       data.subClient.send_message(data.chatId, message="No se ha encontrado la comunidad solicitada")
  if resp["error"] == "join error":
       data.subClient.send_message(data.chatId,message="Ocurrio un error al unirse")
  if resp["error"] == "ok":
       data.subClient.send_message(data.chatId, message="Hecho!")
       print("ID de la comunidad: %s" % resp["comId"])


###COMANDOS DE ENTRETENIMIENTO


@client.command("id")
def idinfo(data):
  data.subClient.send_message(data.chatId, message=f"""{data.author} te doy las siguientes ids.. >w<
  
  Tu UserID: {data.authorId}
  Comunidad: {data.comId}
  ChatId: {data.chatId}""")

@client.command()
def idlink(data):
    id = client.get_from_code(f"{data.message}").objectId
    data.subClient.send_message(data.chatId, message=f"La ID del Link es: {id}", replyTo = data.messageId)


@client.command("terminosuser")
def terminosuser(data):
  data.subClient.send_message(data.chatId, message="""[C]Terminos y Condiciones del Usuario
[CBI]¿Que tipo de información recolectamos?
Para el correcto funcionamiento de las aplicaciones que construimos o desarrollamos, estos son algunos de los datos que recolectamos:

[I]Dato de registro  

[C]Quiero informarle que cada vez que utiliza el bot, en caso de un error y/o falla. El bot puede almacenar, texto, imágenes y otras características, para su correcto uso. 

[C]Siguiendo lo anterior, el bot puede disponer de ella libremente y/o en caso sea necesario.

[C]El usuario acepta que el contenido es de uso libre, por lo mismo anteriormente. 

[C]¿Qué hacemos con los datos que recolectamos?
Los datos recolectados son de un tipo:

[CU]Datos recolectados por nosotros.
[CU]Estos datos se registro se recolectan para obtener un feedback de que es lo que quieren nuestros usuarios y así poder mejorar brindando las correctas mejoras en cada actualización.
[CU]Los datos son manipulados a nivel de código, luego procesados en grandes cantidades, pero en ningún momento accedemos a datos de un usuario en particular, pues están encriptados y solo el usuario dueño de la información puede acceder a ellos.

                              
[C]Deseas aceptar nuestros términos y condiciones? ₍ᐢ. .ᐢ₎
[CUIB]Escribe "!acepto" si acepta, caso contrario al usar el servicio de "KOTOMI", usted acepta los términos y condidiones de esta.
""", replyTo = data.messageId)

@client.command("acepto")
def acepto(data):
    data.subClient.send_message(data.chatId, message="""Gracias por aceptar nuestros terminos y condiciones""")
    data.subClient.follow_user(data.authorId)

@client.command("selfie")
def selfieembed(data):
    url = f'{data.info.message.author.icon}'
    file = url_like(url)

    data.subClient.send_message(chatId=data.chatId, embedContent="se ha tomado una selfie.. >///<", embedTitle=f"{data.author}", file=file, fileType="image")

@client.command("comentar")
def comment_user(data):
     params = data.message

     #search
     search = re.search("=", params)
     if search:
            tmp = re.split("=", params)
            user = data.subClient.search_users(data.comId, tmp[0])
            if not user: return
            message = {
               'message': tmp[1],
               'userId': user.data.userId[0]
                 }
     else:
       message = {
         'message': params,
         'userId': data.userId
       }

     message_carga = {
      'chatId': data.chatId,
      'message': "[C]He dejado una sorpresa en su murito.. :3"}
	
     data.subClient.send_message(data.comId, message_carga)

     data.subClient.comment(message)

@client.command("comenta")
def comenta(data):
          mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
          for user in mention:
            data.subClient.comment(message=f"{data.message}", userId=str(user))
            data.subClient.send_message(chatId=data.chatId, message=f"{data.author} he dejado una sorpresita en el murito de {data.message}.. :33")



@client.command("stickerimg")
def stickerimg(data):
    info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
    reply_message = info.json['extensions']
    if reply_message:
       image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
       filename = image.split("/")[-1]
       filetype = image.split(".")[-1]
       if filetype!="gif":
           filetype = "image"
           urllib.request.urlretrieve(image, filename)
           with open(filename, 'rb') as fp:
               data.subClient.send_message(data.chatId, file=fp, fileType=filetype)
               os.remove(filename)

@client.command("stickergif")
def stickergif(data):
    info = data.subClient.get_message_info(chatId = data.chatId, messageId = data.messageId)
    reply_message = info.json['extensions']
    if reply_message:
       image = info.json['extensions']['replyMessage']['extensions']['sticker']['icon']
       filename = image.split("/")[-1]
       filetype = image.split(".")[-1]
       if filetype!="image":
           filetype = "gif"
           urllib.request.urlretrieve(image, filename)
           with open(filename, 'rb') as fp:
               data.subClient.send_message(data.chatId, file=fp, fileType=filetype)
               os.remove(filename)

@client.command("globallink")
def get_global(data):
  objectId = client.get_from_code(data.message).objectId
  data.subClient.send_message(data.chatId,message="ndc://g/user-profile/"+objectId, replyTo = data.messageId)

@client.command("global")
def globall(data):
	mention = data.subClient.subclient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
	for user in mention:
	   AID=client.get_user_info(userId=str(user)).aminoId
	   data.subClient.send_message(data.chatId,message="https://aminoapps.com/u/"+str(AID))

@client.command("sigueme")
def seguir(data):
    data.subClient.send_message(data.chatId, f'Te he seguido {data.author}.. ₍ᐢ. .ᐢ₎')
    data.subClient.follow_user(data.authorId)

@client.command("unfollow")
def unfollow(data):
    data.subClient.unfollow_user(data.authorId)
    data.subClient.send_message(data.chatId, f"Te he dejado de seguir {data.author}.. :c")

@client.command("fondo")
def bg(data):
  image = data.subClient.get_chat_thread(chatId=data.chatId).backgroundImage
  if image:
     filename = path.basename(image)
     urllib.request.urlretrieve(image, filename)
     with open(filename, 'rb') as fp: data.subClient.send_message(data.chatId, file=fp, fileType="image")
     os.remove(filename)
     data.subClient.send_message(data.chatId, message=f"{data.author} aquí tienes ei fondo del chat.. >w<", replyTo = data.messageId)
  else:
  	data.subClient.send_message(data.chatId, message="No hay fondo en este chat!")

@client.command("staffpregunta")
def staffask(data):
	msg = data.message
	data.subClient.ask_amino_staff(message=f"""[BCI]Pregunta al Staff. ૮₍ ˃̵͈᷄ . ˂̵͈᷅ ₎ა
  
{msg}

[C]Mensaje enviado por = {data.author}  
[C]Soy ╰ Kotomi ╯, fui enviada a hacerle esa pregunta al Staff. Espero que tengan bonitas tardes o noches.""") 


@client.command("checkin")
def checkin(data):
  try:
    data.subClient.check_in()
    data.subClient.lottery()
    racha = data.subClient.get_user_checkins(data.subClient.profile.userId).consecutiveCheckInDays
    data.subClient.send_message(data.chatId, message=f"Check-In y Loteria Realizados! Tienes una Racha Consecutiva de {racha} Dias en tu Check-In")
  except aminofix.lib.util.exceptions.AlreadyCheckedIn:
    racha = data.subClient.get_user_checkins(data.subClient.profile.userId).consecutiveCheckInDays
    data.subClient.send_message(data.chatId, message=f"Ya has Realizado Check-In en esta Comunidad y ya has participado en la loteria de Hoy! No olvides que tu Racha es de {racha} Dias.")
    pass


@client.command("burbujas")
def burbujas(data):
  data.subClient.send_message(data.chatId, message="""

[c]Burbujas Disponibles!

[c]1. Puddle
[c]2. Nube Rosa
[c]3. Muñeco de Nieve
[c]4. Cauldron
[c]5. Primavera
[c]6. Neon

""")

@client.command("burbuja1")
def burbujapuddle(data):
  try:
    bubble = "636d3a9c-8dfc-4f91-82fc-6219349fae55"
    data.subClient.apply_bubble(chatId=data.chatId, bubbleId=bubble, applyToAll=False)
    data.subClient.send_message(data.chatId, message="Listo! Mi burbuja ha sido cambiada en este chat!")
  except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
    data.subClient.send_message(data.chatId, message="Esta burbuja no esta entre tu Inventario de Burbujas")
    pass

@client.command("burbuja2")
def bubblehehe(data):
  try:
    bubble = "4c2d0076-8812-4023-be6a-68146bdae66d"
    data.subClient.apply_bubble(chatId=data.chatId, bubbleId=bubble, applyToAll=False)
    data.subClient.send_message(data.chatId, message="Listo! Mi burbuja ha sido cambiada en este chat!")
  except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
    data.subClient.send_message(data.chatId, message="Esta burbuja no esta entre tu Inventario de Burbujas")
    pass

@client.command("burbuja3")
def bubblehe(data):
  try:
    bubble = "5b6f3f26-498f-4776-94a7-dcae221820d6"
    data.subClient.apply_bubble(chatId=data.chatId, bubbleId=bubble, applyToAll=False)
    data.subClient.send_message(data.chatId, message="Listo! Mi burbuja ha sido cambiada en este chat!")
  except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
    data.subClient.send_message(data.chatId, message="Esta burbuja no esta entre tu Inventario de Burbujas")
    pass

@client.command("burbuja4")
def bubblehe(data):
  try:
    bubble = "ba63246f-90db-4166-b639-979fa24c7164"
    data.subClient.apply_bubble(chatId=data.chatId, bubbleId=bubble, applyToAll=False)
    data.subClient.send_message(data.chatId, message="Listo! Mi burbuja ha sido cambiada en este chat!")
  except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
    data.subClient.send_message(data.chatId, message="Esta burbuja no esta entre tu Inventario de Burbujas")
    pass

@client.command("burbuja5")
def bubblehe(data):
  try:
    bubble = "b468602e-a43e-41e3-92ec-cfcc3c5028fd"
    data.subClient.apply_bubble(chatId=data.chatId, bubbleId=bubble, applyToAll=False)
    data.subClient.send_message(data.chatId, message="Listo! Mi burbuja ha sido cambiada en este chat!")
  except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
    data.subClient.send_message(data.chatId, message="Esta burbuja no esta entre tu Inventario de Burbujas")
    pass

@client.command("burbuja6")
def bubblehe(data):
  try:
    bubble = "817c94af-9311-4856-b0a2-f02c031a09f5"
    data.subClient.apply_bubble(chatId=data.chatId, bubbleId=bubble, applyToAll=False)
    data.subClient.send_message(data.chatId, message="Listo! Mi burbuja ha sido cambiada en este chat!")
  except aminofix.lib.util.exceptions.NotOwnerOfChatBubble:
    data.subClient.send_message(data.chatId, message="Esta burbuja no esta entre tu Inventario de Burbujas")
    pass


###NO COMANDOS
@client.answer("Kotomi")
def hello(data):
    dreven = random.choice(["¡Tontito! Dejame dormir.. :c", "Sabia que no puedes vivir sin mi.. >w<", "Hola, mi amante todo precioso.. :33", "¿Necesitas ayuda en algo? Utiliza !help 2 y entraras en un mundo magico.. :3"])
    data.subClient.send_message(data.chatId, dreven, replyTo = data.messageId)

@client.answer("te amo")
def drevlover(data):
    drevlove = random.choice(["¡Ja! yo no puedo amarte, animal.", "Que cute eres.. :3", "Simplemente no puedo evitar quererte mucho.. >//<"])
    data.subClient.send_message(data.chatId, drevlove, replyTo = data.messageId)


###COMANDOS PRUEBA

@client.command("hifives")
def hifivegif(data):
    hifivegifs = random.choice(["https://c.tenor.com/_KGWqG2EBdIAAAAC/anime-girls.gif", "https://c.tenor.com/ctl_4NqVGkMAAAAd/meliodas-friends.gif", "https://c.tenor.com/i3wzYOB5XysAAAAC/yes-high-five.gif", "http://4.bp.blogspot.com/-zFgKJCMQY0s/VCh7Q7B6NCI/AAAAAAAAUbQ/RQu02-605Uw/s1600/Futs%C5%AB%2Bno%2BJoshik%C5%8Dsei%2Bga%2BLocodol%2BYattemita2.gif"])
    url = hifivegifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha chocado los cincos con {data.message}.. >w<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("llorar")
def lloragif(data):
    lloragifs = random.choice(["https://c.tenor.com/EFBwy6rvcXEAAAAC/sad-anime.gif", "https://mkgifs.com/wp-content/uploads/2022/03/Tanjiro-sad-gif.gif", "https://c.tenor.com/gqkjE1ZY3_MAAAAd/jahy-jahy-sama.gif","https://media.tenor.com/vo4nL75ku1gAAAAC/oshi-no-ko-hoshino-ruby.gif"])
    url = lloragifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta llorando.. :((", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("besar")
def besargif(data):
    besargifs = random.choice(["https://c.tenor.com/tNClex-tMZQAAAAC/kiss-beso.gif", "https://i.pinimg.com/originals/49/7a/55/497a5523d9b1ca23db84ecc3f5d8b1b3.gif", "https://i.gifer.com/2Lmc.gif", "https://64.media.tumblr.com/ba1d2520a76b9c0dd40b971d7a987a52/tumblr_nbl7d3jLuD1tz85kto1_500.gif", "https://c.tenor.com/Yu-sfUdLMAUAAAAC/koi-to-uso-anime.gif", "https://pa1.narvii.com/6048/2fabab7e31ef8d545acef4373a3807e220fd971c_hq.gif", "https://pa1.narvii.com/6430/304d4ed829d894a70d1db64568302059f8446e7f_hq.gif", "https://c.tenor.com/SZUxOrwuypgAAAAd/beso-kiss.gif", "https://c.tenor.com/cLoax6i1w34AAAAC/citrus-anime-kiss.gif","https://pa1.narvii.com/6185/20223264e0180f72bebf50adba0a949e14b7e510_hq.gif"])
    url = besargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha besado apasionadamente a {data.message}.. :33", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("mejilla")
def mejillagif(data):
    mejillagifs = random.choice(["https://i.pinimg.com/originals/97/2c/2e/972c2eb564b9936ab05ffa960c1c632e.gif", "https://acegif.com/wp-content/uploads/anime-kiss-19.gif", "https://c.tenor.com/HrxtQWBHI6cAAAAC/diane-kiss.gif", "http://pa1.narvii.com/6120/d684eb880876c41a223386f8ba34179689b220c7_00.gif", "https://c.tenor.com/Yu2a1FmxFK8AAAAC/love-sweet.gif", "https://c.tenor.com/wr6fXkybDbkAAAAC/girl-anime.gif", "https://c.tenor.com/JQ9jjb_JTqEAAAAC/anime-kiss.gif", "https://c.tenor.com/EQeihkM16pUAAAAC/anime-kiss.gif", "http://i.skyrock.net/5079/88775079/pics/3174561165_1_11_1IKppSSS.gif","https://img1.ak.crunchyroll.com/i/spire2/39fbc1e8ba8e7431d79494e53bee6de31536441455_full.gif"])
    url = mejillagifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha besado en la mejilla a {data.message}.. :33", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("cosquillas")
def cosquillasgif(data):
    cosquillasgifs = random.choice(["https://c.tenor.com/PXL1ONAO9CEAAAAM/tickle-laugh.gif", "https://c.tenor.com/L5-ABrIwrksAAAAC/tickle-anime.gif", "https://c.tenor.com/ymMtVnW-TrYAAAAd/nekopara-anime.gif", "https://pa1.narvii.com/6350/885268cd63e16e4404a071f6423f1f80728c367c_hq.gif"])
    url = cosquillasgifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"le esta haciendo cosquillas a {data.message}.. >w<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("matar")
def matargif(data):
    matargifs = random.choice(["https://64.media.tumblr.com/b73e4f79bbf11e331d74a4e1d4d18acc/tumblr_mxk3qzXabI1s1azceo1_500.gif", "http://pa1.narvii.com/6229/dfeee5bf8eb1c01c478efa7e2d6aa64f85cca5a9_00.gif","https://preview.redd.it/716vygnoaiwa1.gif?s=271fb3f059256dad830b4bf601aa3af19af6e08c"])
    url = matargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha acabado matando a {data.message}.. >.<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("comer")
def comergif(data):
    comergifs = random.choice(["https://i.pinimg.com/originals/4e/54/cc/4e54ccbf373f82cc20fe9fd3cf2bf036.gif", "https://c.tenor.com/r0TXbxJf1JsAAAAC/comer-pastel.gif","https://i.pinimg.com/originals/8d/c7/59/8dc7597447066b2850742cebe85509b1.gif","https://i.pinimg.com/originals/b7/d4/b9/b7d4b9563d01bd7315932c6bdaf44db7.gif"])
    url = comergifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta comiendo.. >.<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("trascender")
def trascendergif(data):
    trascendergifs = random.choice(["https://i.pinimg.com/originals/f3/66/d1/f366d1bd4bb03840b9c98d13a2bf5f08.gif", "https://pa1.narvii.com/6136/87c41c6ada4a07e3633dbf174e03cca4d2e2f11b_hq.gif", "https://media.tenor.com/AJF9BFYmgvgAAAAM/pani-poni-dash-ichijou.gif", "https://media.tenor.com/wMGst1EVs7gAAAAC/enemigo-akatsuki.gif"])
    url = trascendergifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha trascendido..", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("suicidiarse")
def suicidarsegif(data):
    suicidarsegifs = random.choice(["https://media.tenor.com/okTZYEmzZ8wAAAAC/adios-lagrimas.gif", "https://d.wattpad.com/story_parts/39/images/154a5c83ecb03e58828137007566.gif"])
    url = suicidarsegifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"Se ha suicidado ☠..", embedTitle=f"{data.author}", file=file, fileType="gif")



@client.command("alimentar")
def alimentargif(data):
    alimentargifs = random.choice(["https://pa1.narvii.com/6347/361cd75f09a10e757230152ac63aef369f489c04_hq.gif", "https://pa1.narvii.com/6049/7eae49d356f9d44eef3998e073cb8847f7ad802a_hq.gif", "https://c.tenor.com/3b7uYr2qLb8AAAAC/nyanko-days.gif"])
    url = alimentargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta alimentando a su pequeño bebe {data.message}.. :33", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("huir")
def huyendogif(data):
    huyendogifs = random.choice(["https://pa1.narvii.com/6139/84a53675e2f7664073f3750becaa26b408a5d990_hq.gif", "https://c.tenor.com/CRtScm9kMJUAAAAC/corran-corred.gif"])
    url = huyendogifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta huyendo de algo.. :((", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("saltar")
def saltargif(data):
    saltargifs = random.choice(["https://i.pinimg.com/originals/65/c2/6e/65c26e590bbb1387cbd9366376f5f1f9.gif", "http://pa1.narvii.com/6154/156aa081932fdc274eb7398fd0000d2bad88ad5a_00.gif"])
    url = saltargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta saltando alegremente.. >w<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("sonreir")
def sonreirgif(data):
    sonreirgifs = random.choice(["https://pa1.narvii.com/6621/4c502e8666f1b8012504952d07e28ac2332c949f_hq.gif", "https://i.pinimg.com/originals/ca/ea/f1/caeaf1d6541649bbb000ab4ad5096568.gif"])
    url = sonreirgifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta sonriendo.. c:", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("jugar")
def jugargif(data):
    jugargifs = random.choice(["https://c.tenor.com/2MmFAis2SjIAAAAC/chica-anime.gif", "https://pa1.narvii.com/6149/1cc2e4d802d040d62189a8d789cf6196df38a61e_hq.gif", "http://pa1.narvii.com/6044/3b44f8982a08761c0c3d9ce6385581afdfb925ab_00.gif"])
    url = jugargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta jugando su juego favorito.. >.<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("enojado")
def enojadogif(data):
    enojadogifs = random.choice(["https://acegif.com/wp-content/gif/angry-46.gif","https://media.tenor.com/zrkPAalAcMUAAAAC/kanojo-mo-kanojo-rika.gif"])
    url = enojadogifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"{data.author} esta enojado..(¬_¬ ) >.<", embedTitle=f"¡Cuidado! {data.author}", file=file, fileType="gif")

@client.command("dibujar")
def dibujargif(data):
    dibujargifs = random.choice(["https://i.pinimg.com/originals/92/dd/00/92dd00f34385cac3eab40added5539aa.gif", "https://c.tenor.com/LxaQ_irnwmkAAAAC/anime-anime-gif.gif"])
    url = dibujargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta dibujando una obra de arte :3", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("beber")
def bebergif(data):
    bebergifs = random.choice(["http://pa1.narvii.com/5698/844c0a31dd6353cd8495984ddede223cd0a04673_hq.gif", "https://c.tenor.com/1eWj5qLpLDcAAAAC/anime-milk-anime.gif"])
    url = bebergifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta bebiendo su bebida favorita.. >.<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("bailar")
def bailargif(data):
    bailargifs = random.choice(["https://c.tenor.com/mKTS5nbF1zcAAAAd/cute-anime-dancing.gif", "https://c.tenor.com/clfAHFQlLYEAAAAC/anime-dance-deadman.gif"])
    url = bailargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"esta bailando al ritmo de la musica.. >w<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("enamorado")
def enamoradogif(data):
    enamoradogifs = random.choice(["https://i.pinimg.com/originals/c8/69/7a/c8697a9a6804d0a53d8d2fb0fa31ae8f.gif", "https://acegif.com/wp-content/gif/heart-eyes-3.gif", "https://c.tenor.com/7CViaHUzg78AAAAC/muero-de-amor-chica.gif", "https://acegif.com/wp-content/uploads/anime-love-50.gif"])
    url = enamoradogifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"se ha enamorado de {data.message}.. >//<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("pegar")
def golpesgif(data):
    hitgifs = random.choice(["https://c.tenor.com/XhdHGRof6WEAAAAM/anime-ataque-golpe-en-la-pared.gif", "https://i.gifer.com/I5LT.gif", "https://c.tenor.com/FaXcxpmU3PMAAAAC/anime-slap.gif", "https://c.tenor.com/Qpe8tbJURvgAAAAC/eromanga-slap.gif", "https://c.tenor.com/mKX_7m0GsVAAAAAC/anime-blends.gif", "https://c.tenor.com/xc19_U9dSNMAAAAC/chika-fujiwara-hit.gif","https://1.bp.blogspot.com/-N3-ClaatbWE/YOpkM5QNZQI/AAAAAAACNc8/icb4whbr-_08acv3c3bOp1lrthylXscXQCPcBGAsYHg/s1920/Kanojo%2Bmo%2BKanojo%2B-%2BEpisode%2B2%2B-%2BSaki%2BSlaps%2BNaoya.gif"])
    url = hitgifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha golpeado fuertemente a {data.message}.. >.<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("morder")
def mordergif(data):
    mordidasgifs = random.choice(["https://pa1.narvii.com/6547/3b0256b46869d86c221a3df4a161bf874d3ab017_hq.gif", "http://pa1.narvii.com/6354/9cb8a8d8aa07f7f2f4ae47a6b194fb1cb9a1afb3_00.gif", "https://c.tenor.com/noV5mMA7T8oAAAAM/loli-bite.gif", "https://pa1.narvii.com/6228/66a5591c766f364b62da5d77370861c796faa390_hq.gif"])
    url = mordidasgifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha mordido a {data.message}.. >//<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("patada")
def patadagif(data):
    patadagifs = random.choice(["https://i.pinimg.com/originals/b1/94/a9/b194a9ce557297165aafc3046a671744.gif", "https://pa1.narvii.com/6357/385a2be62f29d48c5bb17b1394d167f06da83ba5_hq.gif", "https://i.gifer.com/8DpL.gif", "https://c.tenor.com/dOkrN01Cc0wAAAAC/dodginaaa-anime.gif"])
    url = patadagifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"le ha dado una patada K.O a {data.message}.. >.<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("sonrojarse")
def sonrojarsegif(data):
    sonrojadogifs = random.choice(["https://c.tenor.com/jV9COSlMsBkAAAAd/sonrojo-cyan.gif", "https://pa1.narvii.com/6103/ea55b9171ee7210eafcb4e2ed554d77dd4dfcc2d_hq.gif", "https://i.pinimg.com/originals/ef/d5/38/efd53867ad9691d7cace6a30c5d7d865.gif", "https://animesher.com/orig/1/136/1366/13666/animesher.com_sonrojo-orejitas-acchi-kocchi-1366659.gif"])
    url = sonrojadogifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha sido sonrojado por {data.author}.. >//<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("abrazar")
def abrazargif(data):
    abrazargifs = random.choice(["https://aniyuki.com/wp-content/uploads/2022/06/anime-hugs-aniyuki-55.gif", "https://i.gifer.com/origin/5f/5fc7024b3bee25e36b8bd857baebe0a3.gif", "https://media.tenor.com/T2Bydw8DxCkAAAAC/un-abrazo-amiga-abrazo.gif", "https://gifdb.com/images/thumbnail/abrazos-anime-guy-hugging-girl-miwc09feqiaxcpsj.gif", "https://i.gifer.com/8R4C.gif","https://www.gratistodo.com/wp-content/uploads/2021/12/Anime-gifs-de-Amor-2.gif"])
    url = abrazargifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"ha abrazado a {data.author}.. 7w7", embedTitle=f"{data.author}", file=file, fileType="gif")
@client.command("pat")
def patgif(data):
    patgifs = random.choice(["https://media.tenor.com/68Eb6wgF5rcAAAAC/anime-pat.gif", "https://media.tenor.com/-hkJYNs7tUkAAAAC/anime-pat.gif", "https://media.tenor.com/juz5uR4pJeEAAAAC/pat-anime.gif", "https://thumbs.gfycat.com/EnchantingObedientGermanspitz-max-1mb.gif", "https://pa1.aminoapps.com/6451/a2ed84c9d486fff04ce6769b2e365baf1bba4d6a_hq.gif", "https://media.tenor.com/lOawy4d-SHMAAAAd/anime-cuddle-gauge.gif"])
    url = patgifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"le ha dado un pat en la cabeza a {data.author}.. >//<", embedTitle=f"{data.author}", file=file, fileType="gif")

@client.command("guiño")
def guiñogif(data):
    guiñogifs = random.choice(["https://tenor.com/view/rezero-anime-wink-quiero-verte-gif-10089992", "https://media.tenor.com/b1CQ7t-3A88AAAAC/gui%C3%B1o-saludo.gif", "https://i.pinimg.com/originals/f8/53/9f/f8539f656d2ed90be7cd3bbe95d263d2.gif", "https://img.wattpad.com/19a96d476576cd3c5e6a9534366181ce049fe17a/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f496548787a6b64757430336156773d3d2d3234393733373339392e313434386563343963313432306265392e676966", "https://animemotivation.com/wp-content/uploads/2022/12/chisato-lycoris-recoil-wink.gif", "https://i.gifer.com/41cn.gif","https://aniyuki.com/wp-content/uploads/2023/05/aniyuki-oshi-no-ko-gif-31.gif"])
    url = guiñogifs
    file = url_like(url)

    data.subClient.send_message(data.chatId, embedContent=f"le ha dado un guiño a {data.author}.. >//<", embedTitle=f"{data.author}", file=file, fileType="gif")

###...

@client.command("habla")
def say_something(data):
    audio_file = f"sound/ttp.mp3"
    gTTS(text=data.message, lang='es', slow=False).save(audio_file)
    with open(audio_file, 'rb') as fp:
        data.subClient.send_message(data.chatId, file=fp, fileType="audio")
        os.remove(audio_file)

archivo = io.open("mensajes.txt", "a", encoding="utf-8") # abre o crea el archivo mensajes.txt en modo append

@client.on_message()
def read_message(data):
    print(data.message) # imprime el mensaje recibido
    archivo.write(data.message + "\n") # escribe el mensaje en el archivo con un salto de línea

@client.command("lives")
def lives(data):
	client.start_vc(comId=data.comId,chatId=data.chatId)

@client.command("datos")
def datos(data):
	rep = data.subClient.get_user_info(data.authorId).reputation
	lvl = data.subClient.get_user_info(data.authorId).level
	crttime = data.subClient.get_user_info(data.authorId).createdTime
	followers = data.subClient.get_user_achievements(data.authorId).numberOfFollowersCount
	profilchange = data.subClient.get_user_info(data.authorId).modifiedTime
	commentz = data.subClient.get_user_info(data.authorId).commentsCount
	posts = data.subClient.get_user_achievements(data.authorId).numberOfPostsCreated
	followed = data.subClient.get_user_info(data.authorId).followingCount
	sysrole = data.subClient.get_user_info(data.authorId).role
	data.subClient.send_message(data.chatId, message=f"""[BCI]Datos del Usuario. ૮₍ ˃̵͈᷄ . ˂̵͈᷅ ₎ა

[C]Reputación = {rep}

[C]Nivel = {lvl}

[C]Creación = {crttime}

[C]Seguidores = {followers}

[C]Perfil modificado el = {profilchange}

[C]Comentarios = {commentz}

[C]Publicaciones = {posts}

[C]Seguidos = {followed}

[C]Rol = {sysrole}
""", embedTitle=data.author, embedContent="Datos del Usuario.", embedLink="http://aminoapps.com/u/Serval", embedImage=url_like(data.authorIcon))

@client.command("datosusuario")
def datosusuario(data):
       mention = data.subClient.get_message_info(chatId=data.chatId, messageId=data.messageId).mentionUserIds
       for obj in mention:
       #iddd=client.get_from_code(data.message).objectId
        fotoo = data.subClient.get_user_info(obj).icon
        #obj = client.get_from_code(data.message).objectId
       nick = data.subClient.get_user_info(obj).nickname
       rep = data.subClient.get_user_info(obj).reputation
       lvl = data.subClient.get_user_info(obj).level
       crttime = data.subClient.get_user_info(obj).createdTime
       followers = data.subClient.get_user_achievements(obj).numberOfFollowersCount
       profilchange = data.subClient.get_user_info(obj).modifiedTime
       commentz = data.subClient.get_user_info(obj).commentsCount
       posts = data.subClient.get_user_achievements(obj).numberOfPostsCreated
       followed = data.subClient.get_user_info(obj).followingCount
       sysrole = data.subClient.get_user_info(obj).role
       data.subClient.send_message(data.chatId, message=f"""[BCI]Datos del Usuario. ૮₍ ˃̵͈᷄ . ˂̵͈᷅ ₎ა

[C]Reputación = {rep}

[C]Nivel = {lvl}

[C]Creación = {crttime}

[C]Seguidores = {followers}

[C]Perfil modificado el = {profilchange}

[C]Comentarios = {commentz}

[C]Publicaciones = {posts}

[C]Seguidos = {followed}

[C]Rol = {sysrole}
""", embedTitle=nick, embedContent="Datos del Usuario.", embedLink="http://aminoapps.com/u/Serval", embedImage=url_like(fotoo))


#PRUEBAS COMANDOS
#1.-
@client.command("love")
def love(data):
		msg = data.message + " null null "
		msg = msg.split(" ")
		msg[2] = msg[1]
		msg[1] = msg[0]
		try:
			data.subClient.send_message(data.chatId, message=f"[c]la probabilidad de amor entre {msg[1]} y {msg[2]} es {random.randint(0,100)}%",replyTo=data.messageId)
		except:
			pass

#2.-
@client.event("mention")
def mention(data):
	mention = data.subClient.send_message(chatId=data.chatId, messageId=data.messageId).mentionUserId
	for user in mention:
		data.subClient.send_message(chatId=data.chatId, message="aqui estoy amo.",replyTo=data.messageId)
#este lo puse recien por si le hacian @
#este respondiera con algo.

#3.-

#4.-
@client.answer("hola")
def hellos(data):
    data.subClient.send_message(data.chatId, message="aqui no se saluda",replyTo=data.messageId)

@client.answer("xd")
def xdd(data):
    data.subClient.send_message(data.chatId, message="Xd",replyTo=data.messageId)

@client.answer("bueno")
def bueno(data):
    data.subClient.send_message(data.chatId, message="bueno",replyTo=data.messageId)

@client.answer("buenas")
def buenas(data):
    data.subClient.send_message(data.chatId, message="buenas",replyTo=data.messageId)

@client.answer("uy")
def uy(data):
    data.subClient.send_message(data.chatId, message="Uy kieto!",replyTo=data.messageId)

@client.answer(":0")
def sorpresa(data):
    data.subClient.send_message(data.chatId, message=":0",replyTo=data.messageId)

@client.answer("yo")
def yo(data):
    data.subClient.send_message(data.chatId, message="tú?",replyTo=data.messageId)



#5.-
@client.command("icon", is_it_me)
def icon(args):
	info = args.subClient.get_message_info(chatId = args.chatId, messageId = args.messageId)
	reply_message = info.json['extensions']
	if reply_message:
		image = info.json['extensions']['replyMessage']['mediaValue']
	filename = image.split("/")[-1]
	filetype = image.split(".")[-1]
	urllib.request.urlretrieve(image, filename)
	with open(filename, 'rb') as image:
		for i in range(1,10):
			try:
				args.subClient.edit_profile(icon=image)
			except Exception:
					args.subClient.send_message(args.chatId, message="Listo",replyTo=args.messageId)

#6.-
@client.command("ping", is_it_me)
def test(data):
	timestamp = time.time()
	data.subClient.send_message(chatId=data.chatId, message=".",replyTo=data.messageId)
	time.sleep(0.10)
	data.subClient.send_message(chatId=data.chatId, message=f"Tiempo de procesamiento {time.time()- timestamp:.2f}s.")

#7.-
@client.answer("no")
def no(data):
    data.subClient.send_message(data.chatId, message="no que?",replyTo=data.messageId)

#8.-
@client.answer("uwu")
def uwu(data):
    data.subClient.send_message(chatId=data.chatId,message="UwU",replyTo=data.messageId)

#9.-
@client.answer("si")
def si(data):
    data.subClient.send_message(data.chatId, message="si que?",replyTo=data.messageId)

#10.-

@client.command("startvc")
def startvc(args):
	client.start_vc(comId=args.comId,chatId=args.chatId)
	args.subClient.send_message(chatId=args.chatId,message="llamada empezada",replyTo=args.messageId)

@client.command("endvc")
def endvc(args):
	client.end_vc(comId=args.comId,chatId=args.chatId)
	args.subClient.send_message(chatId=args.chatId,message="llamada terminada",replyTo=args.messageId)

#11.-
@client.command("fancytext")
def fancytext(data):
	msg = data.message + " null "
	msg = msg.split(" ")
	msg[1] = msg[0]
	data.subClient.send_message(data.chatId, message=fancy.light(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.bold(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.box(msg[1]))
	data.subClient.send_message(data.chatId, message=fancy.sorcerer(msg[1]))


#12.-

@client.command("everyone", is_it_me)
def menciones(data):
    usuarios = []
    for cantidad in range(0, 1000, 100):
        usuario = data.subClient.get_chat_users(data.chatId, start = cantidad, size = 1000).json
        for user in usuario:
            usuarios.append(user['uid'])
    data.subClient.send_message(data.chatId, message= f"<$@{data.message}$>", mentionUserIds = usuarios)

#13.-
@client.command()
def gif(data):
  api_instance = gc.DefaultApi()
  api_key = 'JAkGkNBHGXxIDhNibA1dNxAM2jW4XG3E'
  query = data.message
  fmt = 'gif'
  response = api_instance.gifs_search_get(api_key,query,limit=1,offset=random.randint(1,10),fmt=fmt)
  gif = response.data[0]
  url= gif.images.downsized.url
  #print(url)

  urllib.request.urlretrieve(url,f"{data.message}.gif")
  with open(f"{data.message}.gif","rb") as file:
  	data.subClient.send_message(chatId=data.chatId,file=file,fileType="gif")
  	os.remove(f"{data.message}.gif")


###NAGISA

def rutas(ruta=getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

@client.command("dance")
def dance(data):
    imagen = rutas ("img/dance")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"Esta bailando", embedTitle=f"{data.author}", file=aud, fileType="gif")

@client.command("clorox")
def clorox(data):
    imagen = rutas ("img/clorox")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"Esta bebiendo clorox", embedTitle=f"{data.author}", file=aud, fileType="gif")

@client.command("correr")
def correr(data):
    imagen = rutas ("img/correr")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"Esta corriendo", embedTitle=f"{data.author}", file=aud, fileType="gif")

@client.command("sad")
def timido(data):
    imagen = rutas ("img/cry")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"Esta sad", embedTitle=f"{data.author}", file=aud, fileType="gif")

@client.command("desaparecer")
def desaparecer(data):
    imagen = rutas ("img/dance")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"Ha desapericido...", embedTitle=f"{data.author}", file=aud, fileType="gif")

@client.command("hit")
def hit(data):
    imagen = rutas ("img/hit")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"ha golpeado a {data.message}..", embedTitle=f"{data.author}", file=aud, fileType="gif")

@client.command("nalgada")
def nalgada(data):
    imagen = rutas ("img/nalgada")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"ha nalgueado a {data.message}..", embedTitle=f"{data.author}", file=aud, fileType="gif")

@client.command("saludo")
def saludo(data):
    imagen = rutas ("img/saludo")
    with open(str(random.choice(imagen)), "rb") as aud:
        data.subClient.send_message(data.chatId, embedContent=f"Ha saludado a todos.", embedTitle=f"{data.author}", file=aud, fileType="gif")


#####

#####CARA O CRUZ
@client.command("suerte")
def caracoroa(data):
    moeda = ["Cara", "Cruz"]
    while True:
        try:
            data.subClient.send_message(chatId=data.chatId, message=f"[bc]{choice(moeda)}")
            break
        except:
            print(f"Error... Intentalo nuevamente en 5 segundos.")
            time.sleep(5)

#####

client.launch(True)
print("pronto!")


import time
import subprocess
import os
import sys

def restart_script():
    # Ruta absoluta del archivo de script
    script_path = 'main.py'

    # Ejecuta el nuevo proceso, reemplazando el proceso actual
    os.execv(sys.executable, [sys.executable, script_path])

while True:
    # Espera 1 minuto antes de reiniciar el script
    time.sleep(4800)
    restart_script()

#####

#socket
def restart():
    while True:
        time.sleep(120)
        count = 0
        for i in threading.enumerate():
            if i.name == "restart_thread":
                count += 1
        if count <= 1:
            print("Restart")
            client.socket.close()
            client.socket.start()
