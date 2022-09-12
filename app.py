from flask import Flask, render_template

from website import create_app

app = Flask(__name__)




if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)