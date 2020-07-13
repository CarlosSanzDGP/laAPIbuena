#IMPORTANTE en los puntes este archivo se llama TA.py. Aqui carlos.py. He cambiado todos los enlaces para que sirva.

from src.app import app
import random
from flask import request

personajesFavoritos = {
    "Marc": "https://www.lecturas.com/medio/2020/01/16/isabel-pantoja-maestro-joao_a1654b70_875x540.jpg",
    "Juan": "https://ae01.alicdn.com/kf/H5c41e558628243998e4d947800d99f1c6.jpg",
    "Antonio": "https://pbs.twimg.com/profile_images/664146719245000704/EEQl7K44_400x400.jpg"
}

# @app.route("/Carlos")
# def saludaTa():
#     ta = random.choice(["Felipe","Amanda","Marc"])
#     return {
#         "mensaje":f"Hola soy {Ta}"
#     }


def randomTA():
    return random.choice(["Felipe", "Amanda", "Marc"])

#app.route("/ta")(lambda: f"Hola soy {randomTA()}")


@app.route("/carlos/personaje")
def personajeTa():
    ta = random.choice(list(personajesFavoritos.keys()))
    foto = personajesFavoritos[ta]
    return f"""<img src="{foto}" width="200"/>"""


@app.route("/carlos/saludo")
def ejemplo():
    print("Los args")
    print(request.args)
    # Get a query parameter <route>?nombre=pepe
    name = request.args.get("nombre")
    return f"Hola {name} de parte de {randomTA()}"