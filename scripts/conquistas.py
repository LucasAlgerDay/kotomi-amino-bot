from sys import argv as args
from json import dumps, load
from os import system
import os
import sys
basejson = {}

# Compruebe si ya existe un archivo .json para ese usuario
try:
    open(f"info/{args[1]}.json")
except FileNotFoundError:
    # Si no, se crea el .json
    genjson = dumps(basejson)
    open(f"info/{args[1]}.json", "w+").write(genjson)

if args[2] != "ignore":
    # Cargue el archivo json del usuario para realizar cambios en los logros
    jeyson = open(f"info/{args[1]}.json", "r")
    loadjson = load(jeyson)

    # Agregar logro a la lista de logros del usuario
    try:
        loadjson["achievements"].append(args[2])
    except KeyError:
        loadjson["achievements"] = [args[2]]

    # Guardar en un archivo json
    open(f"info/{args[1]}.json", "w+").write(dumps(loadjson))

os.system(f"python3 scripts/ranking.py {args[1]} {args[3]}")
