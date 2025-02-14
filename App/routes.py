from flask import session, render_template, request, redirect, url_for
from App import app, db
from App.models import User



# Routes
@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        gender = request.form['gender']
        blood_type = request.form['blood_type']
        allergies = request.form.get('allergies', '')  # Optional field
        medical_conditions = request.form.get('medical_conditions', '')  # Optional field
        emergency_contact = request.form['emergency_contact']
        emergency_phone = request.form['emergency_phone']
        username = request.form['username']
        password = request.form['password']

        user = User(
            full_name=full_name, email=email, phone=phone, dob=dob, gender=gender,
            blood_type=blood_type, allergies=allergies, medical_conditions=medical_conditions,
            emergency_contact=emergency_contact, emergency_phone=emergency_phone,
            username=username, password=password
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Invalid credentials!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/find-doctors')
def find_doctors():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('find-doctors.html')

@app.route('/book-appointment')
def book_appointment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('book-appointment.html')

@app.route('/order-medication')
def order_medication():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('order-medication.html')

@app.route('/my-profile')
def my_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('my-profile.html')

@app.route('/about-us')
def about_us():
    if 'user_id' not in session:
        return redirect(url_for(''))
    return render_template('about-us.html')

@app.route('/contact-us')
def contact_us():
    if 'user_id' not in session:
        return redirect(url_for(''))
    return render_template('contact-us.html')