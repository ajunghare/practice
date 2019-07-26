from flask_app import get_app

app = get_app()

@app.route('/')
def hello():
    return 'hellow world';
