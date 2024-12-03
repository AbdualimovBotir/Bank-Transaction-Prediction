from flask import Flask

app = Flask(__name__)

# Flask ilovasining ba'zi konfiguratsiyalarini bu yerda sozlash mumkin

from app import routes

