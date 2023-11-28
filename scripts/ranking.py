from sys import argv as args
from json import dumps, load

# Verifique el archivo json del usuario
try:
    open(f"info/{args[1]}.json")
except FileNotFoundError:
    open(f"info/{args[1]}.json", "w+").write('{"type": "normal"}')

userjson = load(open(f"info/{args[1]}.json", "r"))
try:
    int(userjson["points"])
except KeyError:
    userjson["points"] = 100


def mponto(pontos):
    global userjson
    userjson["points"] = int(userjson["points"]) + pontos
    open(f"info/{args[1]}.json", "w").write(dumps(userjson))


# Agregar puntos de comando
mponto(10)

try:
    if args[2] == "!":
        userjson["claims"] = 0
        userjson["points"] = userjson["points"] - int(float(args[3]))
        open(f"info/{args[1]}.json", "w").write(dumps(userjson))
        exit()
except IndexError:
    pass

# Comprueba cuántos acs puede tomar el usuario en función de los puntos
userjson["claims"] = userjson["points"] / 1000
open(f"info/{args[1]}.json", "w").write(dumps(userjson))

# Aquí comprueba si existe el argumento de los logros para continuar
try:
    mponto(int(args[2]))
except IndexError:
    exit()
