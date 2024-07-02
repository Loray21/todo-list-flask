from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


app= Flask(__name__)


app.config.from_mapping(
    DEBUG = True,
    SECRET_KEY="dev",
    SQLALCHEMY_DATABASE_URI= "sqlite:///todo.db"

)

db.init_app(app)





## Registar blue print

from . import todo, auth
app.register_blueprint(todo.bp)
app.register_blueprint(auth.bp)

@app.route('/')
def index():
    return render_template("index.html")


with app.app_context():
    db.create_all()
