from App import db



# Updated User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), unique=True, nullable=False)
    dob = db.Column(db.String(20), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    blood_type = db.Column(db.String(10), nullable=False)
    allergies = db.Column(db.String(255))
    medical_conditions = db.Column(db.String(255))
    emergency_contact = db.Column(db.String(120), nullable=False)
    emergency_phone = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)  # Store hashed passwords in production