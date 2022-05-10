import String
from Flask import current_app, Flask, request, render_template
import json
import os
import requests

app = Flask(__name__)
APP_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(APP_DIR, 'templates')

def main():
    current_app.template_folder = TEMPLATE_DIR
    return render_template('brand.html')