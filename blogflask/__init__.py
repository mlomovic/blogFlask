from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'f7446e435991868183813c59f0307b58'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from blogflask import routes