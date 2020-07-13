#api.py
from flask import Flask, request
from config import PORT

app = Flask (__name__)

app.run("0.0.0.0", PORT, debug=True)