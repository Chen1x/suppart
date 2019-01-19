from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'IloveChuJiaCheng'

user_info = [
    {
        'name': 'Yalam',
        'id': 'bobbyl01',
        'date': '12 Jan 2001',
        'address': 'NJC'
    },
    {
        'name': 'Yash',
        'id': 'YChellani',
        'date': '06 Apr 2000',
        'address': 'NJ Boarding'
    }
    ]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = "home")

@app.route("/users")
def users():
    return render_template('users.html', users = user_info, title = "Users")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsucessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)


