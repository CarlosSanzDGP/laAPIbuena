#api.py
from flask import Flask, request
from config import PORT
from controller.carlos import generateController

app = Flask (__name__)

generateController(app)

app.run("0.0.0.0", PORT, debug=True)