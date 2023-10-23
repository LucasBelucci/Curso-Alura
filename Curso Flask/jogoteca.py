from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config.from_pyfile('config.py')
# instanciando o banco de dados com SQL Alchemy com o banco de dados real
db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)


from views_game import *  # nopep8
from views_user import *  # nopep8

if __name__ == '__main__':
    app.run(debug=True)
