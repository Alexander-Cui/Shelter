from flask import Flask
app = Flask(__name__)


@app.route('/')
def main_page():
    return 'Homeless Shelters'

app.run('0.0.0.0', 8000, debug = True)