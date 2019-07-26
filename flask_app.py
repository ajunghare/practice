
from flask import Flask
app  = None

def create_app ():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Alpha@1234@127.0.0.1/mm'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['extend_existing']=True
    return app
def get_app():
    if app:
        return app
    else:
        return create_app()