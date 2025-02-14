from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Initialize app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medical_history.db'

# Initialize database
db = SQLAlchemy(app)



from App import routes
from App import db
# Create database tables
with app.app_context():
    db.create_all()