```python
from flask import Flask, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from src.models.user import User
from src.utilities import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_KEY'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))

        return 'Invalid username or password'

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password, email=email)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

def authenticateUser():
    user_id = session.get('user_id')

    if user_id is None:
        return None

    return User.query.get(user_id)
```