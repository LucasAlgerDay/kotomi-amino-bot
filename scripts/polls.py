from json import load, dumps
from sys import argv as args

# Crear una encuesta
if args[1] == "crear":
    enquete = {}

    for l in args[3:]:
        enquete[l] = 0
    
    # encuesta JSON
    jsonpoll = dumps(enquete)
    open(f"enquetes/{args[2]}.json", "w+").write(jsonpoll)

# Vota en la encuesta con el id especificado
elif args[1] == "votar":
    jsonpoll = load(open(f"enquetes/{args[2]}.json", "r"))
    jsonpoll[args[3]] += 1
    jsonpoll = dumps(jsonpoll)
    open(f"enquetes/{args[2]}.json", "w+").write(jsonpoll)
